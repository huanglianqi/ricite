<template>
  <div
    id="processControl">
    <three-columns
      thirdColumnTitle="学期">
      <template
        v-slot:thirdColumn>
        <t-dropdown
          variant="outline-info"
          icon-up="calendar3-fill"
          icon-down="calendar"
          :title="term.title"
          :value="term.value"
          :first-item-title="thisTerm.title"
          :first-item-value="thisTerm.value"
          :item-list="termList"
          :select-item-func="selectTerm"></t-dropdown></template></three-columns>
    <b-jumbotron
      fluid
      bg-variant="white">
      <two-columns>
        <template v-slot:right>
          <tian-zi-ge>
            <template v-slot:rightTop>
              <number-board
                titleFront="未签署协议"
                titleBack="lalal"
                :numberFront="0"
                :numberBack="1"
                :numberFrontClass="'text-warning'"
                :numberBackClass="'text-danger'"></number-board></template>
            <template v-slot:leftTop>
              <number-board
                titleFront="未进行课程反馈"
                titleBack="lalal"
                :numberFront="10"
                :numberBack="100"></number-board></template>
            <template v-slot:rightBottom>
              <number-board
                titleFront="未完成课程反馈"
                titleBack="lalal"
                :numberFront="10"
                :numberBack="1"></number-board></template>
            <template v-slot:leftBottom>
              <number-board
                titleFront="未寄回问卷"
                titleBack="lalal"
                :numberFront="10"
                :numberBack="1"></number-board></template></tian-zi-ge></template>
        <template v-slot:left>
          lalal</template></two-columns></b-jumbotron>
    <div aria-label="list"
      v-show="!showDetail">
      <three-columns aria-label="list toolbar"
        firstColumnTitle="教师"
        secondColumnTitle="社群"
        thirdColumnTitle="学期">
        <template v-slot:firstColumn>
          <b-form
            @submit="search">
            <b-input-group>
              <b-input-group-prepend>
                <b-button
                  type="submit"
                  variant="light">
                  <b-icon
                    icon="search">
                  </b-icon>
                </b-button>
              </b-input-group-prepend>
              <b-form-input
                class="bg-light border-0"
                v-model="keyword">
              </b-form-input>
              <b-input-group-append>
                <b-button
                  variant="light">
                  <b-icon
                    icon="X">
                  </b-icon>
                </b-button>
              </b-input-group-append>
            </b-input-group>
          </b-form>
        </template>
        <template v-slot:secondColumn>
          <t-dropdown
            variant="outline-success"
            icon-up="folder-check"
            icon-down="folder-plus"
            :title="group.title"
            :value="group.value"
            first-item-title="个人"
            first-item-value="个人"
            :item-list="groupList"
            :select-item-func="selectGroup">
          </t-dropdown>
        </template>
        <template v-slot:thirdColumn>
          <t-dropdown
            variant="outline-info"
            icon-up="calendar-check-fill"
            icon-down="calendar-plus-fill"
            :title="term.title"
            :value="term.value"
            :first-item-title="thisTerm.title"
            :first-item-value="thisTerm.value"
            :item-list="termList"
            :select-item-func="selectTerm">
          </t-dropdown>
        </template></three-columns>
      <div
        id="desktop-container"
        class="my-5">
        <b-container
          class="bv-example-row my-3">
          <b-row>
            <b-col>
              <div
                v-for="item in processList"
                :key="item.title"
                class="shadow-sm bg-light mb-3 p-3"
                v-on:click="getProcessDetail(item.content)">
                <b-overlay
                  :show="!getListCompletely">
                  <b-row
                    class="mb-3 mt-1">
                    <b-col
                      class="text-left font-weight-bolder">
                      <b-icon
                        icon="circle-fill"
                        :variant="item.variant">
                      </b-icon>
                      {{item.title}}
                      <b-badge
                        class="float-right"
                        :variant="item.variant">
                        <b-icon
                          icon="people-fill">
                        </b-icon>
                        {{item.value}} | {{(item.value / allPeerNum * 100).toFixed(2)}}%
                      </b-badge>
                    </b-col>
                  </b-row>
                  <b-row
                    class="mb-1">
                    <b-col>
                      <b-progress
                        class="align-middle"
                        :max="allPeerNum"
                        :value="item.value"
                        :variant="item.variant">
                      </b-progress>
                    </b-col>
                  </b-row>
                </b-overlay>
              </div>
            </b-col>
            <b-col
              class="font-weight-bolder mt-4">
              <b-row
                class="mb-3">
                <b-col
                  class="shadow-sm bg-light p-5 mx-3"
                  v-on:click="getGetCourseDetail">
                  <b-overlay
                    :show="!getListCompletely">
                    <b-row>
                      <b-col
                        class="text-warning">
                        <h1>
                          {{getCoursePeerNum}}
                        </h1>
                      </b-col>
                    </b-row>
                    <b-row>
                      <b-col>
                        已签署协议
                      </b-col>
                    </b-row>
                  </b-overlay>
                </b-col>
                <b-col
                  class="shadow-sm bg-light p-5 mx-3"
                  v-on:click="getAllDetail">
                  <b-overlay
                    :show="!getListCompletely">
                    <b-row>
                      <b-col
                        class="text-danger">
                        <h1>
                          {{allPeerNum}}
                        </h1>
                      </b-col>
                    </b-row>
                    <b-row>
                      <b-col>
                        已审核通过
                      </b-col>
                    </b-row>
                  </b-overlay>
                </b-col>
              </b-row>
              <b-row>
                <b-col
                  class="shadow-sm bg-light p-5 mx-3"
                  v-on:click="gethasFeedbackDetail">
                  <b-overlay
                    :show="!getListCompletely">
                    <b-row>
                      <b-col
                        class="text-info">
                        <h1>
                          {{hasFeedbackPeerNum}}
                        </h1>
                      </b-col>
                    </b-row>
                    <b-row>
                      <b-col>
                        参与课程反馈
                      </b-col>
                    </b-row>
                  </b-overlay>
                </b-col>
                <b-col
                  class="shadow-sm bg-light p-5 mx-3"
                  v-on:click="getFinishCourseDetail">
                  <b-overlay
                    :show="!getListCompletely">
                    <b-row>
                      <b-col
                        class="text-success">
                        <h1>
                          {{finishCourseRate}}%
                        </h1>
                      </b-col>
                    </b-row>
                    <b-row>
                      <b-col>
                        预计结课率
                      </b-col>
                    </b-row>
                  </b-overlay>
                </b-col>
              </b-row>
            </b-col>
          </b-row>
        </b-container>
      </div>
      <div
        id="moble-container"
        class="my-5">
        <b-container
          class="bv-example-row my-3">
          <b-row
            class="font-weight-bolder my-3">
            <b-col
              class="shadow-sm bg-light p-5 mx-3"
              v-on:click="getGetCourseDetail">
              <b-overlay
                :show="!getListCompletely">
                <b-row>
                  <b-col
                    class="text-warning">
                    <h1>
                      {{getCoursePeerNum}}
                    </h1>
                  </b-col>
                </b-row>
                <b-row>
                  <b-col>
                    已签署协议
                  </b-col>
                </b-row>
              </b-overlay>
            </b-col>
          </b-row>
          <b-row
            class="font-weight-bolder my-3">
            <b-col
              class="shadow-sm bg-light p-5 mx-3"
              v-on:click="getAllDetail">
              <b-overlay
                :show="!getListCompletely">
                <b-row>
                  <b-col
                    class="text-danger">
                    <h1>
                      {{allPeerNum}}
                    </h1>
                  </b-col>
                </b-row>
                <b-row>
                  <b-col>
                    已审核通过
                  </b-col>
                </b-row>
              </b-overlay>
            </b-col>
          </b-row>
          <b-row
            class="font-weight-bolder my-3">
            <b-col
              class="shadow-sm bg-light p-5 mx-3"
              v-on:click="gethasFeedbackDetail">
              <b-overlay
                :show="!getListCompletely">
                <b-row>
                  <b-col
                    class="text-info">
                    <h1>
                      {{hasFeedbackPeerNum}}
                    </h1>
                  </b-col>
                </b-row>
                <b-row>
                  <b-col>
                    参与课程反馈
                  </b-col>
                </b-row>
              </b-overlay>
            </b-col>
          </b-row>
          <b-row
            class="font-weight-bolder my-3">
            <b-col
              class="shadow-sm bg-light p-5 mx-3 mb-4"
              v-on:click="getFinishCourseDetail">
              <b-overlay
                :show="!getListCompletely">
                <b-row>
                  <b-col
                    class="text-success">
                    <h1>
                      {{finishCourseRate}}%
                    </h1>
                  </b-col>
                </b-row>
                <b-row>
                  <b-col>
                    预计结课率
                  </b-col>
                </b-row>
              </b-overlay>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <div
                v-for="item in processList"
                :key="item.title"
                class="shadow-sm bg-light mb-3 p-3"
                v-on:click="getProcessDetail(item.content)">
                <b-overlay
                  :show="!getListCompletely">
                  <b-row
                    class="mb-3 mt-1">
                    <b-col
                      class="text-left font-weight-bolder">
                      <b-icon
                        icon="circle-fill"
                        :variant="item.variant">
                      </b-icon>
                      {{item.title}}
                      <b-badge
                        class="float-right"
                        :variant="item.variant">
                        <b-icon
                          icon="people-fill">
                        </b-icon>
                        {{item.value}} | {{(item.value / allPeerNum * 100).toFixed(2)}}%
                      </b-badge>
                    </b-col>
                  </b-row>
                  <b-row
                    class="mb-1">
                    <b-col>
                      <b-progress
                        class="align-middle"
                        :max="allPeerNum"
                        :value="item.value"
                        :variant="item.variant">
                      </b-progress>
                    </b-col>
                  </b-row>
                </b-overlay>
              </div>
            </b-col>
          </b-row>
        </b-container>
      </div>
    </div>
    <div aria-label="detail"
      v-show="showDetail">
      <three-columns aria-label="detail toolbar"
        firstColumnTitle="返回"
        secondColumnTitle="教师"
        thirdColumnTitle="课程">
        <template
          v-slot:firstColumn>
          <b-button
            block
            variant="outline-dark"
            class="float-left mb-2"
            v-on:click="backToList">
            <b-icon
              icon="arrow-left-short">
            </b-icon>
          </b-button>
        </template>
        <template
          v-slot:secondColumn>
          <b-form
            @submit="search">
            <b-input-group>
              <b-input-group-prepend>
                <b-button
                  type="submit"
                  variant="light">
                  <b-icon
                    icon="search">
                  </b-icon>
                </b-button>
              </b-input-group-prepend>
              <b-form-input
                class="bg-light border-0"
                v-model="keyword">
              </b-form-input>
              <b-input-group-append>
                <b-button
                  variant="light">
                  <b-icon
                    icon="X">
                  </b-icon>
                </b-button>
              </b-input-group-append>
            </b-input-group>
          </b-form>
        </template>
        <template
          v-slot:thirdColumn>
          <t-dropdown
            variant="outline-success"
            icon-up="folder-check"
            icon-down="folder-plus"
            :title="tag.title"
            :value="tag.value"
            first-item-title="全部"
            first-item-value="all"
            :item-list="tagList"
            :select-item-func="tagSelect">
          </t-dropdown>
        </template></three-columns>
      <b-container
        id="mobile-detail"
        class="bv-example-row my-3">
        <div
          v-for="item in processDetail"
          :key="item.id"
          class="shadow-sm bg-light mb-3 p-3"
          v-show="tagFilter(item.tag_name)">
          <head-img-kits
            :tow-line="true">
            <template
              v-slot:button>
              <head-img-btn
                :src="item.teacher.head_img"
                :size="'2rem'"></head-img-btn></template>
              <template
                v-slot:topText>
                {{item.teacher.name}}</template>
              <template
                v-slot:bottomText>
                {{item.teacher.phone}}</template></head-img-kits>
          <b-row
            class="font-weight-bolder">
            <b-col>
              <b-progress
                :value="item.feedback_forms.length"
                :max="item.course_num + 1"
                variant="success">
              </b-progress>
            </b-col>
          </b-row>
          <b-row
            class="ml-1 mt-1 mb-1 font-weight-bolder">
            <div
              class="overflow-auto">
              {{item.tag_name}}
            </div>
          </b-row>
          <b-row
            class="ml-1 mt-1 mb-1 font-weight-bolder">
            已完成：{{item.feedback_forms.length}}
          </b-row>
          <b-row
            class="ml-1 mt-1 mb-1 font-weight-bolder">
            总课时：{{item.course_num}} + 1
          </b-row>
          <b-row>
            <b-button
              variant="outlint-danger"
              v-on:click="delDetailItem(item.id)">
              <b-icon
                icon="trash"></b-icon>
            </b-button>
          </b-row>
        </div>
      </b-container>
      <b-container
        id="desktop-detail"
        class="bv-example-row my-3">
        <div
          v-for="item in processDetail"
          :key="item.id"
          v-show="tagFilter(item.tag_name)">
          <b-row
            class="font-weight-bolder shadow-sm bg-light mb-3 p-3">
            <head-img-kits
              :tow-line="true">
              <template
                v-slot:button>
                <head-img-btn
                  :src="item.teacher.head_img"
                  :size="'2rem'"></head-img-btn></template>
                <template
                  v-slot:topText>
                  {{item.teacher.name}}</template>
                <template
                  v-slot:bottomText>
                  {{item.teacher.phone}}</template></head-img-kits>
            <b-col
              cols="8">
              <b-row
                class="mb-1 ml-1">
                {{item.tag_name}}
                {{item.feedback_forms.length}} / ({{item.course_num}} + 1)
              </b-row>
              <b-row>
                <b-col>
                  <b-progress
                    :value="item.feedback_forms.length"
                    :max="item.course_num + 1"
                    variant="success">
                  </b-progress>
                </b-col>
              </b-row>
            </b-col>
            <b-col
              cols="1">
              <b-row>
                <b-col>
                  <b-button
                    variant="outline-danger"
                    v-on:click="delDetailItem(item.id)">
                    <b-icon
                      icon="trash"></b-icon>
                  </b-button>
                </b-col>
              </b-row>
            </b-col>
          </b-row>
        </div>
      </b-container>
    </div>
  </div>
