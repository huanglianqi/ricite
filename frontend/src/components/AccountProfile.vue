<template>
  <div
    id="accountProfile">
    <b-button
      class="shadow-sm border-0 border-white"
      pill
      v-b-toggle.accountProfile_sidebar
      :variant="accountProfile_btn_clr">
      <b-icon
        icon="person-fill"
        shift-v="4"
        font-scale="0.9"></b-icon></b-button>
    <b-sidebar
      id="accountProfile_sidebar"
      title="账号管理"
      shadow
      backdrop
      v-model="show">
      <b-jumbotron
        bg-variant="light">
        <div
          v-show="isLogin">
          <div
            class="text-left mb-3 shadow p-3 rounded">
            <div>
              <small
                class="text-muted">账号</small>
              <b-button
                v-b-tooltip.hover
                title="退出/切换账号"
                v-on:click="logout"
                size="sm"
                pill
                variant="outline-danger"
                class="float-right shadow-sm border-0 border-white">
                <b-icon

                  icon="box-arrow-left"
                  font-scale="0.9"
                  shift-v="3"></b-icon></b-button></div>
            <div
              class="text-monospace">
              <b-icon
                icon="person-fill"></b-icon>
              {{username}}</div></div>
          <div
            class="text-left mb-3 shadow p-3 rounded">
            <div>
              <small
                class="text-muted">姓名</small>
              <b-button
                v-b-tooltip.hover
                title="小慈应该怎么称呼你"
                v-b-modal.modifyName
                size="sm"
                pill
                variant="outline-success"
                class="float-right shadow-sm border-0 border-white">
                <b-icon
                  icon="pencil-square"
                  font-scale="0.9"
                  shift-v="3"></b-icon></b-button></div>
            <div
              class="text-monospace">
              <b-icon
                icon="person-fill"></b-icon>
              {{fullname}}</div></div>
          <div
            class="text-left mb-3 shadow p-3 rounded">
            <div>
              <small
                class="text-muted">邮箱</small>
              <b-button
                v-b-tooltip.hover
                title="修改绑定邮箱，邮箱可用于找回或重置密码"
                v-b-modal.modifyEmail
                size="sm"
                pill
                variant="outline-success"
                class="float-right shadow-sm border-0 border-white">
                <b-icon
                  icon="pencil-square"
                  font-scale="0.9"
                  shift-v="3"></b-icon></b-button></div>
            <div
              class="text-monospace">
              <b-icon
                icon="mailbox2"></b-icon>
              {{emailName}}
              <br/>
              <b-icon
                icon="at"
                class="mr-1"
                font-scale="1.25"
                shift-h="-1"></b-icon>{{emailAt}}</div></div>
          <div
            class="text-left mb-3 shadow p-3 rounded">
            <div>
              <small
                class="text-muted">订阅</small>
              <b-button
                v-b-tooltip.hover
                title="功能尚未开放"
                size="sm"
                pill
                variant="outline-dark"
                class="float-right shadow-sm border-0 border-white">
                <b-icon
                  icon="question"
                  font-scale="0.9"
                  shift-v="3"></b-icon></b-button></div></div>
          <div
            class="text-left mb-3 shadow p-3 rounded">
            <div>
              <small
                class="text-muted">密码</small>
              <b-button
                v-b-tooltip.hover
                title="通过邮箱重置密码:你的邮箱将收到一份邮件，点击邮箱中的链接，进入重置密码页面"
                v-on:click="resetPassword_submit"
                size="sm"
                pill
                :disabled="!resetPassword_afterWait"
                variant="outline-success"
                class="float-right shadow-sm border-0 border-white">
                <b-icon
                  v-show="resetPassword_afterWait"
                  icon="envelope-fill"
                  font-scale="0.9"
                  shift-v="3"></b-icon>
                <b-icon
                  v-show="resetPassword_waitTime"
                  icon="envelope-open-fill"
                  font-scale="0.9"
                  shift-v="3"></b-icon></b-button></div>
                  <b-icon
                    icon="lock-fill"></b-icon>
                  通过邮箱重置密码 | {{resetPassword_waitTime}}</div></div>
        <div
          v-show="!isLogin"
          class="text-left mb-3 shadow p-3 rounded">
          <div>
            <small
              class="text-muted">账号</small>
            <b-button
              v-b-tooltip.hover
              title="跳转至登入页面"
              v-on:click="login"
              size="sm"
              pill
              variant="outline-success"
              class="float-right shadow-sm border-0 border-white">
              <b-icon
                icon="box-arrow-in-right"
                font-scale="0.9"
                shift-v="3"></b-icon></b-button></div>
          <div
            class="text-monospace">
            <b-icon
              icon="person-fill"></b-icon>
            账号未登入</div></div></b-jumbotron></b-sidebar>
    <modal-model
      id="modifyEmail"
      size="md"
      :hide-footer="true">
      <div
        class="shadow-sm p-3 rounded mb-3 bg-info text-white font-weight-bold text-center">
        日慈信息管理平台 ｜ 修改绑定邮箱</div>
        <b-input-group
          class="shadow-sm p-3 px-3 rounded my-3">
          <b-input-group-prepend>
            <b-button
              variant="white"
              disabled>
              <b-icon
                icon="mailbox2"
                variant="dark"></b-icon></b-button></b-input-group-prepend>
          <b-form-input
            id="email"
            v-model="newEmail"
            type="email"
            required
            placeholder="输入新的邮箱地址"
            class="bg-white border-0"></b-form-input></b-input-group>
        <b-row>
          <b-col>
            <b-button
              v-on:click="email_modify_submit"
              variant="outline-success"
              block
              class="shadow-sm border-0">
              <b-icon
                icon="pencil-square"
                class="float-left"
                shift-v="-1.25"></b-icon>
              修改</b-button></b-col>
        <b-col>
          <b-button
            v-on:click="newEmail=''"
            variant="outline-danger"
            block
            class="shadow-sm border-0">
            <b-icon
              icon="arrow-clockwise"
              class="float-left"
              shift-v="-1.25"></b-icon>
            重置</b-button></b-col>
        <b-col>
          <b-button
            v-on:click="quitModifyEmail"
            variant="outline-info"
            block
            class="shadow-sm border-0">
            <b-icon
              icon="arrow-left"></b-icon>
            返回</b-button></b-col></b-row></modal-model>
    <modal-model
      :hide-footer="true"
      id="modifyName"
      size="md">
      <div
        class="shadow-sm p-3 rounded mb-3 bg-info text-white font-weight-bold text-center">
        日慈信息管理平台 ｜ 修改姓名</div>
        <b-input-group
          class="shadow-sm p-3 px-3 rounded my-3">
          <b-input-group-prepend>
            <b-button
              variant="white"
              disabled>
              <b-icon
                icon="person-fill"
                variant="dark"></b-icon></b-button></b-input-group-prepend>
          <b-form-input
            id="lastname"
            v-model="newLastName"
            type="text"
            required
            placeholder="姓"
            class="bg-white border-0"></b-form-input>
          <b-form-input
            id="firstname"
            v-model="newFirstName"
            type="text"
            required
            placeholder="名"
            class="bg-white border-0"></b-form-input></b-input-group>
        <b-row>
          <b-col>
            <b-button
              v-on:click="name_modify_submit"
              variant="outline-success"
              block
              class="shadow-sm border-0">
              <b-icon
                icon="pencil-square"
                class="float-left"
                shift-v="-1.25"></b-icon>
              修改</b-button></b-col>
        <b-col>
          <b-button
            v-on:click="resetModifyName"
            variant="outline-danger"
            block
            class="shadow-sm border-0">
            <b-icon
              icon="arrow-clockwise"
              class="float-left"
              shift-v="-1.25"></b-icon>
            重置</b-button></b-col>
        <b-col>
          <b-button
            v-on:click="quitModifyName"
            variant="outline-info"
            block
            class="shadow-sm border-0">
            <b-icon
              icon="arrow-left"></b-icon>
            返回</b-button></b-col></b-row></modal-model>
  </div>
