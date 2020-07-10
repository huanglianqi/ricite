<template>
  <div
    id="pictureManage">
    <three-columns aria-label="head toolbar"
      firstColumnTitle="类型"
      secondColumnTitle="起于"
      thirdColumnTitle="止于">
      <template v-slot:firstColumn>
        <tool-dropdown
          variant="outline-success"
          iconUp="collection-play-fill"
          iconDown="collection-fill"
          :title="type.title"
          :value="type.value"
          firstItemTitle="群组动态"
          firstItemValue="2"
          :itemList="typeList"
          :selectItemFunc="selectType"></tool-dropdown></template>
      <template v-slot:secondColumn>
        <b-button
          variant="outline-info"
          block
          class="mb-3"
          v-on:click="onConfirmStartDate">
          <div
            v-show="!confirmStartDate">
            请确定开始日期
          </div>
          <div
            v-show="confirmStartDate">
            <div
              v-if="startDate === ''">
              请选择结束日期
            </div>
            {{startDate}}
          </div></b-button>
        <div
          v-show="!confirmStartDate">
          <b-calendar
            v-model="startDate"
            v-bind="calendarFormat"
            selected-variant="success"
            today-variant="info"
            block></b-calendar></div></template>
      <template v-slot:thirdColumn>
        <b-button
          variant="outline-info"
          block
          class="mb-3"
          v-on:click="onConfirmEndDate">
          <div
            v-show="!confirmEndDate">
            请确定结束日期
          </div>
          <div
            v-show="confirmEndDate">
            <div
              v-if="endDate === ''">
              请选择结束日期
            </div>
            {{endDate}}
          </div></b-button>
        <div
          v-show="!confirmEndDate">
          <b-calendar
            v-model="endDate"
            v-bind="calendarFormat"
            selected-variant="success"
            today-variant="info"
            block></b-calendar></div></template></three-columns>
    <three-blocks aria-label="list">
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
          <b-icon
            :icon="isLike(pic)"
            variant="danger"
            v-on:click="likeIt(pic)"></b-icon>
          <b-button
            size="sm"
            class="float-right"
            variant="outline-success"
            pill
            v-on:click="downloadPic(pic)">
            <b-icon
              icon="download"
              font-scale="0.95"
              shift-v="1.75"></b-icon></b-button></b-card-text></b-card></three-blocks>
    <tool-modal aria-label="detail"
      id="detail"
      :title="detail.teacher.real_name">
      <b-img
        center
        fluid-grow
        :src="detail.pic_url"
        :alt="detail.pic_url"></b-img></tool-modal>
  </div>
</template>