</template>

<script>
import Axios from 'axios'
import ToolDropdownVue from './parts/ToolDropdown.vue'
import ThreeColumnsVue from './structure/ThreeColumns.vue'
import HeadImgKitsVue from './headImg/HeadImgKits.vue'
import HeadImgInfoVue from './headImg/HeadImgInfo.vue'
import HeadImgBtnVue from './headImg/HeadImgBtn.vue'
import NumberBoardVue from './parts/NumberBoard.vue'
import TianZiGeVue from './structure/TianZiGe.vue'
import TwoColumnsVue from './structure/TwoColumns.vue'

export default {
  name: 'processControl',
  components: {
    't-dropdown': ToolDropdownVue,
    'three-columns': ThreeColumnsVue,
    'head-img-kits': HeadImgKitsVue,
    'head-img-info': HeadImgInfoVue,
    'head-img-btn': HeadImgBtnVue,
    'number-board': NumberBoardVue,
    'tian-zi-ge': TianZiGeVue,
    'two-columns': TwoColumnsVue
  },
  data () {
    return {
      showDetail: false,
      headImgFormat: {
        width: 45,
        height: 45,
        class: 'm-1 mr-2',
        rounded: true,
        left: true
      },
      processList: [
        {
          title: '未签署协议',
          value: 0,
          variant: 'danger',
          content: []
        },
        {
          title: '已签署协议未反馈',
          value: 0,
          variant: 'warning',
          content: []
        },
        {
          title: '已反馈未结课',
          value: 0,
          variant: 'info',
          content: []
        },
        {
          title: '已结课',
          value: 0,
          variant: 'success',
          content: []
        }
      ],
      term: {
        title: '',
        value: ''
      },
      group: {
        title: '个人',
        value: '个人'
      },
      groupList: [
        {
          title: '机构',
          value: '机构'
        }
      ],
      processDetail: [],
      tag: {
        title: '全部',
        value: 'all'
      },
      tagList: [],
      getNoprotocalListCompletely: false,
      getNoFeedbackListCompletely: false,
      getNoAllFeedbackListCompletely: false,
      getIsAllFeedbackListCompletely: false,
      keyword: '',
      searchList: []
    }
  },
  created () {
    this.term = this.thisTerm
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
      return ls
    },
    getListCompletely () {
      return this.getNoprotocalListCompletely && this.getNoFeedbackListCompletely && this.getNoAllFeedbackListCompletely && this.getIsAllFeedbackListCompletely
    },
    allPeerNum () {
      return this.processList[0].value + this.processList[1].value + this.processList[2].value + this.processList[3].value
    },
    getCoursePeerNum () {
      let num = 0
      for (let i = 1; i < this.processList.length; i++) {
        num += this.processList[i].value
      }
      return num
    },
    hasFeedbackPeerNum () {
      return this.processList[2].value + this.processList[3].value
    },
    finishCourseRate () {
      return (this.processList[3].value / this.getCoursePeerNum * 100).toFixed(2)
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
    }
  },
  watch: {
    group (val) {
      console.log(val)
    },
    term (val) {
      this.getProgressData(val.value)
    },
    processDetail (val) {
      let ls = []
      this.tagList = []
      for (let i = 0; i < val.length; i++) {
        if (ls.indexOf(val[i].tag_name) === -1) {
          ls.push(val[i].tag_name)
        }
      }
      for (let i = 0; i < ls.length; i++) {
        this.tagList.push(
          {
            title: ls[i],
            value: ls[i]
          }
        )
      }
    }
  },
  methods: {
    delDetailItem (id) {
      Axios
        .patch(
          `flourish/update_usercourse/${id}`,
          {
            is_fake: true
          }
        )
        .catch(
          err => {
            if (String(err).indexOf('401')) {
              this.autoLogin()
              this.delDetailItem(id)
            }
          }
        )
    },
    search () {
      Axios
        .get(
          `flourish/search_usercourse/${this.keyword}/${this.term.value}/${this.tag.value}/`
        )
        .then(
          res => {
            this.processDetail = res.data.results
            this.showDetail = true
          }
        )
        .catch(
          err => {
            if (String(err).indexOf('401')) {
              this.autoLogin()
              this.search()
            }
          }
        )
    },
    reset () {
      this.keyword = ''
    },
    tagFilter (tag) {
      if (this.tag.value === 'all' || tag === this.tag.value) {
        return true
      } else {
        return false
      }
    },
    backToList () {
      this.showDetail = false
      this.tag.title = '全部'
      this.tag.value = 'all'
    },
    tagSelect (title, value) {
      this.tag.title = title
      this.tag.value = value
    },
    getAllDetail () {
      this.processDetail = this.processList[0].content.concat(
        this.processList[1].content.concat(
          this.processList[2].content.concat(
            this.processList[3].content
          )
        )
      )
      this.showDetail = true
    },
    getGetCourseDetail () {
      this.processDetail = this.processList[1].content.concat(
        this.processList[2].content.concat(
          this.processList[3].content
        )
      )
      this.showDetail = true
    },
    gethasFeedbackDetail () {
      this.processDetail = this.processList[2].content.concat(
        this.processList[3].content
      )
      this.showDetail = true
    },
    getFinishCourseDetail () {
      this.processDetail = this.processList[3].content
      this.showDetail = true
    },
    getProcessDetail (content) {
      this.processDetail = content
      this.showDetail = true
    },
    selectTerm (title, value) {
      this.term = {title: title, value: value}
    },
    selectGroup (title, value) {
      this.group = {title: title, value: value}
    },
    getProgressData (term) {
      this.getNoProtocalList(term)
      this.getNoFeedbackList(term)
      this.getNoAllFeedbackList(term)
      this.getIsAllFeedbackList(term)
    },
    getNoProtocalList (term) {
      this.getNoprotocalListCompletely = false
      Axios
        .get(
          `flourish/no_protocal_list/${term}/`
        )
        .then(
          res => {
            this.processList[0].value = res.data.count
            this.processList[0].content = res.data.results
            this.getNoprotocalListCompletely = true
          }
        )
        .catch(
          err => {
            if (String(err).indexOf('401')) {
              this.autoLogin()
              this.getNoProtocalList(term)
            } else {
              console.log(err)
            }
          }
        )
    },
    getNoFeedbackList (term) {
      this.getNoFeedbackListCompletely = false
      Axios
        .get(
          `flourish/no_feedback_list/${term}/`
        )
        .then(
          res => {
            this.processList[1].value = res.data.count
            this.processList[1].content = res.data.results
            this.getNoFeedbackListCompletely = true
          }
        )
        .catch(
          err => {
            if (String(err).indexOf('401')) {
              this.autoLogin()
              this.getNoFeedbackList(term)
            } else {
              console.log(err)
            }
          }
        )
    },
    getNoAllFeedbackList (term) {
      this.getNoAllFeedbackListCompletely = false
      Axios
        .get(
          `flourish/no_finish_course_list/${term}/`
        )
        .then(
          res => {
            this.processList[2].value = res.data.count
            this.processList[2].content = res.data.results
            this.getNoAllFeedbackListCompletely = true
          }
        )
        .catch(
          err => {
            if (String(err).indexOf('401')) {
              this.autoLogin()
              this.getNoAllFeedbackList(term)
            } else {
              console.log(err)
            }
          }
        )
    },
    getIsAllFeedbackList (term) {
      this.getIsAllFeedbackListCompletely = false
      Axios
        .get(
          `flourish/finish_course_list/${term}/`
        )
        .then(
          res => {
            this.processList[3].value = res.data.count
            this.processList[3].content = res.data.results
            this.getIsAllFeedbackListCompletely = true
          }
        )
        .catch(
          err => {
            if (String(err).indexOf('401')) {
              this.autoLogin()
              this.getIsAllFeedbackList(term)
            } else {
              console.log(err)
            }
          }
        )
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
    }
  }
}
</script>

<style>
#moble-container,
#mobile-detail {
  display: none;
}
@media screen and (max-width: 1000px) {
  #desktop-container,
  #desktop-detail {
    display: none;
  }
  #moble-container,
  #mobile-detail {
    display: block;
  }
  #moble-container > *,
  #mobile-detail> * {
    display: block;
  }
  #mobile-detail {
    padding: 0 10px 0 10px;
  }
}
</style>
