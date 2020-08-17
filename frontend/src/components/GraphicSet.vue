<template>
  <div
    id="graphicPad">
    <three-blocks>
      <b-card
        v-for="item in list"
        :key="item.id"
        border-variant="white"
        bg-variant="light"
        rounded>
        <div>
          <head-img-kits
            :two-line="true">
            <template
              v-slot:button>
              <div
                @click="getPersonInfoData(item.teacher.infoForms)">
                <head-img-btn
                  v-b-modal.graphicSetPersonInfoModal
                  :src="item.teacher.head_img"
                  :size="'2.5rem'"></head-img-btn></div></template>
            <template
              v-slot:topText>
              {{item.user_name}}</template>
            <template
              v-slot:bottomText>
              {{item.create_time}}</template></head-img-kits>
          <p
            class="text-left ml-5">
            <b-badge
              class="mr-1 px-2"
              href="#"
              variant="danger">
              <b-icon
                icon="hand-thumbs-up"></b-icon>
                {{item.shareLikes.length}}</b-badge>
            <b-badge
              class="mr-1 px-2"
              href="#"
              variant="warning">
              <b-icon
                icon="chat"></b-icon>
                {{item.shareComments.length}}</b-badge>
            <b-badge
              class="mr-1 px-2"
              variant="info">
              <b-icon
                icon="image"></b-icon>
                {{item.sharePics.length}}</b-badge></p>
          <p
            v-if="item.content!==''"
            id="textarea"
            class="ml-5 text-justify text-black-75 text-left w-75"
            style="height: 100px;">
            {{item.content}}</p>
          <div
            v-else
            class="font-weight-bold"
            style="height: 100px;">
            <b-icon
              font-scale="3"
              icon="card-text"></b-icon>
            No Text</div></div>
          <div
            v-if="item.sharePics.length>0"
            style="height: 275px;"
            id="image"
            class="d-inline-flex rounded w-100 shadow-sm p-2 bg-white">
            <div
              v-for="pic in item.sharePics"
              :key="pic"
              @click="getSharePicDetail(pic, item)">
              <b-img-lazy
                v-b-modal.graphicSetSharePicDetailModal
                class="m-1"
                style="max-height: 250px;"
                :src="pic"
                rounded></b-img-lazy></div></div>
          <div
            v-else
            style="height: 250px;">
            <b-icon
              font-scale="5"
              icon="image"></b-icon>
            <p
              class="font-weight-bold">No Picture</p></div>
          <b-container
            class="mt-2">
            <b-row>
              <b-col>
                <b-button
                  @click="updateShareLike(item, item.like)"
                  block
                  variant="outline-danger"
                  size="sm"
                  class="border-0 shadow">
                  <b-icon
                    :icon="updateIcon(item.like)"></b-icon></b-button></b-col>
              <b-col>
                <b-button
                  @click="downloadShare(item)"
                  block
                  variant="outline-success"
                  size="sm"
                  class="border-0 shadow">
                  <b-icon
                    icon="cloud-download">
                    {{item.shareComments.length}}</b-icon></b-button></b-col></b-row></b-container></b-card></three-blocks>
    <head-img-info
      :id="'graphicSetPersonInfoModal'"
      :info="graphicSetPersonInfoData"></head-img-info>
    <modal-model
      :id="'graphicSetSharePicDetailModal'"
      :hide-footer="true">
      <b-img
        class="shadow-lg"
        rounded
        block
        fluid-grow
        :src="graphicSetSharePicDetail"></b-img>
      <b-container
        class="mt-3">
        <b-row>
          <b-col>
            <b-button
              class="shadow border-white border-0"
              block
              variant="outline-success"
              v-on:click="downloadPic(graphicSetSharePicDetail, graphicSetShareDetail)">
              <b-icon
                icon="cloud-download"></b-icon></b-button></b-col>
          <b-col>
            <b-button
              block
              variant="outline-info"
              v-on:click="$bvModal.hide('graphicSetSharePicDetailModal')"
              class="shadow border-white border-0">
              <b-icon
                icon="arrows-angle-contract"></b-icon></b-button></b-col></b-row></b-container></modal-model>
    </div>
</template>

<script>
import HeadImgInfoVue from './headImg/HeadImgInfo.vue'
import HeadImgBtnVue from './headImg/HeadImgBtn.vue'
import HeadImgKitsVue from './headImg/HeadImgKits.vue'
import ThreeBlocksVue from './ThreeBlocks.vue'
import ModalModelVue from './ModalModel.vue'
import Axios from 'axios'
// import JSZip from 'jszip'
import {saveAs} from 'file-saver'

