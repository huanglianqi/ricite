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
                  v-b-modal.graphicPadPersonInfoModal
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
            id="textarea"
            class="ml-5 text-justify text-black-75 text-left w-75"
            style="height: 100px;">
            {{item.content}}</p></div>
          <div
            v-if="item.sharePics.length>=0"
            style="height: 250px;"
            id="image"
            class="d-inline-flex rounded w-100 shadow-sm p-2 bg-white">
            <b-img-lazy
              v-for="pic in item.sharePics"
              :key="pic"
              class="m-1"
              style="max-height: 250px;"
              :src="pic"
              rounded></b-img-lazy></div>
          <b-container
            class="mt-2">
            <b-row>
              <b-col>
                <b-button
                  block
                  variant="outline-danger"
                  size="sm"
                  class="border-0 shadow">
                  <b-icon
                    icon="heart"></b-icon></b-button></b-col>
              <b-col>
                <b-button
                  block
                  variant="outline-success"
                  size="sm"
                  class="border-0 shadow">
                  <b-icon
                    icon="cloud-download">
                    {{item.shareComments.length}}</b-icon></b-button></b-col></b-row></b-container></b-card></three-blocks>
    <head-img-info
      :id="'graphicPadPersonInfoModal'"
      :info="graphicPadPersonInfoData"></head-img-info>
    </div>
</template>

<script>
import HeadImgInfoVue from './headImg/HeadImgInfo.vue'
import HeadImgBtnVue from './headImg/HeadImgBtn.vue'
import HeadImgKitsVue from './headImg/HeadImgKits.vue'
import ThreeBlocksVue from './ThreeBlocks.vue'

export default {
  name: 'graphicPad',
  components: {
    'head-img-btn': HeadImgBtnVue,
    'head-img-info': HeadImgInfoVue,
    'head-img-kits': HeadImgKitsVue,
    'three-blocks': ThreeBlocksVue
  },
  props: {
    list: {
      type: Array,
      required: true
    }
  },
  data () {
    return {
      graphicPadPersonInfoData: [
        {
          field_name: '',
          field_value: '',
          field_id: ''
        }
      ]
    }
  },
  methods: {
    getPersonInfoData (data) {
      this.graphicPadPersonInfoData = data
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
