<template>
  <div
    id="pictureDetailModal">
    <modal-model
      :id="id">
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
                    icon="cloud-download"></b-icon></b-button></b-col></b-row></b-container></div></modal-model></div>
</template>

<script>
import ModalModelVue from './ModalModel.vue'

export default {
  name: 'pictureDetailModal',
  components: {
    'modal-model': ModalModelVue
  },
  props: {
    id: {
      type: String,
      required: true
    },
    detail: {
      type: Object,
      required: true
    }
  }
}
</script>