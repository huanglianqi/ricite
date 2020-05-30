<template>
  <div id="app">
    <div id="nav-top">
      <router-link
          to='/'>
          <b-icon
            icon="house-fill"
            scale="1.25"
            shift-v="1.25"
            aria-hidden="true"></b-icon>
          home
      </router-link>
      |
      <router-link
        to='/about'>
        <b-icon
          icon="info-circle-fill"
          scale="1.25"
          shift-v="1.25"
          aria-hidden="true"></b-icon>
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
          aria-hidden="true"></b-icon>
        {{username}}
      </b-badge>
      <b-sidebar
        id="profile"
        title="账户信息"
        shadow
        backdrop>
        <b-jumbotron>
          <p>
            {{id}}
            {{email}}
            {{fullname}}
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
            <b-icon
              icon="gear-fill"
              animation="null"
              class="when-closed"></b-icon>
            <b-icon
              icon="gear-fill"
              animation="spin"
              class="when-open">
            </b-icon>
            修改个人信息
            <b-icon
              icon="caret-left-fill"
              shift-v="1.25"
              class="when-closed">
            </b-icon>
            <b-icon
              icon="caret-down-fill"
              shift-v="1.25"
              class="when-open">
            </b-icon>
          </b-button>
          <b-collapse
            id="modifyInfo">
            <b-form
              class="mb-5"
              align="left"
              @submit="modifyInfoSubmit"
              @reset="modifyReset">
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
                <b-icon
                  icon="box-arrow-in-right"
                  class="mr-2">
                </b-icon>
                确定修改
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
          </b-collapse>
          <b-button
            v-if="isAuth"
            v-b-toggle.modifyPasswd
            block
            class="mt-3"
            variant="outline-dark">
            <b-icon
              icon="gear-fill"
              animation="null"
              class="when-closed"></b-icon>
            <b-icon
              icon="gear-fill"
              animation="spin"
              class="when-open">
            </b-icon>
            修改账号密码
            <b-icon
              icon="caret-left-fill"
              shift-v="1.25"
              class="when-closed">
            </b-icon>
            <b-icon
              icon="caret-down-fill"
              shift-v="1.25"
              class="when-open">
            </b-icon>
          </b-button>
          <b-collapse
            id="modifyPasswd">
            <b-form
              class="mb-5"
              align="left"
              @submit="modifyPasswdSubmit"
              @reset="modifyPasswdReset">
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
                class="mt-4"
                v-b-toggle.modifyPasswd>
                确认修改密码
              </b-button>
            </b-form>
          </b-collapse>
          <b-button
            variant="outline-danger"
            v-on:click="logout"
            v-if="isAuth"
            block
            class="mt-3">
            退出/切换账号
          </b-button>
          <b-button
            variant="outline-success"
            v-on:click="login"
            v-else
            block
            class="mt-3">
            登入验证
          </b-button>
        </b-jumbotron>
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
      newPasswd: '',
      newPasswdAgain: '',
      dismissSecs: 2,
      dismissFailAlert: 0,
      dismissSuccessAlert: 0,
      successAlert: false,
      failAlert: false
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
        .post(
          `users/${this.username}/`,
          {
            first_name: this.firstname,
            last_name: this.lastname,
            email: this.email
          }
        )
        .then(
          () => {
            this.successAlert = true
            this.showSuccessAlert()
          }
        )
        .catch(
          () => {
            this.failAlert = true
            this.showFailAlert()
          }
        )
    },
    modifyReset () {
      this.username = this.$store.state.auth.username
    },
    modifyPasswdSubmit () {
      if (this.newPasswd === this.newPasswdAgain) {
        axios
          .patch(
            `users/${this.id}/`,
            {
              password: this.newPasswd,
              username: this.username
            }
          )
          .then(
            console.log('ok')
          )
          .catch(
            err => {
              console.log(err)
            }
          )
      } else {
        console.log('not ok')
      }
    },
    modifyPasswdReset () {
      console.log(this.newPasswd)
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

<style>
.collapsed > .when-open,
.not-collapsed > .when-closed {
  display: none;
}

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
