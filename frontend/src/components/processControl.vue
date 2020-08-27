<template>
  <div
    id="processControl">
    <three-columns aria-label="List Toolbar Menu"
      thirdColumnTitle="学期"
      firstColumnTitle="刷新"
      v-show="!showDetail">
      <template v-slot:firstColumn>
        <b-button
          block
          @click="refreshList"
          variant="outline-success"
          class="border-0 shadow-sm">
          <b-icon
            icon="arrow-counterclockwise"></b-icon></b-button></template>
      <template v-slot:thirdColumn>
        <tool-dropdown
          variant="outline-info"
          icon-up="calendar3-fill"
          icon-down="calendar"
          :title="term.title"
          :value="term.value"
          :first-item-title="thisTerm.title"
          :first-item-value="thisTerm.value"
          :item-list="termList"
          :select-item-func="selectTerm"></tool-dropdown></template>
      <template v-slot:secondColumn>
        <p
          class="badge badge-info text-warp p-2 m-1 d-block">
          Total - {{list.length}}</p></template></three-columns>
    <three-columns aria-label="Detail Toolbar Menu"
      thirdColumnTitle="搜索"
      v-show="showDetail">
      <template v-slot:thirdColumn>
        <b-input-group
          class="shadow-sm rounded">
          <b-input-group-prepend>
            <b-button
              variant="white"
              disabled>
              <b-icon
                icon="search"
                variant="dark"></b-icon></b-button></b-input-group-prepend>
        <b-form-input
          v-model="searchKeyword"
          type="text"
          placeholder="姓名、微信名、手机号或课程包"
          class="bg-white border-0"></b-form-input></b-input-group></template>
      <template v-slot:firstColumn>
        <b-button
          block
          class="shadow-sm border-white border-0"
          variant="outline-success"
          @click="backPage">
          Back</b-button></template>
      <template v-slot:secondColumn>
        <p
          class="badge badge-info text-warp p-2 m-1 d-block">
          Total - {{result.length}}</p></template></three-columns>
    <b-jumbotron aria-label="Main Content"
      fluid
      bg-variant="white">
      <tian-zi-ge aria-label="List Type"
        v-show="!showDetail">
        <template v-slot:leftTop>
          <number-board
            :detail="noProtocalList"
            :buttonClick="getDetail"
            titleFront="未签署协议人数"
            titleBack="未签署协议占比"
            subTitleFront="---"
            subTitleBack="相比于通过申请总人数"
            :numberFront="noProtocalListNumber"
            :numberBack="noProtocalListPercent"
            :numberFrontClass="'text-danger'"
            :numberBackClass="'text-warning'"></number-board></template>
        <template v-slot:rightTop>
          <number-board
            :detail="noFeedbackList"
            :buttonClick="getDetail"
            titleFront="未进行课程反馈人数"
            titleBack="未进行课程反馈占比"
            subTitleFront="---"
            subTitleBack="相比于签署协议总人数"
            :numberFront="noFeedbackListNumber"
            :numberBack="noFeedbackListPercent"
            :numberFrontClass="'text-info'"
            :numberBackClass="'text-warning'"></number-board></template>
        <template v-slot:leftBottom>
          <number-board
            :detail="noAllFeedbackList"
            :buttonClick="getDetail"
            titleFront="未完成课程反馈人数"
            titleBack="未完成课程反馈占比"
            subTitleFront="---"
            subTitleBack="相比于签署协议总人数"
            :numberFront="noAllFeedbackListNumber"
            :numberBack="noAllFeedbackListPercent"
            :numberFrontClass="'text-primary'"
            :numberBackClass="'text-warning'"></number-board></template>
        <template v-slot:rightBottom>
          <number-board
            :detail="noMailBackList"
            :buttonClick="getDetail"
            titleFront="未寄回问卷人数"
            titleBack="未寄回问卷占比"
            subTitleFront="---"
            subTitleBack="相比于签署协议总人数"
            :numberFront="noMailBackListNumber"
            :numberBack="noMailBackListPercent"
            :numberFrontClass="'text-success'"
            :numberBackClass="'text-warning'"></number-board></template></tian-zi-ge>
      <b-list-group aria-label="User Course List"
        v-show="showDetail"
        class="my-2">
        <b-list-group-item aria-label="User Course List Item"
          class="shadow-sm mb-2 rounded flex-column border-0 align-items-start"
          v-for="item in resultPageList"
          :key="item.id">
          <b-overlay aria-label="Person Information Button"
            class="float-left"
            :show="item.is_fake"
            rounded>
            <head-img-kit
              :twoLine="true"
              :topText="item.teacher.real_name"
              :bottomText="item.tag_name">
              <template v-slot:button>
                <div
                  @click="catPersonInfoDetail(item.teacher.id)">
                  <head-img-btn
                    v-b-modal.personInfoDetailModal
                    :rounded="false"
                    :src="item.teacher.head_img"
                    :size="'2.5rem'"></head-img-btn></div></template></head-img-kit>
            <template v-slot:overlay>
              <b-icon
                icon="trash"></b-icon></template></b-overlay>
          <b-button aria-label="Delete User Course Button"
            pill
            @click="deleteItem(item)"
            class="shadow-sm border-0 float-right m-2"
            variant="outline-danger">
            <b-icon
              v-b-tooltip.hover
              title="删除"
              v-show="!item.is_fake"
              font-scale="0.9"
              shift-v="4"
              icon="trash"></b-icon>
            <b-iconstack
              v-b-tooltip
              title="取消删除"
              v-show="item.is_fake"
              font-scale="0.9"
              shift-v="4">
              <b-icon
                stacked
                icon="x-circle-fill"
                shift-v="-6"
                shift-h="4"
                scale="0.5"></b-icon>
              <b-icon
                icon="trash"
                stacked
                scale="1"></b-icon></b-iconstack></b-button>
          <div aria-label="Apply Course Form Button"
            @click="catApplyForm(item.applycourse)"
            v-show="item.applycourse!==null">
            <b-button
              v-b-modal.applyFormDetailModal
              pill
              variant="outline-success"
              class="shadow-sm border-0 float-right m-2">
              <b-icon
                font-scale="0.9"
                shift-v="4"
                icon="arrows-angle-expand"></b-icon></b-button></div>
          <div aria-label="Feedback Button"
            v-show="item.feedback_forms.length!==0"
            @click="catDetailItem(item)">
            <b-button
              v-b-modal.feedbackListDetailModal
              pill
              variant="outline-info"
              class="shadow-sm border-0 float-right m-2">
              {{item.feedback_forms.length}}</b-button></div>
          <b-button aria-label="Confirm Mail Back Button"
            @click="confirmMailBack(item)"
            pill
            :variant="mailBackBtnVariantUpdate(item.mail_back)"
            class="shadow-sm border-0 float-right m-2">
            <b-iconstack
              v-show="item.mail_back"
              font-scale="0.9"
              shift-v="5"
              v-b-tooltip.hover
              title="已寄回">
              <b-icon
                stacked
                scale="0.6"
                shift-v="-6"
                shift-h="10"
                icon="check-circle-fill"></b-icon>
              <b-icon
                icon="envelope"></b-icon></b-iconstack>
            <b-iconstack
              v-show="!item.mail_back"
              font-scale="0.9"
              shift-v="5"
              v-b-tooltip.hover
              title="未寄回">
              <b-icon
                stacked
                scale="0.6"
                shift-v="-6"
                shift-h="10"
                icon="x-circle-fill"></b-icon>
              <b-icon
                icon="envelope"></b-icon></b-iconstack></b-button>
          <div aria-label="Submit Remarks Detail Button"
            @click="catRemarksDetail(item.id); catDetailItem(item)">
            <b-button
              v-b-modal.remarksDetailModal
              pill
              variant="outline-dark"
              class="shadow-sm border-0 float-right m-2">
              <b-icon
                icon="chat-text"
                font-scale="0.9"
                shift-v="5"></b-icon></b-button></div></b-list-group-item></b-list-group></b-jumbotron>
    <b-container
        v-show="showDetail">
        <b-row>
          <b-col>
            <b-button
              :disabled="resultPage === 1"
              @click="resultPage -= 1"
              variant="outline-success"
              class="shadow-sm border-0"
              block>
              Pre</b-button></b-col>
          <b-col>
            <small
              class="badge badge-info text-warp p-2 mt-1 d-block">
              {{resultPage}} / {{resultPageSum}}</small></b-col>
          <b-col>
            <b-button
              :disabled="result.length <= resultPage * 8 + 1"
              @click="resultPage += 1"
              variant="outline-success"
              class="shadow-sm border-0"
              block>
              Next</b-button></b-col></b-row></b-container>
    <head-img-info aria-label="Person Information Detail Modal"
      id="personInfoDetailModal"
      :info="personInfoDetail"></head-img-info>
    <modal-model aria-label="Feedback List Modal"
      id="feedbackListDetailModal"
      :size="'lg'"
      :hideFooter="true">
      <div
        v-for="btn in detailItem.feedback_forms"
        :key="btn.id"
        @click="catFeedbackForm(btn.id)"
        class="d-inline-block">
        <b-button
          v-b-modal.feedbackFormDetailModal
          pill
          variant="outline-info"
          class="shadow-sm border-0 m-2">
          {{btn.class_num}}</b-button></div>
      <b-button
        variant="outline-success"
        class="border-0 shadow-sm"
        pill
        @click="$bvModal.hide('feedbackListDetailModal')">
        <b-icon
          font-scale="0.9"
          shift-v="2"
          icon="arrows-angle-contract"></b-icon></b-button></modal-model>
    <modal-model aria-label="Apply Course Form Detail Modal"
      id="applyFormDetailModal"
      :size="'lg'"
      :hideFooter="true">
      <b-card
        border-variant="white">
        <b-list-group
          class="p-2"
          flush>
          <b-list-group-item
            class="font-weight-bold p-3 shadow-lg mb-2 bg-success text-light text-center rounded w-100 align-self-center">
            课程申请信息表</b-list-group-item>
          <b-list-group-item
            class="shadow-lg mb-2 rounded">
            <b-row>
              <small
                class="text-muted pl-1">申请学生手册数量</small></b-row>
            <b-row
              class="font-weight-bold pl-2">{{applyFormDetail.stu_num}}</b-row></b-list-group-item>
          <b-list-group-item
            class="shadow-lg mb-2 rounded">
            <b-row>
              <small
                class="text-muted pl-1">申请教师手册数量</small></b-row>
            <b-row
              class="font-weight-bold pl-2">{{applyFormDetail.teacher_num}}</b-row></b-list-group-item>
          <b-list-group-item
            class="shadow-lg mb-2 rounded">
            <b-row>
              <small
                class="text-muted pl-1">授课学校名称</small></b-row>
            <b-row
              class="font-weight-bold pl-2">{{applyFormDetail.school_name}}</b-row></b-list-group-item>
          <b-list-group-item
            class="shadow-lg mb-2 rounded">
            <b-row>
              <small
                class="text-muted pl-1">授课学校地址</small></b-row>
            <b-row
              class="font-weight-bold pl-2">{{applyFormDetail.school_address}}</b-row></b-list-group-item>
          <b-list-group-item
            class="shadow-lg mb-2 rounded">
            <b-row>
              <small
                class="text-muted pl-1">身份证照片</small></b-row>
            <b-row
              class="font-weight-bold pl-2">
              <b-img-lazy
                :src="applyFormDetail.front_img"
                fluid></b-img-lazy></b-row></b-list-group-item>
          <b-button
            @click="$bvModal.hide('applyFormDetailModal')"
            class="shadow border-0"
            variant="outline-info">
            <b-icon
              icon="arrows-angle-contract"></b-icon></b-button></b-list-group></b-card></modal-model>
    <modal-model aria-label="Feedback Detail Modal"
      id="feedbackFormDetailModal"
      :size="'lg'"
      :hideFooter="true">
      {{feedbackFormDetail}}</modal-model>
    <modal-model aria-label="User Course Remarks Detail Modal"
      id="remarksDetailModal"
      :size="'md'"
      :hideFooter="true">
      <b-form-textarea aria-label="User Course Remarks Detail Create"
        class="border-0 shadow-sm"
        v-model="remarksDetailContent"
        rows="3"></b-form-textarea>
      <three-columns>
        <template v-slot:firstColumn>
          <b-button
            @click="submitRemarksDetail"
            variant="outline-success"
            class="shadow-sm border-0"
            block>
            <b-icon
              icon="check"></b-icon></b-button></template>
        <template v-slot:secondColumn>
          <b-button
            @click="$bvModal.hide('remarksDetailModal'); remarksDetailContent=''"
            variant="outline-warning"
            class="shadow-sm border-0"
            block>
            <b-icon
              icon="x"></b-icon></b-button></template>
        <template v-slot:thirdColumn>
          <b-button
            @click="$bvModal.hide('remarksDetailModal'); remarksDetailContent='';"
            variant="outline-warning"
            class="shadow-sm border-0"
            block>
            <b-icon
              icon="x"></b-icon></b-button></template></three-columns>
      <b-list-group aria-label="User Course Remarks Detail Item"
        class="text-left">
        <b-list-group-item
          class="shadow-sm my-2 rounded flex-column border-0 align-items-start"
          v-for="item in remarksPageList"
          :key="item.id">
          <div>
            {{item.content}}</div>
          <div>
            <small
              class="text-muted float-right">
              {{item.fromPerson.last_name}}{{item.fromPerson.first_name}}</small></div>
          <div>
            <small
              class="text-muted">
              {{item.create_time.split('.')[0]}}</small></div></b-list-group-item></b-list-group>
      <b-container
        v-show="remarksDetail.length>0">
        <b-row>
          <b-col>
            <b-button
              variant="outline-success"
              class="shadow-sm border-0"
              block
              @click="remarksPage -= 1"
              :disabled="remarksPage === 1">
              Pre</b-button></b-col>
          <b-col>
            <small
              class="badge badge-info text-warp p-1 m-1 d-block">
              {{remarksPage}} / {{remarksPageSum}}</small></b-col>
          <b-col>
            <b-button
              variant="outline-success"
              class="shadow-sm border-0"
              block
              @click="remarksPage += 1"
              :disabled="remarksDetail.length <= remarksPage * 3">
              Next</b-button></b-col></b-row></b-container></modal-model>
  </div>
