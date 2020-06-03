<template>
  <div id="app">
    <div id="nav-top">
      <router-link
          to='/'>
          <b-icon
            icon="house-fill"
            scale="1.25"
            shift-v="1.25"
            aria-hidden="true">
          </b-icon>
          home
      </router-link>
      |
      <router-link
        to='/about'>
        <b-icon
          icon="info-circle-fill"
          scale="1.25"
          shift-v="1.25"
          aria-hidden="true">
        </b-icon>
        about
      </router-link>
      |
      <b-badge
        v-b-toggle.profile
        :variant="authOrNotCrl">
        <b-icon
          icon="people-fill"
          scale="1.25"
          shift-v="1.25"
          aria-hidden="true">
        </b-icon>
        {{username}}
      </b-badge>
      <b-sidebar
        id="profile"
        :title="username"
        shadow
        backdrop>
        <b-jumbotron
          bg-variant="light">
          <p
            class="text-left mb-3 text-break"
            v-if="isAuth">
            <b-icon
              icon="person-fill">
            </b-icon>
            {{fullname}}
          </p>
          <p
            class="text-left mb-5 text-break"
            v-if="isAuth">
            <b-icon
              icon="envelope-fill">
            </b-icon>
            {{email}}
          </p>
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
          <b-button
            v-if="isAuth"
            v-b-toggle.modifyInfo
            block
            class="mt-3"
            variant="outline-info">
            <div
              v-on:click="close=!close">
              <b-icon
                icon="gear-fill"
                animation="null"
                v-show="close">
              </b-icon>
              <b-icon
                icon="gear-fill"
                animation="spin"
                v-show="!close">
              </b-icon>
              修改个人账户信息
              <b-icon
                icon="caret-left-fill"
                shift-v="1.25"
                v-show="close">
              </b-icon>
              <b-icon
                icon="caret-down-fill"
                shift-v="1.25"
                v-show="!close">
              </b-icon>
            </div>
          </b-button>
          <b-collapse
            id="modifyInfo">
            <b-form
              class="mb-5"
              align="left"
              @submit="modifyInfoSubmit">
              <b-input-group
                class="mt-3 mb-3">
                <template
                  v-slot:prepend>
                  <b-input-group-text>
                    姓
                  </b-input-group-text>
                </template>
                <b-form-input
                  id="modifyLastname"
                  v-model="lastname"
                  required
                  trim>
                </b-form-input>
              </b-input-group>
              <b-input-group>
                <template
                  v-slot:prepend>
                  <b-input-group-text>
                    名
                  </b-input-group-text>
                </template>
                <b-form-input
                  id="modifyFirstname"
                  v-model="firstname"
                  required
                  trim>
                </b-form-input>
              </b-input-group>
              <b-input-group
                class="mt-3 mb-3">
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
                  id="modifyEmail"
                  v-model="email"
                  required
                  trim>
                </b-form-input>
              </b-input-group>
              <b-button
                type="submit"
                variant="outline-success"
                block
                class="mt-4"
                v-b-toggle.modifyInfo>
                <div
                  v-on:click="close=!close">
                  <b-icon
                    icon="box-arrow-in-right"
                    class="mr-2">
                  </b-icon>
                  确定修改
                </div>
              </b-button>
              <b-button
                v-on:click="modifyReset"
                variant="outline-danger"
                block>
                <b-icon
                  icon="arrow-clockwise"
                  class="mr-2">
                </b-icon>
                重置输入
              </b-button>
            </b-form>
          </b-collapse>
          <b-button
            v-if="isAuth"
            block
            class="mt-3"
            variant="outline-dark"
            v-on:click="resetPassword"
            v-show="waitTime"
            disabled>
            <b-icon
              icon="unlock-fill"
              shift-v="1.25">
            </b-icon>
            请前往邮箱（重新发送 {{waitTime}}）
          </b-button>
          <b-button
            v-if="isAuth"
            block
            class="mt-3"
            variant="outline-dark"
            v-on:click="resetPassword"
            v-show="afterWait">
            <b-icon
              icon="lock-fill"
              shift-v="1.25">
            </b-icon>
            通过邮箱重置密码
          </b-button>
          <b-button
            variant="outline-danger"
            v-on:click="logout"
            block
            class="mt-3"
            v-if="isAuth">
            <b-icon
              icon="box-arrow-left"
              shift-v="1.25">
            </b-icon>
            退出/切换账号
          </b-button>
          <b-button
            variant="outline-success"
            v-on:click="login"
            v-else
            block
            class="mt-3">
            <b-icon
              icon="box-arrow-in-right"
              shift-v="1.25">
            </b-icon>
            登入验证
          </b-button>
        </b-jumbotron>
        <template
          v-if="isAuth"
          v-slot:footer="{hide}">
          <b-button
            variant="outline-danger"
            block
            v-on:click="hide">
            关闭
          </b-button>
        </template>
      </b-sidebar>
    </div>
    <router-view/>
    <div id="nav">
      Copyright &copy; {{currentYear}}
      <a
        href="http://www.ricifoundation.org/">
        <b-icon
          icon="link45deg"
          scale="1.25"
          shift-v="1,25"
          aria-hidden="true">
        </b-icon>
        RICI Foundation
      </a>
      .
      All Rights Reserved |
      <a
        href="http://www.beian.miit.gov.cn/">
        <b-icon
          icon="lock-fill"
          scale="1.25"
          shift-v="1,25"
          aria-hidden="true">
        </b-icon>
        粤ICP备14073346号
      </a>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data () {
    return {
      currentYear: new Date().getFullYear(),
      authOrNotCrl: '',
      username: 'Unknown',
      lastname: '',
      firstname: '',
      email: '',
      id: '',
      fullname: '',
      dismissSecs: 2,
      dismissFailAlert: 0,
      dismissSuccessAlert: 0,
      waitTime: 0,
      afterWait: true,
      oneMin: 60,
      close: true
    }
  },
  computed: {
    isAuth () {
      if (this.$store.state.auth.status === 'success') {
        return true
      } else {
        return false
      }
    }
  },
  watch: {
    isAuth (val) {
      if (val) {
        this.getAccount()
        this.authOrNotCrl = 'success'
      } else {
        this.strechAccount()
        this.authOrNotCrl = 'dark'
      }
    },
    firstname (val) {
      this.fullname = this.lastname + val
    },
    lastname (val) {
      this.fullname = val + this.firstname
    },
    waitTime (val) {
      if (val === 0) {
        this.afterWait = true
      } else {
        this.afterWait = false
      }
    }
  },
  methods: {
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
          }
        )
        .catch(
          err => {
            console.log(err)
          }
        )
    },
    login () {
      if (this.$router.currentRoute.path === '/login') {
        this.$router.go()
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
    modifyInfoSubmit () {
      axios
        .patch(
          `users/${this.username}/`,
          {
            first_name: this.firstname,
            last_name: this.lastname,
            email: this.email
          }
        )
        .then(
          () => {
            this.showSuccessAlert()
          }
        )
        .catch(
          () => {
            this.showFailAlert()
          }
        )
    },
    modifyReset () {
      this.getAccount()
    },
    resetPassword () {
      axios
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
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}

#nav {
  padding: 10px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

#nav-top {
  padding: 10px;
  padding-bottom: 10px;
}

#nav-top a {
  font-weight: bold;
  color: #2c3e50;
}

#nav-top a.router-link-exact-active {
  color: #42b983;
}
</style>
