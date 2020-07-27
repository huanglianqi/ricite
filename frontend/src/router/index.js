import Vue from 'vue'
import Router from 'vue-router'
import store from '../store'
import axios from 'axios'

import Home from '@/components/Home'
import Login from '@/components/Login'
import About from '@/components/About'
import ResetPassword from '@/components/ResetPassword'
import FeedbackCheck from '@/components/FeedbackCheck'
import VolunteerManagement from '@/components/VolunteerManagement'
import PictureManage from '@/components/PictureManage'
import DataStatistics from '@/components/DataStatistics'

Vue.use(Router)

axios.defaults.baseURL = 'http://localhost:8000/'

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
      beforeEnter: (to, from, next) => {
        if (
          to.name !== 'Login' && store.state.auth.status !== 'success'
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
      component: About,
      beforeEnter: (to, from, next) => {
        if (
          to.name !== 'Login' && store.state.auth.status !== 'success'
        ) next({name: 'Login'})
        else next()
      }
    },
    {
      path: '/resetPassword',
      name: 'ResetPassword',
      component: ResetPassword
    },
    {
      path: '/feedbackCheck',
      name: 'FeedbackCheck',
      component: FeedbackCheck,
      beforeEnter: (to, from, next) => {
        if (
          to.name !== 'Login' && store.state.auth.status !== 'success'
        ) next({name: 'Login'})
        else next()
      }
    },
    {
      path: '/volunteerManagement',
      name: 'VolunteerManagement',
      component: VolunteerManagement,
      beforeEnter: (to, from, next) => {
        if (
          to.name !== 'Login' && store.state.auth.status !== 'success'
        ) next({name: 'Login'})
        else next()
      }
    },
    {
      path: '/pictureManage',
      name: 'PictureManage',
      component: PictureManage,
      beforeEnter: (to, from, next) => {
        if (
          to.name !== 'Login' && store.state.auth.status !== 'success'
        ) next({name: 'Login'})
        else next()
      }
    },
    {
      path: '/statistics',
      name: 'dataStatistics',
      component: DataStatistics,
      beforeEnter: (to, from, next) => {
        if (
          to.name !== 'Login' && store.state.auth.status !== 'success'
        ) next({name: 'Login'})
        else next()
      }
    }
  ]
})