</template>

<script>
import axios from 'axios'
import ModalModelVue from './ModalModel.vue'

export default {
  name: 'app-account',
  components: {
    'modal-model': ModalModelVue
  },
  data () {
    return {
      newEmail: '',
      newFirstName: '',
      newLastName: '',
      accountProfile_btn_clr: 'outline-secondary',
      username: '登入账号',
      lastname: '',
      firstname: '',
      email: '',
      id: '',
      fullname: '',
      dismissSecs: 2,
      resetPassword_waitTime: 0,
      resetPassword_afterWait: true,
      oneMin: 60,
      baseInfo_collapse_open: false,
      subscriptionList_collapse_open: false,
      subscriptionList_opt: [
        {text: '项目数据 ｜ 日报', value: 'base_daily'},
        {text: '项目数据 ｜ 周报', value: 'base_weekly'},
        {text: '项目数据 ｜ 月报', value: 'base_monthly'},
        {text: '反馈数据 ｜ 日报', value: 'feedback_daily'},
        {text: '反馈数据 ｜ 周报', value: 'feedback_weekly'},
        {text: '反馈数据 ｜ 月报', value: 'feedback_monthly'}
      ],
      subscriptionList_sec: [],
      show: false
    }
  },
  computed: {
    isLogin () {
      if (this.$store.state.auth.status === 'success') {
        return true
      } else {
        return false
      }
    },
    emailName () {
      return this.email.substring(0, this.email.search('@'))
    },
    emailAt () {
      return this.email.substring(this.email.search('@') + 1)
    }
  },
  watch: {
    isLogin (val) {
      if (val) {
        this.getAccount()
        this.accountProfile_btn_clr = 'outline-info'
      } else {
        this.strechAccount()
        this.accountProfile_btn_clr = 'outline-secondary'
      }
    },
    firstname (val) {
      this.fullname = this.lastname + val
    },
    lastname (val) {
      this.fullname = val + this.firstname
    },
    resetPassword_waitTime (val) {
      if (val === 0) {
        this.resetPassword_afterWait = true
      } else {
        this.resetPassword_afterWait = false
      }
    }
  },
  methods: {
    showToast (title, content, variant) {
      this.$bvToast.toast(
        content,
        {
          title: title,
          solid: true,
          variant: variant
        }
      )
    },
    strechAccount () {
      this.username = this.$store.state.auth.username
      this.firstname = this.$store.state.auth.firstname
      this.lastname = this.$store.state.auth.lastname
      this.id = this.$store.state.auth.id
      this.email = this.$store.state.auth.email
    },
    getAccount () {
      this.$store
        .dispatch(
          'auth/getAccount',
          sessionStorage.username
        )
        .then(
          () => {
            this.username = this.$store.state.auth.username
            this.firstname = this.$store.state.auth.firstname
            this.lastname = this.$store.state.auth.lastname
            this.id = this.$store.state.auth.id
            this.email = this.$store.state.auth.email
            this.subscriptionList_sec = this.$store.state.auth.subscribeEmails
          }
        )
        .catch(
          err => {
            this.showToast(
              '获取账号信息失败',
              `error: ${err},请刷新页面后重新登入`,
              'warning'
            )
          }
        )
    },
    login () {
      if (this.$router.currentRoute.path === '/login') {
        this.show = false
      } else {
        this.$router.push('/login')
      }
    },
    logout () {
      this.$store
        .dispatch('auth/logout')
        .then(
          this.$router.push('/login')
        )
        .catch(
          err => (console.log(err))
        )
    },
    email_modify_submit () {
      this.email = this.newEmail
      this.baseInfo_modify_submit(`你的邮箱已成功修改为${this.email}`)
      this.$bvModal.hide('modifyEmail')
      this.newEmail = ''
    },
    quitModifyEmail () {
      this.$bvModal.hide('modifyEmail')
      this.newEmail = ''
    },
    name_modify_submit () {
      this.firstname = this.newFirstName
      this.lastname = this.newLastName
      this.baseInfo_modify_submit(`你的姓名已成功修改为${this.lastname}${this.firstname}`)
      this.$bvModal.hide('modifyName')
      this.newFirstName = ''
      this.newLastName = ''
    },
    quitModifyName () {
      this.$bvModal.hide('modifyName')
      this.newFirstName = ''
      this.newLastName = ''
    },
    resetModifyName () {
      this.newFirstName = ''
      this.newLastName = ''
    },
    baseInfo_modify_submit (content) {
      axios
        .patch(
          `user/account/${this.username}/`,
          {
            first_name: this.firstname,
            last_name: this.lastname,
            email: this.email
          }
        )
        .then(
          () => {
            this.showToast(
              '修改成功',
              content,
              'success'
            )
          }
        )
        .catch(
          () => {
            this.showToast(
              '修改失败',
              '可能是以下原因导致：网络出现问题，请刷新后重试',
              'warning'
            )
          }
        )
    },
    modifyReset () {
      this.getAccount()
    },
    resetPassword_submit () {
      axios
        .post(
          'password_reset/',
          {
            email: this.email
          }
        )
        .then(
          () => {
            this.showToast(
              '发送成功',
              `重置密码的链接已成功发送至${this.email}，前往邮箱并打开链接进行密码重置`,
              'success'
            )
            this.showWait()
            this.timeCountDown()
          }
        )
        .catch(
          () => {
            this.showToast(
              '发送失败',
              '可能是以下原因导致：网络出现问题，请刷新后重试',
              'warning'
            )
          }
        )
    },
    showWait () {
      this.resetPassword_waitTime = this.oneMin
    },
    timeCountDown () {
      let count = setInterval(
        () => {
          this.resetPassword_waitTime -= 1
          if (this.resetPassword_waitTime === 0) {
            clearInterval(count)
          }
        },
        1000
      )
    },
    subscriptionList_modify_submit () {
      axios
        .patch(
          `user/account/${this.username}/`,
          {
            subscribeEmails: this.subscriptionList_sec
          }
        )
        .then(
          () => {
            this.showToast(
              '修改成功',
              `你的邮件${this.email}的订阅修改成功`,
              'success'
            )
          }
        )
        .catch(
          () => {
            this.showToast(
              '修改失败',
              '可能是以下原因导致：网络出现问题，请刷新后重试',
              'warning'
            )
          }
        )
    }
  }
}
</script>

<style>

</style>
