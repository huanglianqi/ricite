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
    <three-blocks aria-label="PicList">
      <b-card
        v-for="pic in picList"
        :key="pic.id"
        border-variant="white">
        <div
          v-on:click="getDetail(pic)">
          <b-card-img-lazy aria-label="feedback pic"
            :src="pic.pic_url"
            alt="Oops 服务器丢掉了该图片"
            top
            v-b-modal.detail
            blank-width="300"
            black-height="200"></b-card-img-lazy></div>
        <b-card-text
          class="p-2 font-weight-bolder text-left text-black-75 align-text-bottom">
          <b-img-lazy aria-label="head pic"
            :src="pic.teacher.head_img"
            :alt="pic.teacher.head_img"
            v-bind="headImgFormat"
            rounded="circle"
            blank></b-img-lazy>
          {{pic.teacher.real_name}}
          <b-button
            size="sm"
            pill
            variant="white"
            v-on:click="likeIt(pic)">
            <b-icon
              variant="danger"
              shift-v="1.75"
              font-scale="1.5"
              :icon="isLike(pic)"></b-icon></b-button>
          <b-button
            size="sm"
            class="float-right"
            variant="white"
            pill
            v-on:click="downloadPic(pic)">
            <b-icon
              icon="download"
              font-scale="1.5"
              shift-v="1.75"
              variant="success"></b-icon></b-button></b-card-text></b-card></three-blocks>
    <b-modal aria-label="detail"
      id="detail"
      size="xl"
      hide-header
      centered
      ok-variant="outline-success"
      ok-only
      ok-title="关闭"
      body-bg-variant="light">
      <b-img
        block
        center
        fluid-grow
        :src="detail.pic_url"
        :alt="detail.pic_url"></b-img></b-modal>
  </div>
</template>

<script>
import ThreeColumnsVue from './ThreeColumns.vue'
import ToolDropdownVue from './ToolDropdown.vue'
import Axios from 'axios'
import ThreeBlocksVue from './ThreeBlocks.vue'
import ToolModalVue from './ToolModal.vue'

export default {
  name: 'pictureManage',
  components: {
    'three-columns': ThreeColumnsVue,
    'tool-dropdown': ToolDropdownVue,
    'three-blocks': ThreeBlocksVue,
    'tool-modal': ToolModalVue
  },
  data () {
    return {
      headImgFormat: {
        width: 25,
        height: 25,
        class: 'ml-1 mr-2 mb-1 mt-0',
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
      detail: {
        teacher: {
          real_name: ''
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
    }
  },
  methods: {
    /*
     * Heart-fill means we like it,
     * when pic was choised by us.
     * Heart means we don't like it,
     * when pic isn't choised by us.
    */
    isLike (pic) {
      if (pic.like) {
        return 'heart-fill'
      } else {
        return 'heart'
      }
    },
    likeIt (pic) {
      if (pic.like) {
        // modify data remotely
        this.updateLike(pic.id, false)
        // modify data locally
        pic.like = false
      } else {
        // modify data remotely
        this.updateLike(pic.id, true)
        // modify data locally
        pic.like = true
      }
    },
    updateLike (id, bool) {
      Axios
        .patch(
          `flourish/feedback_pic_like_update/${id}`,
          {
            like: bool
          }
        )
        .catch(
          err => {
            console.log(err)
          }
        )
    },
    checkDateFormat (date) {
      if (date.length === 10) {
        if (date.slice(0, 4) >= 2018 && date[5] === '-' && date[8] === '-' && date[6] >= 0 && date[6] <= 1 && date[7] <= 9 && date[7] >= 0 && date[9] >= 0 && date[9] <= 3 && date[10] >= 0 && date[10] <= 9) {
          this.collectPic()
        }
      }
    },
    selectType (title, value) {
      this.type.value = value
      this.type.title = title
      this.collectPic()
    },
    collectPic () {
      if (this.startDate !== '' && this.endDate !== '' && this.type.value !== '') {
        if (this.startDate > this.endDate) {
          this.getPicCollect(this.endDate, this.startDate)
        } else {
          this.getPicCollect(this.startDate, this.endDate)
        }
      }
    },
    getPicCollect (start, end) {
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
              this.getPicCollect(start, end)
            }
          }
        )
    },
    // Zoom up the picture
    getDetail (pic) {
      this.detail = pic
    },
    /*
     * Download image one by one, HD
    */
    downloadPic (pic) {
      // Translate pic_url into 'download/' format for proxy request.
      let image = new Image()
      let src = pic.pic_url.replace('https://www.rici.org.cn/', 'download/')
      image.setAttribute('crossOrigin', 'anonymous')
      image.src = src
      image.onload = () => {
        let canvas = document.createElement('canvas')
        canvas.width = image.width
        canvas.height = image.height
        let ctx = canvas.getContext('2d')
        ctx.drawImage(image, 0, 0, image.width, image.height)
        canvas.toBlob((blob) => {
          let url = URL.createObjectURL(blob)
          // Click on simulate download link
          this.onDownloadPic(url, pic)
          URL.revokeObjectURL(url)
        })
        // auto add 'like' list
        this.likeIt(pic)
      }
    },
    onDownloadPic (url, pic) {
      // human readable time format is 'yyyy-mm--dd'
      let time = pic.feedback_form.create_time.split('T')[0]
      // Data 'school' exist in info forms
      let school = this.searchSchool(pic.teacher.infoForms)
      const link = document.createElement('a')
      link.href = url
      link.setAttribute('download', `${time}-${school}-心灵魔法学院-${pic.teacher.real_name}-${pic.user_course.tag_name}.jpg`)
      document.body.append(link)
      link.click()
      document.body.removeChild(link)
    },
    /*
     * search school string in info form
     * and its field id is 9
    */
    searchSchool (forms) {
      // info form field id 9 is school
      for (let i = 0; i < forms.length; i++) {
        if (forms[i].field_id === '9') {
          return forms[i].field_value
        }
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
