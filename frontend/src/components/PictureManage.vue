<template>
  <div
    id="pictureManage">
    <three-columns aria-label="toolbar"
      firstColumnTitle="起于"
      secondColumnTitle="止于"
      thirdColumnTitle="类型">
      <template v-slot:firstColumn>
        <b-input-group aria-label="start date">
          <b-form-datepicker
            v-model="startDate"
            calendar-width="100%"
            hide-header
            selected-variant="success"
            menu-class="shadow-sm border-0 mt-2 w-100"
            class="border-white border-0 bg-white shadow-sm p-1"></b-form-datepicker></b-input-group></template>
      <template v-slot:secondColumn>
        <b-input-group aria-label="end date">
          <b-form-datepicker
            v-model="endDate"
            calendar-width="100%"
            hide-header
            selected-variant="success"
            menu-class="shadow-sm border-0 mt-2 w-100"
            class="border-white border-0 bg-white shadow-sm p-1"></b-form-datepicker></b-input-group></template>
      <template v-slot:thirdColumn>
        <tool-dropdown
          variant="outline-info"
          iconUp="image"
          iconDown="images"
          :title="type.title"
          :value="type.value"
          firstItemTitle="课堂图片 ｜ 全部"
          firstItemValue="feedback_image_all_list"
          :itemList="typeList"
          :selectItemFunc="selectType"></tool-dropdown></template></three-columns>
    <image-pad
      v-show="!isGraph"
      :list="feedbackImgList"></image-pad>
    <graphic-pad
      v-show="isGraph"
      :list="shareGraphicList"></graphic-pad>
  </div>
</template>

<script>
import ThreeColumnsVue from './structure/ThreeColumns.vue'
import ToolDropdownVue from './parts/ToolDropdown.vue'
import Axios from 'axios'
import ImagePadVue from './ImagePad.vue'
import GraphicSetVue from './GraphicSet.vue'

export default {
  name: 'pictureManage',
  components: {
    'three-columns': ThreeColumnsVue,
    'tool-dropdown': ToolDropdownVue,
    'image-pad': ImagePadVue,
    'graphic-pad': GraphicSetVue
  },
  data () {
    return {
      startDate: '',
      endDate: '',
      type: {
        title: '选择图片类型',
        value: ''
      },
      typeList: [
        {
          title: '课堂图片 | 精选',
          value: 'feedback_image_like_list'
        },
        {
          title: '群组动态 | 全部',
          value: 'share_graphic_all_list'
        },
        {
          title: '群组动态 | 精选',
          value: 'share_graphic_like_list'
        }
      ],
      feedbackImgList: [],
      shareGraphicList: []
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
    // show or hide feedback img list or share graphic list
    isGraph () {
      if (this.type.value === 'share_graphic_all_list' || this.type.value === 'share_graphic_like_list') {
        return true
      } else {
        return false
      }
    }
  },
  methods: {
    showToast (title, content, variant) {
      this.$bvToast.toast(
        content,
        {
          title: title,
          solid: true,
          variant: variant
        }
      )
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
      this.showToast(
        '正在搜索',
        `搜索从 ${start} 至 ${end} 的 ${this.type.title}`,
        'info'
      )
      Axios
        .get(
          `flourish/${this.type.value}/${end}T23:59:59/${start}T00:00:00/`
        )
        .then(
          res => {
            if (this.type.value === 'feedback_image_all_list' || this.type.value === 'feedback_image_like_list') {
              this.feedbackImgList = res.data
            } else {
              this.shareGraphicList = res.data
            }
            this.showToast(
              '搜索成功',
              `搜索结果为 ${start} 至 ${end} 的 ${this.type.title}, 共搜索到${res.data.length}条结果`,
              'success'
            )
          }
        )
        .catch(
          err => {
            if (String(err).indexOf('401')) {
              this.showToast(
                '搜索失败，正在尝试重新获取验证，或者选择手动刷新',
                `尝试搜索 ${start} 至 ${end} 的 ${this.type.title}`,
                'warning')
              this.autoLogin()
              this.getCollect(start, end)
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
</style>