<script>
import ThreeColumnsVue from './ThreeColumns.vue'
import ToolDropdownVue from './ToolDropdown.vue'
import Axios from 'axios'
import ThreeBlocksVue from './ThreeBlocks.vue'
import ToolModalVue from './ToolModal.vue'
// import {saveAs} from 'file-saver'

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
      confirmStartDate: true,
      confirmEndDate: true,
      startDate: '',
      endDate: '',
      calendarFormat: {
        weekdayHeaderFormat: 'narrow',
        labelPrevDecade: '过去十年',
        labelPrevYear: '上一年',
        labelPrevMonth: '上个月',
        labelCurrentMonth: '当前月份',
        labelNextMonth: '下个月',
        labelNextYear: '明年',
        labelNextDecade: '下一个十年',
        labelToday: '今天',
        labelSelected: '选定日期',
        labelNoDateSelected: '未选择日期',
        labelCalendar: '日历',
        labelNav: '日历导航',
        labelHelp: '使用光标键浏览日期',
        locale: 'zh'
      },
      type: {
        title: '群组动态',
        value: '1'
      },
      typeList: [
        {
          title: '课时反馈',
          value: '2'
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
        this.updateLike(pic.id, false)
      } else {
        this.updateLike(pic.id, true)
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
    selectType (title, value) {
      this.type.value = value
      this.type.title = title
    },
    onConfirmStartDate () {
      this.confirmStartDate = !this.confirmStartDate
      this.collectPic()
    },
    onConfirmEndDate () {
      this.confirmEndDate = !this.confirmEndDate
      this.collectPic()
    },
    collectPic () {
      if (this.confirmEndDate === true && this.confirmStartDate === true && this.startDate !== '' && this.endDate !== '') {
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
          `flourish/feedback_pic_collect/${end}T23:59:59/${start}T00:00:00/`
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
    getDetail (pic) {
      this.detail = pic
    },
    downloadPic (pic) {
      let image = new Image()
      image.setAttribute('crossOrigin', 'anonymous')
      image.src = pic.pic_url
      image.onload = () => {
        let canvas = document.createElement('canvas')
        canvas.width = image.width
        canvas.height = image.height
        let ctx = canvas.getContext('2d')
        ctx.drawImage(image, 0, 0, image.width, image.height)
        canvas.toBlob((blob) => {
          let url = URL.createObjectURL(blob)
          this.download(url)
          // 用完释放URL对象
          URL.revokeObjectURL(url)
        })
      }
      /*
      let image = new Image()
      image.setAttribute('crossOrigin', 'anonymous')
      image.src = pic.pic_url
      image.onload = () => {
        let canvas = document.createElement('canvas')
        canvas.width = image.width
        canvas.height = image.height
        let ctx = canvas.getContext('2d')
        ctx.drawImage(image, 0, 0, image.width, image.height)
        let ext = image.src.substring(image.src.lastIndexOf('.') + 1).toLowerCase()
        let dataURL = canvas.toDataURL('image/' + ext)
        this.download(dataURL)
      }
      */
      /*
      var canvas = document.createElement('canvas')
      var context = canvas.getContext('2d')

      var img = new Image()
      img.crossOrigin = 'anonymous'
      img.setAttribute('crossOrigin', 'anonymous')
      img.onload = function () {
        context.drawImage(this, 0, 0)
        context.getImageData(0, 0, this.width, this.height)
      }
      img.src = pic.pic_url
      */
      /*
      Axios
        .get(
          pic.pic_url,
          {
            responseType: 'blob'
          }
        )
        .then(
          res => {
            let blob = res.data
            let url = URL.createObjectURL(blob)
            this.download(url)
            URL.revokeObjectURL(url, pic)
          }
        )
    */
    },
    download (url, pic) {
      const link = document.createElement('a')
      link.href = url
      link.setAttribute('download', `${pic.teacher.real_name}.jpg`)
      document.body.append(link)
      link.click()
    },
    /*
    downloadPic (pic) {
      let src = pic.pic_url
      var canvas = document.createElement('canvas')
      var img = document.createElement('img')
      img.onload = function (e) {
        canvas.width = img.width
        canvas.height = img.height
        var context = canvas.getContext('2d')
        context.drawImage(img, 0, 0, img.width, img.height)
        canvas.getContext('2d').drawImage(img, 0, 0, img.width, img.height)
        canvas.toBlob(
          (blob) => {
            let link = document.createElement('a')
            link.href = window.URL.createObjectURL(blob)
            link.download = pic.teacher.real_name
            link.click()
          },
          'image/jpeg'
        )
      }
    },
    */
    // downloadPic (pic) {
    //   let image = new Image()
    //   let that = this
    //   image.crossOrigin = ''
    //   image.src = pic.pic_url
    //   image.src = pic.pic_url + '?time' + new Date().indexOf()
    //   image.setAttribute('crossOrigin', 'anonymous')
    //   image.onload = function () {
    //     let base64 = that.getBase64Image(image)
    //     let img = that.convertBase64UrlToBlob(base64)
    //     that.changeKoubeiImg(1, img)
    //   }
    // },
    /*
    downloadPic (pic) {
      Axios
        .get(
          `${pic.pic_url}`
        )
        .then(
          res => {
            this.forceFileDownload(res, pic)
          }
        )
        .catch(
          err => {
            console.log(err)
          }
        )
    },
    forceFileDownload (res, pic) {
      const url = window.URL.createObjectURL(new Blob([res.data]))
      const link = document.createElement('a')
      link.href = url
      link.setAttribute('download', `${pic.teacher.real_name}.jpg`)
      document.body.append(link)
      link.click()
    },
    */
    /*
    downloadPic (pic) {
      var canvas = document.createElement('canvas')
      var context = canvas.getContext('2d')

      var img = new Image()
      img.crossOrigin = ''
      img.onload = function () {
          context.drawImage(this, 0, 0)
          context.getImageData(0, 0, this.width, this.height)
      }
      img.src = pic.pic_url
    },
    downloadPic (pic) {
      let that = this
      let image = new Image()
      image.src = pic.pic_url
      image.crossOrigin = 'anonymous'
      image.onload = function () {
        let base64 = that.getBase64Image(image)
        that.talkInfo.imageUrls.push(base64)
        that.networkImg = ''
      }
    },
    getBase64Image (img) {
      let canvas = document.createElement('canvas')
      canvas.width = img.width
      canvas.height = img.height
      let ctx = canvas.getContext('2d')
      ctx.drawImage(img, 0, 0, img.width, img.height)
      let dataURL = canvas.toDataURL('image/jpeg')
      return dataURL
    },
    downloadPic (pic) {
      saveAs(
        pic.pic_url,
        `${pic.teacher.real_name}.jpg`
      )
    },
    */
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