export default {
  name: 'graphicPad',
  components: {
    'head-img-btn': HeadImgBtnVue,
    'head-img-info': HeadImgInfoVue,
    'head-img-kits': HeadImgKitsVue,
    'three-blocks': ThreeBlocksVue,
    'modal-model': ModalModelVue
  },
  props: {
    list: {
      type: Array,
      required: true
    }
  },
  data () {
    return {
      graphicSetPersonInfoData: [
        {
          field_name: '',
          field_value: '',
          field_id: ''
        }
      ],
      graphicSetSharePicDetail: '',
      graphicSetShareDetail: {}
    }
  },
  methods: {
    getPersonInfoData (data) {
      this.graphicSetPersonInfoData = data
    },
    getSharePicDetail (pic, info) {
      this.graphicSetSharePicDetail = pic
      this.graphicSetShareDetail = info
    },
    downloadPic (url, info) {
      this.showToast(
        '图片准备下载',
        `${info.teacher.real_name}，${info.create_time.split('T')[0]}，${this.searchSchool(info.teacher.infoForms)}`,
        'info'
      )
      // Translate pic_url into 'download/' format for proxy request.
      let image = new Image()
      let src = url.replace('https://www.rici.org.cn/', 'download/')
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
          this.onDownloadPic(url, info)
          URL.revokeObjectURL(url)
        })
        this.showToast(
          '图片下载成功',
          `${info.teacher.real_name}，${info.create_time.split('T')[0]}，${this.searchSchool(info.teacher.infoForms)}`,
          'success'
        )
      }
    },
    onDownloadPic (url, info) {
      // human readable time format is 'yyyy-mm--dd'
      let time = info.create_time.split('T')[0]
      // Data 'school' exist in info forms
      let school = this.searchSchool(info.teacher.infoForms)
      const link = document.createElement('a')
      link.href = url
      link.setAttribute('download', `${time}-${school}-心灵魔法学院-${info.teacher.real_name}.jpg`)
      document.body.append(link)
      link.click()
      document.body.removeChild(link)
    },
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
    searchSchool (forms) {
      if (typeof forms === 'object') {
        for (let i = 0; i < forms.length; i++) {
          if (forms[i].field_id === '9') {
            return forms[i].field_value
          }
        }
      } else {
        return ''
      }
    },
    updateShareLike (detail, state) {
      this.graphicSetShareDetail = detail
      Axios
        .patch(
          `flourish/share_update/${detail.id}`,
          {
            like: !state
          }
        )
        .then(
          res => {
            this.graphicSetShareDetail.like = res.data.like
          }
        )
        .catch(
          err => {
            if (String(err).indexOf('401')) {
              this.autoLogin()
              this.updateShareLike(detail)
            }
          }
        )
    },
    downloadShare (detail) {
      var filename = `${this.searchSchool(detail.teacher.infoForms)}-心灵魔法学院-${detail.teacher.real_name}-${detail.create_time.split('T')[0]}`
      this.showToast(
        '正在收集群组动态压缩包资源',
        filename,
        'info')

      if (detail.like === false) {
        this.updateShareLike(detail, detail.like)
      }

      // var zip = new JSZip()
      // zip.file(`${filename}-content.txt`, `${detail.content}`)
      // var imageFolder = zip.folder('images')

      saveAs(
        new Blob(
          [`${detail.content}`],
          {type: 'text/plain;charset=utf-8'}),
        `${filename}.txt`)

      for (let i = 0; i < detail.sharePics.length; i++) {
        // this.downloadPic(detail.sharePics[i], detail)
        // let src = detail.sharePics[i].replace('https://www.rici.org.cn/', 'download/')
        // Axios
        //   .get(src, {responseType: 'blob'})
        //   .then(res => {
        //     console.log(res)
        //     imageFolder.file(
        //       `${filename}-${i + 1}.jpg`,
        //       res.data)
        //   })
        //   .catch(err => {
        //     console.log(err)
        //   })
        let image = new Image()
        let src = detail.sharePics[i].replace('https//:www.rici.org.cn/', 'download/')
        image.setAttribute('crossOrigin', 'anonymous')
        image.src = src
        image.onload = () => {
          let canvas = document.createElement('canvas')
          canvas.width = image.width
          canvas.height = image.height
          let ctx = canvas.getContext('2d')
          ctx.drawImage(image, 0, 0, image.width, image.height)
          canvas.toBlob(function (blob) {
            saveAs(blob, `${filename}-${i + 1}.jpg`)
          })
          // let blob = canvas.toDataURL()
          // let blobArr = blob.split(',')
          // imageFolder.file(`${filename}-${i + 1}.txt`, blobArr[1])
          // zip.file(`${filename}-content-${i + 1}.txt`, `${detail.content}`)
        }
      }
      // zip
      //   .generateAsync({type: 'blob'})
      //   .then(content => {
      //     saveAs(content, `${filename}.zip`)
      //   })

      // saveAs(`${detail.content}`, `${filename}-content.txt`)
      // for (let i = 0; i< detail.sharePics.length; i++) {
      //   this.downloadPic(detail.sharePics[i], detail)
      // }

      // var zip = new JSZip()
      // zip.file('群组动态分享文字.docx', `${detail.content}`)
      // var imageFolder = zip.folder('群组动态分享图片')
      // for (let i = 0; i < detail.sharePics.length; i++) {
      //   let image = new Image()
      //   var src = detail.sharePics[i].replace('https://www.rici.org.cn/', 'download/')
      //   image.setAttribute('crossOrgin', 'anonymous')
      //   image.src = src
      //   image.onload = () => {
      //     let canvas = document.createElement('canvas')
      //     canvas.width = image.width
      //     canvas.height = image.height
      //     let ctx = canvas.getContext('2d')
      //     ctx.drawImage(image, 0, 0, image.width, image.height)
      //     canvas.toBlob((blob) => {
      //       imageFolder.file(
      //         `${filename}-${i + 1}.jpg`,
      //         blob,
      //         {type: 'blob'})
      //     })
      //   }
      // }
      // zip
      //   .generateAsync({type: 'blob'})
      //   .then(
      //     content => {
      //       saveAs(content, `${filename}.zip`)
      //     })

      this.showToast(
        '群组动态压缩包准备下载',
        filename,
        'success')
    },
    updateIcon (state) {
      if (state) {
        return 'heart-fill'
      } else {
        return 'heart'
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
#textarea {
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
  overflow: scroll;
}
#image {
  overflow-x: scroll;
}
</style>
