<template>
  <div
    id="graphicPad">
      <b-card
        class="my-5 mx-0"
        v-for="item in list"
        :key="item.id"
        border-variant="white"
        bg-variant="light"
        rounded>
        <b-row>
        <b-col
          cols="3">
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
            id="textarea"
            class="ml-5 text-justify text-black-75 text-left"
            style="max-width: 300px;">
            {{item.content}}</p></b-col>
        <b-col
          cols="9">
          <div
            id="image"
            class="d-inline-flex"
            style="width: 900px">
            <b-img-lazy
              v-for="pic in item.sharePics"
              :key="pic"
              class="mx-1"
              style="max-width: 300px; max-height: 300px;"
              :src="pic"
              rounded></b-img-lazy></div></b-col></b-row></b-card>
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
