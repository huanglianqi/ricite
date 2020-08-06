<template>
  <div
    id="home">
    <three-blocks>
      <b-button
        class="mt-5 p-5"
        v-on:click="skip(item.path)"
        v-for="item in list"
        :key="item.id"
        :variant="item.variant">
        <b-icon
          :icon="item.icon"
          font-scale="10"></b-icon>
        <h3>
          {{item.header}}</h3></b-button>
    </three-blocks>
  </div>
</template>

<script>
import ThreeBlocksVue from './ThreeBlocks.vue'

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
          path: '/pictureManage'
        },
        {
          id: 2,
          header: '课程反馈',
          variant: 'outline-info',
          icon: 'book',
          path: '/feedbackCheck'
        },
        {
          id: 3,
          header: '社群运营',
          variant: 'outline-secondary',
          icon: 'people-fill',
          path: '/feedbackCheck'
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
