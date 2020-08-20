<template>
  <div
    id="home">
    <three-blocks>
      <b-button
        block
        class="p-4 shadow-lg border-0 text-left"
        v-on:click="skip(item.path)"
        v-for="item in list"
        :key="item.id"
        :variant="item.variant">
        <div
          class="font-weight-bold">
          <b-icon
            font-scale="1.5"
            :icon="item.icon"></b-icon>
          {{item.header}}</div>
        <hr>
        <div
          class="my-2"
          v-for="i in item.content"
          :key="i">
          <b-icon
            font-scale="0.9"
            shift-v="5"
            icon="star-fill"></b-icon>
          {{i}}</div></b-button>
    </three-blocks>
  </div>
</template>

<script>
import ThreeBlocksVue from './structure/ThreeBlocks.vue'

export default {
  name: 'home',
  components: {
    'three-blocks': ThreeBlocksVue
  },
  data () {
    return {
      list: [
        {
          id: 1,
          header: '图片管理',
          variant: 'outline-success',
          icon: 'images',
          path: '/pictureManage',
          content: [
            '课堂图片',
            '课堂图片精选',
            '群组动态',
            '群组动态精选'
          ]
        },
        {
          id: 2,
          header: '课程反馈',
          variant: 'outline-info',
          icon: 'card-checklist',
          path: '/feedbackCheck',
          content: [
            '每节课后课程反馈',
            '结课反馈'
          ]
        },
        {
          id: 3,
          header: '流程把控',
          variant: 'outline-secondary',
          icon: 'bezier2',
          path: '/processControl',
          content: [
            '通过审核',
            '签署协议',
            '课程反馈',
            '寄回问卷'
          ]
        }
      ]
    }
  },
  methods: {
    skip (path) {
      if (this.$router.currentRoute.path !== path) {
        this.$router.push(path)
      } else {
        this.show = false
      }
    }
  }
}
</script>
