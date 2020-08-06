<template>
  <div
    id="pictureManage">
    <three-columns aria-label="head toolbar"
      firstColumnTitle="起于"
      secondColumnTitle="止于"
      thirdColumnTitle="类型">
      <template v-slot:firstColumn>
        <b-input-group aria-label="start date">
          <b-form-datepicker
            v-model="startDate"
            calendar-width="100%"
            hide-header
            button-only
            button-variant="white"></b-form-datepicker>
          <b-form-input
            v-model="startDate"
            :state="checkStartDate"
            debounce=500
            placeholder="YYYY-MM-DD"
            trim></b-form-input></b-input-group></template>
      <template v-slot:secondColumn>
        <b-input-group aria-label="end date">
          <b-form-datepicker
            v-model="endDate"
            calendar-width="100%"
            hide-header
            button-only
            button-variant="white"></b-form-datepicker>
          <b-form-input
            v-model="endDate"
            :state="checkEndDate"
            debounce=500
            placeholder="YYYY-MM-DD"
            trim></b-form-input></b-input-group></template>
      <template v-slot:thirdColumn>
        <tool-dropdown
          variant="outline-success"
          iconUp="collection-play-fill"
          iconDown="collection-fill"
          :title="type.title"
          :value="type.value"
          firstItemTitle="全部图片"
          firstItemValue="feedback_pic_collect"
          :itemList="typeList"
          :selectItemFunc="selectType"></tool-dropdown></template></three-columns>

    <b-container aria-label="share list"
      class="mt-3"
      v-show="isGraph"
      v-for="item in shareList"
      :key="item.id">
      <b-row>
        <div
          v-on:click="getPersonDetail(item.teacher)">
          <head-img
            class="mr-2"
            :src="item.teacher.head_img"
            :button="true"
            v-b-modal.personDetail></head-img></div>
          <b-col><b-row><p>{{item.teacher.real_name}}</p></b-row>
          <b-row><p>{{item.content}}</p></b-row></b-col></b-row>
        <b-row>
          <div
            class="overflow-auto d-inline-block">
            <b-img-lazy
              v-for="pic in item.sharePics"
              :key="pic.url"
              class="m-2"
              height="200"
              left
              rounded
              :src="pic.url"></b-img-lazy></div></b-row></b-container>
    <person-detail
      id="personDetail"
      :detail="personDetail"></person-detail>
    <image-pad
      :show="!isGraph"
      :list="picList"></image-pad>
  </div>
</template>

<script>
import ThreeColumnsVue from './ThreeColumns.vue'
import ToolDropdownVue from './ToolDropdown.vue'
import Axios from 'axios'
import ThreeBlocksVue from './ThreeBlocks.vue'
import HeadImgVue from './HeadImg.vue'
import PersonDetailModalVue from './PersonDetailModal.vue'
import updateLikeButtonVue from './updateLikeButton.vue'
import ImagePadVue from './ImagePad.vue'

export default {
  name: 'pictureManage',
  components: {
    'three-columns': ThreeColumnsVue,
    'tool-dropdown': ToolDropdownVue,
    'three-blocks': ThreeBlocksVue,
    'head-img': HeadImgVue,
    'person-detail': PersonDetailModalVue,
    'update-like-button': updateLikeButtonVue,
    'image-pad': ImagePadVue
  },
  data () {
    return {
      headImgFormat: {
        width: 25,
        height: 25,
        class: 'ml-0 mr-2 mb-1 mt-0',
        rounded: 'circle',
        left: true
      },
      startDate: '',
      endDate: '',
      type: {
        title: '选择图片类型',
        value: ''
      },
      typeList: [
        {
          title: '图片精选',
          value: 'feedback_pic_like'
        },
        {
          title: '全部图文',
          value: 'share_list'
        },
        {
          title: '图文精选',
          value: 'share_like_list'
        }
      ],
      picList: [],
      shareList: [],
      personDetail: {},
      detail: {
        teacher: {
          real_name: '',
          name: ''
        },
        user_course: {
          tag_name: ''
        },
        feedback_form: {
          create_time: ''
        },
        pic_url: ''
      }
    }
  },
  watch: {
    endDate (val) {
      this.checkDateFormat(val)
    },
    startDate (val) {
      this.checkDateFormat(val)
    }
  },
  computed: {
    checkEndDate () {
      if (this.endDate.length === 10) {
        return true
      } else {
        return false
      }
    },
    checkStartDate () {
      if (this.startDate.length === 10) {
        return true
      } else {
        return false
      }
    },
    isGraph () {
      if (this.type.value === 'share_list' || this.type.value === 'share_like_list') {
        return true
      } else {
        return false
      }
    }
  },
  methods: {
    getPersonDetail (detail) {
      this.personDetail = detail
    },
    checkDateFormat (date) {
      if (date.length === 10) {
        this.collectList()
      }
    },
    selectType (title, value) {
      this.type.value = value
      this.type.title = title
      this.collectList()
    },
    collectList () {
      if (this.startDate !== '' && this.endDate !== '' && this.type.value !== '') {
        if (this.startDate > this.endDate) {
          this.getCollect(this.endDate, this.startDate)
        } else {
          this.getCollect(this.startDate, this.endDate)
        }
      }
    },
    getCollect (start, end) {
      if (this.type.value === 'share_list' || this.type.value === 'share_like_list') {
        Axios
          .get(
            `flourish/${this.type.value}/${end}T23:59:59/${start}T00:00:00/`
          )
          .then(
            res => {
              this.shareList = res.data.results
            }
          )
          .catch(
            err => {
              if (String(err).indexOf('401')) {
                this.autoLogin()
                this.getCollect(start, end)
              }
            }
          )
      } else {
        Axios
          .get(
            `flourish/${this.type.value}/${end}T23:59:59/${start}T00:00:00/`
          )
          .then(
            res => {
              this.picList = res.data.results
            }
          )
          .catch(
            err => {
              if (String(err).indexOf('401')) {
                this.autoLogin()
                this.getCollect(start, end)
              }
            }
          )
      }
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
</style>
