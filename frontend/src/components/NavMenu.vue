<template>
  <div
    id="navMenu">
    <b-button
      block
      v-on:click="menuShow=!menuShow"
      pill
      class="shadow-sm border-white border-0 mb-1"
      variant="outline-success">
      <b-icon
        font-scale="0.9"
        shift-v="5"
        :icon="icon"></b-icon></b-button>
    <b-button
      v-for="item in list"
      :key="item.id"
      block
      pill
      v-on:click="$router.push(item.path)"
      :variant="item.variant"
      class="shadow-sm border-0 mb-1"
      v-show="menuShow">
      <b-icon
        font-scale="0.9"
        shift-v="5"
        :icon="item.icon"></b-icon></b-button>
  </div>
</template>

<script>
export default {
  name: 'navMenu',
  data () {
    return {
      menuShow: false,
      show: false,
      list: [
        {
          id: 'navMenu_item_1',
          variant: 'outline-dark',
          path: '/',
          icon: 'house',
          name: '网站首页'
        },
        {
          id: 'navMenu_item_2',
          variant: 'outline-success',
          path: '/statistics',
          icon: 'clipboard-data',
          name: '数据统计'
        },
        {
          id: 'navMenu_item_3',
          variant: 'outline-success',
          path: '/pictureManage',
          icon: 'images',
          name: '图片管理'
        },
        {
          id: 'navMenu_item_4',
          variant: 'outline-success',
          path: '/volunteerManagement',
          icon: 'people-fill',
          name: '社群运营'
        },
        {
          id: 'navMenu_item_5',
          variant: 'outline-success',
          path: '/feedbackCheck',
          icon: 'book',
          name: '课程反馈'
        },
        {
          id: 'navMenu_item_6',
          variant: 'outline-dark',
          path: '/about',
          icon: 'info-circle-fill',
          name: '关于网站'
        }
      ]
    }
  },
  computed: {
    icon () {
      if (this.menuShow) {
        return 'three-dots-vertical'
      } else {
        return 'menu-app'
      }
    }
  },
  methods: {
    showMenu () {
      this.menuShow = !this.menuShow
    }
  }
}
</script>

<style>

</style>
