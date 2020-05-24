import Vue from 'vue'
import Router from 'vue-router'
import store from '../store'
import axios from 'axios'

import Home from '@/components/Home'
import Login from '@/components/Login'
import About from '@/components/About'

Vue.use(Router)

axios.defaults.baseURL = 'http://localhost:8000/api/'

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
      beforeEnter: (to, from, next) => {
        if (
          to.name !== 'Login' && store.getters.authStatus !== 'success'
        ) next({name: 'Login'})
        else next()
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/about',
      name: 'About',
      component: About
    }
  ]
})
