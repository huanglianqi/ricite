<template>
  <div
    id="imagePad">
    <no-result
      :show="list.length===0"
      :icon="'images'"></no-result>
    <three-blocks aria-label="picture set">
      <b-card
        v-for="item in list"
        :key="item.id"
        border-variant="white"
        bg-variant="light"
        rounded>
        <div
          v-on:click="getDetail(item)"
          class="rounded"
          style="max-width: 450px; overflow-x: hidden">
          <b-img-lazy
            class=" align-self-center"
            style="overflow-x: hidden;"
            rounded
            v-b-modal.detail
            :src="item.pic_url"
            height="300"></b-img-lazy></div>
        <b-container
          class="mt-3">
          <b-row>
            <b-col>
              <b-button
                class="shadow border-white border-0"
                block
                variant="outline-danger"
                v-on:click="update(item)">
                <b-icon
                  :icon="updateIcon(item.like)"></b-icon></b-button></b-col>
            <b-col>
              <b-button
                class="shadow border-white border-0"
                block
                variant="outline-success"
                v-on:click="download(item)">
                <b-icon
                  icon="cloud-download"></b-icon></b-button></b-col>
             <b-col>
              <b-button
                v-b-modal.detail
                class="shadow border-white border-0"
                block
                variant="outline-info"
                v-on:click="getDetail(item)">
                <b-icon
                  icon="arrows-angle-expand"></b-icon></b-button></b-col></b-row></b-container></b-card></three-blocks>
    <modal-model aria-label="picture detail"
      id='detail'
      body-bg-variant="light"
      :hide-footer="true">
      <b-img
        class="shadow-lg"
        rounded
        block
        fluid-grow
        :src="detail.pic_url"
        alt="图片丢失"></b-img>
        <div
          class="shadow p-3 rounded bg-white mt-3">
          <div>
            <small
              class="text-muted">图片提供者</small></div>
            <head-img-kits
              :tow-line="false">
              <template
                v-slot:button>
                <head-img-btn
                  v-b-modal.imagePadHeadImgInfoModal
                  :src="detail.teacher.head_img"
                  :size="'1.5rem'"></head-img-btn></template>
              <template
                v-slot:centerText>
                {{detail.teacher.name}}</template></head-img-kits>
            <head-img-info
              :id="'imagePadHeadImgInfoModal'"
              :info="detail.teacher.infoForms"></head-img-info></div>
        <div
          class="shadow p-3 rounded bg-white mt-3">
          <div>
            <small
              class="text-muted">上传时间</small></div>
            <b-icon
              icon="clock-fill"></b-icon>
            {{detail.feedback_form.create_time}}</div>
        <div
          class="shadow p-3 rounded bg-white mt-3">
          <div>
            <small
              class="text-muted">所属课程包</small></div>
            <b-icon
              icon="tag-fill"></b-icon>
            {{detail.user_course.tag_name}}</div>
        <div
          class="shadow p-3 rounded bg-white mt-3">
          <div>
            <small
              class="text-muted">真实姓名</small></div>
            <b-icon
              icon="person-fill"></b-icon>
            {{detail.teacher.real_name}}</div>
        <div
          class="shadow p-3 rounded bg-white mt-3">
          <div>
            <small
              class="text-muted">联系方式</small></div>
            <b-icon
              icon="telephone-fill"></b-icon>
            {{detail.teacher.phone}}</div>
        <div
          class="shadow p-3 rounded bg-white mt-3">
          <div>
            <small
              class="text-muted">所属学校</small></div>
            <b-icon
              icon="geo"></b-icon>
            {{searchSchool(detail.teacher.infoForms)}}</div>
        <b-container
          class="mt-3">
          <b-row>
            <b-col>
              <b-button
                class="shadow border-white border-0"
                block
                variant="outline-danger"
                v-on:click="updateLike(detail.id, detail.like)">
                <b-icon
                  :icon="updateIcon(detail.like)"></b-icon></b-button></b-col>
            <b-col>
              <b-button
                class="shadow border-white border-0"
                block
                variant="outline-success"
                v-on:click="download(detail)">
                <b-icon
                  icon="cloud-download"></b-icon></b-button></b-col>
            <b-col>
              <b-button
                block
                variant="outline-info"
                v-on:click="$bvModal.hide('detail')"
                class="shadow border-white border-0">
                <b-icon
                  icon="arrows-angle-contract"></b-icon></b-button></b-col></b-row></b-container></modal-model>
  </div>
</template>

<script>
import ModalModelVue from './parts/ModalModel.vue'
import ThreeBlocksVue from './structure/ThreeBlocks.vue'
import Axios from 'axios'
import HeadImgKitsVue from './headImg/HeadImgKits.vue'
import HeadImgBtnVue from './headImg/HeadImgBtn.vue'
import HeadImgInfoVue from './headImg/HeadImgInfo.vue'
import noResultVue from './noResult.vue'

export default {
  name: 'imagePad',
  components: {
    'modal-model': ModalModelVue,
    'three-blocks': ThreeBlocksVue,
    'head-img-kits': HeadImgKitsVue,
    'head-img-btn': HeadImgBtnVue,
    'head-img-info': HeadImgInfoVue,
    'no-result': noResultVue
  },
  data () {
    return {
      detail: {
        teacher: {
          real_name: '',
          name: '',
          head_img: ''
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
  props: {
    list: {
      type: Array,
      required: false
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
    getDetail (item) {
      this.detail = item
    },
    update (item) {
      this.getDetail(item)
      this.updateLike(item.id, item.like)
    },
    download (item) {
      this.downloadPic(item)
      if (!item.like) {
        this.getDetail(item)
        this.updateLike(item.id, false)
      }
    },
    updateLike (id, state) {
      Axios
        .patch(
          `flourish/feedback_pic_like_update/${id}`,
          {
            like: !state
          }
        )
        .then(
          res => {
            this.detail.like = res.data.like
          }
        )
        .catch(
          err => {
            if (String(err).indexOf('401')) {
              this.autoLogin()
              this.updateLike(id, state)
            }
          }
        )
    },
    updateIcon (state) {
      if (state) {
        return 'heart-fill'
      } else {
        return 'heart'
      }
    },
    downloadPic (pic) {
      var fileName = `${pic.feedback_form.create_time.split('T')[0]}-${this.searchSchool(pic.teacher.infoForms)}-心灵魔法学院-${pic.teacher.real_name}-${pic.user_course.tag_name}`
      this.showToast(
        '收集图片资源',
        `${fileName}`,
        'info'
      )
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
          this.onDownloadPic(url, fileName)
          URL.revokeObjectURL(url)
        })
        this.showToast(
          '图片准备下载',
          `${fileName}`,
          'success'
        )
      }
    },
    onDownloadPic (url, fileName) {
      const link = document.createElement('a')
      link.href = url
      link.setAttribute('download', `${fileName}.jpg`)
      document.body.append(link)
      link.click()
      document.body.removeChild(link)
    },
    // school form id is 9
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
