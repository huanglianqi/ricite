<template>
  <div>
    <b-alert
      variant="success"
      dismissble
      fade
      :show="dismissSuccessAlert"
      @dismiss-count-down="changeSuccessAlert">
      操作成功，{{dismissSuccessAlert}}秒后将自动跳转自登入页面
    </b-alert>
    <b-alert
      variant="danger"
      dismissble
      fade
      :show="dismissFailAlert"
      @dismiss-count-down="changeFailAlert">
      操作失败，请确认是否正确输入，或者重新获取链接
    </b-alert>
    <b-jumbotron
      class="shadow-sm mx-auto m-5"
      style="max-width: 30rem;"
      bg-variant="white">
      <b-form
        class="mb-5"
        align="left"
        @submit="resetPassword"
        @reset="resetInput">
        <b-input-group
          class="mt-3 mb-3">
          <template
            v-slot:prepend>
            <b-input-group-text>
              <b-icon
                icon="lock-fill"
                font-scale="1.25">
              </b-icon>
            </b-input-group-text>
          </template>
          <b-form-input
            id="newPasswd"
            type="password"
            v-model="newPasswd"
            required
            trim
            placeholder="输入新密码">
          </b-form-input>
        </b-input-group>
        <b-input-group
          class="mt-3 mb-3">
          <template
            v-slot:prepend>
            <b-input-group-text>
              <b-icon
                icon="lock-fill"
                font-scale="1.25">
              </b-icon>
            </b-input-group-text>
          </template>
          <b-form-input
            id="newPasswdAgain"
            type="password"
            v-model="newPasswdAgain"
            required
            trim
            placeholder="再次输入新密码">
          </b-form-input>
        </b-input-group>
        <b-button
          type="submit"
          variant="outline-success"
          block
          class="mt-3">
          确认修改密码
        </b-button>
        <b-button
          type="reset"
          variant="outline-danger"
          block
          class="mt-3">
          重置输入
        </b-button>
      </b-form>
    </b-jumbotron>
  </div>
</template>

<script>
import Axios from 'axios'
// @ is an alias to /src

export default {
  name: 'resetPassword',
  data () {
    return {
      newPasswd: '',
      newPasswdAgain: '',
      dismissSecs: 2,
      dismissFailAlert: 0,
      dismissSuccessAlert: 0
    }
  },
  methods: {
    resetPassword () {
      if (this.newPasswd === this.newPasswdAgain) {
        Axios
          .post(
            'password_reset/confirm/',
            {
              password: this.newPasswd,
              token: this.$router.currentRoute.query.token
            }
          )
          .then(
            this.showSuccessAlert()
          )
          .then(
            this.$router.push('/login')
          )
          .catch(
            this.showFailAlert()
          )
      } else {
        this.showFailAlert()
      }
    },
    resetInput () {
      this.newPasswd = ''
      this.newPasswdAgain = ''
    },
    changeFailAlert (dismissCountDown) {
      this.dismissFailAlert = dismissCountDown
    },
    changeSuccessAlert (dismissCountDown) {
      this.dismissSuccessAlert = dismissCountDown
    },
    showFailAlert () {
      this.dismissFailAlert = this.dismissSecs
    },
    showSuccessAlert () {
      this.dismissSuccessAlert = this.dismissSecs
    }
  }
}
</script>
