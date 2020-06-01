<template>
  <div id="login">
    <b-progress
      variant="success"
      :value="value"
      :max="max"
      class="mb-3"
      height="3px">
    </b-progress>
    <b-alert
      variant="success"
      dismissble
      fade
      :show="dismissSuccessAlert"
      @dismiss-count-down="changeSuccessAlert">
      操作成功
    </b-alert>
    <b-alert
      variant="danger"
      dismissble
      fade
      :show="dismissFailAlert"
      @dismiss-count-down="changeFailAlert">
      操作失败
    </b-alert>
    <b-jumbotron
      class="shadow-sm mx-auto m-5"
      style="max-width: 30rem;"
      bg-variant="white">
      <b-tabs
        content-class="mt-1"
        fill
        pills
        active-nav-item-class="font-weight-bold bg-success"
        nav-class="bg-light">
        <b-tab
          title="验证登入">
          <b-form
            class="mt-5"
            align="left"
            @submit="loginSubmit"
            @reset="loginReset">
            <b-input-group
              class="mt-3 mb-3">
              <template
                  v-slot:prepend>
                  <b-input-group-text>
                    <b-icon
                      icon="person-fill"
                      font-scale="1.25">
                    </b-icon>
                  </b-input-group-text>
                </template>
              <b-form-input
                id="login-username"
                v-model="username"
                required
                :state="nameState"
                trim
                placeholder="请输入正确的用户名">
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
                  id="login-password"
                  v-model="password"
                  required
                  type="password"
                  :state="nameState"
                  trim
                  placeholder="请输入对应用户名的密码">
              </b-form-input>
            </b-input-group>
            <b-button
              type="submit"
              variant="outline-success"
              block
              class="mt-4">
              <b-icon
                icon="box-arrow-in-right"
                class="mr-2">
              </b-icon>
              验证登入
            </b-button>
            <b-button
              type="reset"
              variant="outline-danger"
              block>
              <b-icon
                icon="arrow-clockwise"
                class="mr-2">
              </b-icon>
              重置输入
            </b-button>
          </b-form>
        </b-tab>
        <b-tab
          title="找回密码">
          <b-jumbotron
            bg-variant="white">
            <b-form
              class="mt-1"
              align="left"
              @submit="emailSubmit"
              @reset="emailReset">
              <b-input-group
                class="mt-1 mb-3">
                <template
                  v-slot:prepend>
                  <b-input-group-text>
                    <b-icon
                      icon="envelope-fill"
                      font-scale="1.25">
                    </b-icon>
                  </b-input-group-text>
                </template>
                <b-form-input
                  id="email"
                  v-model="email"
                  type="email"
                  required
                  trim
                  placeholder="输入账号绑定的邮箱">
                </b-form-input>
              </b-input-group>
              <b-button
                type="submit"
                variant="outline-success"
                block
                class="mt-3 mb-3"
                v-show="afterWait">
                发送重置密码链接至邮箱
              </b-button>
              <b-button
                type="submit"
                variant="outline-success"
                block
                class="mt-3 mb-3"
                v-show="waitTime"
                disabled>
                请前往邮箱（重新发送 {{waitTime}}）
              </b-button>
              <b-button
                type="reset"
                variant="outline-danger"
                block
                class="mt-3 mb-3">
                重置输入
              </b-button>
            </b-form>
          </b-jumbotron>
        </b-tab>
      </b-tabs>
    </b-jumbotron>
  </div>
</template>

<script>
import Axios from 'axios'
// @ is an alias to /src

export default {
  name: 'login',
  components: {},
  computed: {
    nameState () {
      if (this.username.length > 3) {
        return true
      } else {
        return false
      }
    },
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
      max: 10,
      value: 0,
      email: '',
      waitTime: 0,
      afterWait: true,
      oneMin: 60,
      dismissSecs: 2,
      dismissFailAlert: 0,
      dismissSuccessAlert: 0
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
          this.value = this.max
        )
        .then(
          () => {
            this.$router.push(
              '/'
            )
          }
        )
        .catch(
          err => {
            console.log(err)
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
            this.showSuccessAlert()
            this.showWait()
            this.timeCountDown()
          }
        )
        .catch(
          () => {
            this.showFailAlert()
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
