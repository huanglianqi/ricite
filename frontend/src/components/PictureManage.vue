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
    <three-blocks aria-label="PicList"
      v-show="!isGraph">
      <b-card
        v-for="pic in picList"
        :key="pic.id"
        border-variant="white"
        :img-src="pic.pic_url"
        overlay>
        <b-container
          class="mt-3">
            <b-row
              class="mb-3">
              <b-col>
                <b-button
                  block
                  variant="outline-danger"
                  v-on:click="likeIt(pic)">
                  <b-icon
                    :icon="isLike(pic)"></b-icon></b-button></b-col>
              <b-col>
                <b-button
                  block
                  variant="outline-success"
                  v-on:click="downloadPic(pic)">
                  <b-icon
                    icon="cloud-download"></b-icon></b-button></b-col></b-row>
            <b-row
              class="mb-3 px-3">
              <b-button
                block
                v-b-modal.detail
                v-on:click="getDetail(pic)"
                variant="outline-info">
                详情</b-button></b-row></b-container></b-card></three-blocks>
    <three-blocks aria-label="shareList"
      v-show="isGraph">
      <b-carousel
        v-for="share in shareList"
        :key="share.moment"
        fade
        indicators
        controls
        img-width="1024"
        img-height="480">
        <b-carousel-slide
          v-for="pic in share.sharePics"
          :key="pic.url"
          :img-src="pic.url"></b-carousel-slide></b-carousel>
    </three-blocks>
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
        fluid-grow
        :src="detail.pic_url"
        alt="图片丢失"></b-img>
        <div
          class="p-2 font-weight-bold text-left text-black-75 align-text-bottom">
          <p>
            <b-img-lazy aria-label="head pic"
              :src="detail.teacher.head_img"
              v-bind="headImgFormat"
              rounded
              blank></b-img-lazy>
            {{detail.teacher.name}}</p>
          <p>
            <b-icon
            icon="calendar-event-fill"></b-icon>
            {{detail.feedback_form.create_time}}</p>
          <p>
            <b-icon
            icon="person-fill"></b-icon>
            {{detail.teacher.real_name}}</p>
          <p>
            <b-icon
              icon="tag-fill"></b-icon>
            {{detail.user_course.tag_name}}</p>
          <p>
            {{detail.is_reapply}}</p>
          <p>
            <b-icon
              icon="telephone-fill"></b-icon>
            {{detail.teacher.phone}}</p>
          <b-container
            class="mt-3">
            <b-row>
              <b-col>
                <b-button
                  block
                  variant="outline-danger"
                  v-on:click="likeIt(detail)">
                  <b-icon
                    :icon="isLike(detail)"></b-icon></b-button></b-col>
              <b-col>
                <b-button
                  block
                  variant="outline-success"
                  v-on:click="downloadPic(detail)">
                  <b-icon
                    icon="cloud-download"></b-icon></b-button></b-col></b-row></b-container></div></b-modal>
  </div>
</template>

<script>
import ThreeColumnsVue from './ThreeColumns.vue'
import ToolDropdownVue from './ToolDropdown.vue'
import Axios from 'axios'
import ThreeBlocksVue from './ThreeBlocks.vue'

export default {
  name: 'pictureManage',
  components: {
    'three-columns': ThreeColumnsVue,
    'tool-dropdown': ToolDropdownVue,
    'three-blocks': ThreeBlocksVue
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