</template>

<script>
import ThreeColumnsVue from './structure/ThreeColumns.vue'
import ToolDropdownVue from './parts/ToolDropdown.vue'
import TwoColumnsVue from './structure/TwoColumns.vue'
import NumberBoardVue from './parts/NumberBoard.vue'
import TianZiGeVue from './structure/TianZiGe.vue'
import Axios from 'axios'
import HeadImgKitsVue from './headImg/HeadImgKits.vue'
import HeadImgBtnVue from './headImg/HeadImgBtn.vue'
import HeadImgInfoVue from './headImg/HeadImgInfo.vue'
import ModalModelVue from './parts/ModalModel.vue'
import ListPagerVue from './parts/ListPager.vue'

export default {
  name: 'processControl',
  components: {
    'three-columns': ThreeColumnsVue,
    'tool-dropdown': ToolDropdownVue,
    'two-columns': TwoColumnsVue,
    'number-board': NumberBoardVue,
    'tian-zi-ge': TianZiGeVue,
    'head-img-kit': HeadImgKitsVue,
    'head-img-btn': HeadImgBtnVue,
    'head-img-info': HeadImgInfoVue,
    'modal-model': ModalModelVue,
    'list-pager': ListPagerVue
  },
  computed: {
    termList () {
      let ls = []
      let yearDelta = new Date().getFullYear() - 2019
      for (let i = 0; i <= yearDelta; i++) {
        ls.push(
          {
            title: `${2019 + i}年春季学期`,
            value: `${i * 2}`
          },
          {
            title: `${2019 + i}年秋季学期`,
            value: `${i * 2 + 1}`
          }
        )
      }
      return ls.reverse()
    },
    thisTerm () {
      let thisMonth = new Date().getMonth()
      let thisYear = new Date().getFullYear()
      if (thisMonth < 9 && thisMonth > 3) {
        return {
          title: `${thisYear}年春季学期`,
          value: `${(thisYear - 2019) * 2}`
        }
      } else {
        return {
          title: `${thisYear}年秋季学期`,
          value: `${(thisYear - 2019) * 2 + 1}`
        }
      }
    },
    noProtocalListNumber () {
      if (this.list.length !== 0) {
        return `${this.noProtocalList.length}`
      } else {
        return '0'
      }
    },
    noProtocalListPercent () {
      if (this.list.length !== 0) {
        return `${((this.noProtocalList.length / this.list.length) * 100).toFixed(2)}%`
      } else {
        return '0%'
      }
    },
    noFeedbackListNumber () {
      if (this.list.length !== 0) {
        return `${this.noFeedbackList.length}`
      } else {
        return '0'
      }
    },
    noFeedbackListPercent () {
      if (this.list.length !== 0) {
        return `${((this.noFeedbackList.length / this.list.length) * 100).toFixed(2)}%`
      } else {
        return '0%'
      }
    },
    noAllFeedbackListNumber () {
      if (this.list.length !== 0) {
        return `${this.noAllFeedbackList.length}`
      } else {
        return '0'
      }
    },
    noAllFeedbackListPercent () {
      if (this.list.length !== 0) {
        return `${((this.noAllFeedbackList.length / this.list.length) * 100).toFixed(2)}%`
      } else {
        return '0%'
      }
    },
    noMailBackListNumber () {
      if (this.list.length !== 0) {
        return `${this.noMailBackList.length}`
      } else {
        return '0'
      }
    },
    noMailBackListPercent () {
      if (this.list.length !== 0) {
        return `${((this.noMailBackList.length / this.list.length) * 100).toFixed(2)}%`
      } else {
        return '0%'
      }
    },
    resultPageList () {
      return this.result.slice((this.resultPage - 1) * 8, 7 + (this.resultPage - 1) * 8)
    },
    resultPageSum () {
      if (this.result.length < 4) {
        return 1
      } else {
        return (this.result.length / 8).toFixed(0)
      }
    },
    remarksPageList () {
      return this.remarksDetail.slice((this.remarksPage - 1) * 3, this.remarksPage * 3)
    },
    remarksPageSum () {
      if (this.remarksDetail.length <= 2) {
        return 1
      } else {
        return (this.remarksDetail.length / 3).toFixed(0)
      }
    }
  },
  watch: {
    list (val) {
      if (val.length !== 0) {
        this.noProtocalList = this.list.filter(
          item => item.has_protocal === false
        )
        this.noFeedbackList = this.list.filter(
          item => item.has_protocal === true && item.feedback_num === 0
        )
        this.noAllFeedbackList = this.list.filter(
          item => item.has_protocal === true && item.finish_final === false && item.feedback_num > 0
        )
        this.noMailBackList = this.list.filter(
          item => item.mail_back === false
        )
      }
    },
    searchKeyword (val) {
      this.resultPage = 1
      if (val !== '' || val !== null) {
        this.result = this.detail.filter(
          item => {
            if (item.teacher.real_name.indexOf(val) !== -1) {
              return true
            } else if (item.teacher.phone === val) {
              return true
            } else if (item.tag_name.indexOf(val) !== -1) {
              return true
            } else if (item.name === val) {
              return true
            } else {
              return false
            }
          }
        )
      } else {
        this.result = this.detail
      }
    }
  },
  data () {
    return {
      term: {
        title: '选择学期',
        value: ''
      },
      list: [],
      detail: [],
      result: [],
      resultPage: 1,
      detailItem: {},
      noProtocalList: [],
      noFeedbackList: [],
      noAllFeedbackList: [],
      noMailBackList: [],
      showDetail: false,
      searchKeyword: '',
      personInfoDetail: [],
      applyFormDetail: {},
      feedbackFormDetail: {},
      mailBackDetail: false,
      remarksDetail: [],
      remarksPage: 1,
      remarksDetailContent: ''
    }
  },
  methods: {
    selectTerm (title, value) {
      this.term.title = title
      this.term.value = value
      this.getList(this.term.value)
    },
    getList (term) {
      Axios
        .get(
          `flourish/user_course_all_list/${term}`
        )
        .then(
          res => {
            this.list = res.data
          }
        )
        .catch(
          error => {
            if (error) {
              this.autoLogin()
              this.getList(term)
            }
          }
        )
    },
    refreshList () {
      this.getList(this.term.value)
    },
    getDetail (detail) {
      this.result = detail
      this.detail = detail
      this.showDetail = true
    },
    getDetailTitle (title) {
      this.listTitle = title
    },
    deleteItem (item) {
      this.catDetailItem(item)
      this.delete(item.id, item.is_fake)
    },
    delete (id, state) {
      Axios
        .patch(
          `flourish/user_course_item_update/${id}`,
          {
            'is_fake': !state
          }
        )
        .then(
          res => {
            this.detailItem.is_fake = res.data.is_fake
          }
        )
        .catch(
          err => {
            if (err) {
              this.autoLogin()
              this.delete(id, state)
            }
          }
        )
    },
    deleteIconUpdate (state) {
      if (state) {
        return 'arrow-counterclockwise'
      } else {
        return 'trash'
      }
    },
    confirmMailBack (item) {
      this.catDetailItem(item)
      this.confirm(item.id, item.mail_back)
    },
    confirm (id, state) {
      Axios
        .patch(
          `flourish/user_course_item_update/${id}`,
          {
            'mail_back': !state
          }
        )
        .then(
          res => {
            this.detailItem.mail_back = res.data.mail_back
          }
        )
        .catch(
          err => {
            if (err) {
              this.autoLogin()
              this.confirm(id, state)
            }
          }
        )
    },
    mailBackBtnVariantUpdate (state) {
      if (state === true) {
        return 'outline-success'
      } else if (state === false) {
        return 'outline-danger'
      } else {
        return 'dark'
      }
    },
    submitRemarksDetail () {
      if (this.remarksDetailContent === '') {

      } else {
        Axios
          .post(
            `flourish/create_user_course_remarks_item/`,
            {
              'content': this.remarksDetailContent,
              'fromPerson': this.$store.state.auth.id,
              'toPerson': this.detailItem.teacher.id,
              'forUserCourse': this.detailItem.id
            }
          )
          .then(
            res => {
              this.remarksDetail.unshift(res.data)
              this.remarksDetailContent = ''
            }
          )
          .catch(
            err => {
              if (err) {
                this.autoLogin()
                this.submitRemarksDetail()
              }
            }
          )
      }
    },
    backPage () {
      if (this.searchKeyword !== '') {
        this.searchKeyword = ''
      } else {
        this.showDetail = false
      }
      this.resultPage = 1
    },
    autoLogin () {
      this.$store
        .dispatch(
          'auth/login',
          {
            username: sessionStorage.username,
            password: sessionStorage.password
          }
        )
    },
    catPersonInfoDetail (id) {
      Axios
        .get(
          `flourish/get_teacher_item_info_form/${id}`
        )
        .then(
          res => {
            this.personInfoDetail = res.data.infoForms
          }
        )
        .catch(
          err => {
            if (err) {
              this.autoLogin()
              this.catPersonInfoDetail()
            }
          }
        )
    },
    catApplyForm (id) {
      if (id !== null) {
        Axios
          .get(
            `flourish/get_apply_course_item/${id}`
          )
          .then(
            res => {
              this.applyFormDetail = res.data
            }
          )
          .catch(
            err => {
              if (err) {
                this.autoLogin()
                this.catApplyForm(id)
              }
            }
          )
      }
    },
    catFeedbackForm (id) {
      Axios
        .get(
          `flourish/get_feedback_form_item/${id}`
        )
        .then(
          res => {
            this.feedbackFormDetail = res.data
          }
        )
        .catch(
          err => {
            if (err) {
              this.autoLogin()
              this.catFeedbackForm(id)
            }
          }
        )
    },
    catDetailItem (item) {
      this.detailItem = item
    },
    catRemarksDetail (id) {
      Axios
        .get(
          `flourish/get_user_course_remarks_item/${id}`
        )
        .then(
          res => {
            this.remarksDetail = res.data.user_course_remarks.reverse()
            this.remarksPage = 1
          }
        )
        .catch(
          err => {
            if (err) {
              this.autoLogin()
              this.catRemarksDetail(id)
            }
          }
        )
    }
  }
}
</script>
