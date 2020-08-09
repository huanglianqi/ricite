<template>
  <div
    id="login">
    <b-jumbotron
      class="mx-auto m-5 shadow"
      style="max-width: 30rem;"
      bg-variant="white">
      <div
        v-show="isLoginPage">
        <div
          class="shadow-sm p-3 rounded mb-3 bg-info text-white font-weight-bold text-center">
          日慈信息管理平台 ｜ 账号登入</div>
        <b-input-group
          class="shadow-sm pt-3 px-3 rounded my-3">
          <b-input-group-prepend
            tag="p">
            <b-button
              disabled
              class="bg-white border-0">
              <b-icon
                variant="dark"
                icon="person-fill"></b-icon></b-button></b-input-group-prepend>
          <b-form-input
            id="login-username"
            variant="white"
            v-model="username"
            type="text"
            required
            placeholder="请输入正确的用户名"
            class="bg-white border-0"></b-form-input></b-input-group>
        <b-input-group
          class="my-3 pt-3 px-3 shadow-sm">
          <b-input-group-prepend
            tag="p">
            <b-button
              disabled
              class="bg-white border-0">
              <b-icon
                icon="lock-fill"
                variant="dark"></b-icon></b-button></b-input-group-prepend>
          <b-form-input
              id="login-password"
              v-model="password"
              required
              type="password"
              placeholder="请输入对应用户名的密码"
              class="bg-white border-0"></b-form-input></b-input-group>
        <b-row>
          <b-col>
            <b-button
              class="shadow-sm border-0"
              variant="outline-success"
              v-on:click="loginSubmit"
              block>
              <b-icon
                icon="box-arrow-in-right"
                class="float-left"
                shift-v="-1.25"></b-icon>
              登入</b-button></b-col>
          <b-col>
            <b-button
              v-on:click="loginReset"
              variant="outline-danger"
              class="shadow-sm border-0"
              block>
              <b-icon
                icon="arrow-clockwise"
                class="float-left"
                shift-v="-1.25"></b-icon>
              重置</b-button></b-col>
          <b-col>
            <b-button
              v-on:click="isLoginPage=false"
              variant="outline-info"
              class="shadow-sm border-0"
              block>
              <b-icon
                v-b-tooltip.hover
                title="忘记密码？请点击这里，我们将通过邮件进行密码重置"
                icon="question"
                class="float-left"
                shift-v="-1.25"></b-icon>
              密码</b-button></b-col></b-row></div>
      <div
        v-show="!isLoginPage">
        <div
          class="shadow-sm p-3 rounded mb-3 bg-info text-white font-weight-bold text-center">
          日慈信息管理平台 ｜ 重置密码</div>
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
              v-model="email"
              type="email"
              required
              placeholder="输入账号绑定的邮箱"
              class="bg-white border-0"></b-form-input></b-input-group>
        <b-row>
          <b-col>
            <b-button
              v-on:click="emailSubmit"
              variant="outline-success"
              block
              class="shadow-sm border-0"
              v-if="afterWait">
              <b-icon
                icon="envelope-fill"
                class="float-left"
                shift-v="-1.25">
              </b-icon>
              发送
            </b-button>
            <b-button
              variant="outline-success"
              block
              class="shadow-sm border-0"
              v-else
              disabled>
              <b-icon
                icon="envelope-open-fill"
                class="float-left"
                shift-v="-1.25"></b-icon>
              {{waitTime}}</b-button></b-col>
        <b-col>
          <b-button
            v-on:click="emailReset"
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
            v-on:click="isLoginPage=true"
            variant="outline-info"
            block
            class="shadow-sm border-0">
            <b-icon
              icon="arrow-left"></b-icon>
            返回</b-button></b-col></b-row></div></b-jumbotron>
  </div>
</template>

<script>
import Axios from 'axios'

export default {
  name: 'login',
  components: {},
  computed: {
    passwordState () {
      if (this.password.length > 3) {
        return true
      } else {
        return false
      }
    }
  },
  data () {
    return {
      username: '',
      password: '',
      email: '',
      isLoginPage: true,
      waitTime: 0,
      afterWait: true,
      oneMin: 60
    }
  },
  watch: {
    waitTime (val) {
      if (val === 0) {
        this.afterWait = true
      } else {
        this.afterWait = false
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
    loginSubmit () {
      this.$store
        .dispatch(
          'auth/login',
          {
            username: this.username,
            password: this.password
          }
        )
        .then(
          () => {
            this.$router.push('/')
          }
        )
        .catch(
          () => {
            this.showToast(
              '登入失败',
              '可能是以下原因导致：1.账号或密码输入错误；2.网络出现问题，请刷新后重试',
              'warning'
            )
          }
        )
    },
    loginReset () {
      this.username = ''
      this.password = ''
    },
    emailSubmit () {
      Axios
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
              '可能是以下原因导致：1.该邮箱未绑定任何账号；2.输入错误或邮箱格式错误；3.网络出现问题，请刷新后重试',
              'warning'
            )
          }
        )
    },
    emailReset () {
      this.email = ''
    },
    showWait () {
      this.waitTime = this.oneMin
    },
    timeCountDown () {
      let count = setInterval(
        () => {
          this.waitTime -= 1
          if (this.waitTime === 0) {
            clearInterval(count)
          }
        },
        1000
      )
    }
  }
}
</script>

<style>

</style>
