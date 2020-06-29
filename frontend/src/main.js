// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import axios from 'axios'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import draggable from 'vuedraggable'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap/dist/css/bootstrap.css'
import ECharts from 'vue-echarts'
import 'echarts-liquidfill'
import 'echarts/lib/chart/bar'
import 'echarts/lib/component/tooltip'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(draggable)
Vue.component('v-chart', ECharts)
Vue.config.productionTip = false
Vue.prototype.$http = axios

const token = sessionStorage.getItem(
  'token'
)
if (token) {
  Vue.prototype.$http.defaults.headers.common = {
    'Authentication': token
  }
}

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
