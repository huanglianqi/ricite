<template>
  <div
    id="navMenu">
    <b-button
      v-b-toggle.navMenu_sidebar
      variant="outline-success">
      <b-icon
        icon="list">
      </b-icon>
      导航菜单
    </b-button>
    <b-sidebar
      title="导航菜单"
      id="navMenu_sidebar"
      shadow
      backdrop
      v-model="show">
      <b-jumbotron
        bg-variant="light">
        <div
          v-for="navMenu_item in navMenu_list"
          :key="navMenu_item.id">
          <b-button
            :variant="navMenu_item.variant"
            v-on:click="navMenu_skip(navMenu_item.path)"
            class="mt-3"
            block>
            <b-icon
              :icon="navMenu_item.icon"
              class="float-left">
            </b-icon>
            {{navMenu_item.name}}
          </b-button>
        </div>
        <b-button
          variant="outline-danger"
          block
          class="mt-3"
          v-b-toggle.navMenu_sidebar>
          <b-icon
            icon="power"
            class="float-left">
          </b-icon>
          关闭导航菜单
        </b-button>
      </b-jumbotron>
    </b-sidebar>
  </div>
</template>

<script>
export default {
  name: 'navMenu',
  data () {
    return {
      show: false,
      navMenu_list: [
        {
          id: 'navMenu_item_1',
          variant: 'outline-dark',
          path: '/',
          icon: 'house-fill',
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
          icon: 'receipt-cutoff',
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
  methods: {
    navMenu_skip (path) {
      if (this.$router.currentRoute.path !== path) {
        this.$router.push(path)
      } else {
        this.show = false
      }
    }
  }
}
</script>

<style>

</style>
