<template>
  <div
    id="accountProfile">
    <b-button
      v-b-toggle.accountProfile_sidebar
      :variant="accountProfile_btn_clr">
      <b-icon
        icon="person-fill"
        shift-v="1.25">
      </b-icon>
      {{username}}
    </b-button>
    <b-sidebar
      id="accountProfile_sidebar"
      :title="username"
      shadow
      backdrop>
      <b-jumbotron
        bg-variant="light">
        <div
          v-show="isLogin">
          <p
            class="text-left mb-3 text-break">
            <b-icon
              icon="person-fill">
            </b-icon>
            {{fullname}}
          </p>
          <p
            class="text-left mb-5 text-break">
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
            <b-icon
              icon="check2">
            </b-icon>
            操作成功
          </b-alert>
          <b-alert
            variant="danger"
            dismissble
            fade
            :show="dismissFailAlert"
            @dismiss-count-down="changeFailAlert">
            <b-icon
              icon="exclamation">
            </b-icon>
            操作失败
          </b-alert>
          <div
            v-on:click="baseInfo_collapse_open=!baseInfo_collapse_open">
            <b-button
              v-b-toggle.baseInfo_collapse
              variant="outline-info"
              block
              class="mt-3">
              <b-icon
                icon="gear-fill"
                animation="null"
                class="float-left"
                v-show="!baseInfo_collapse_open">
              </b-icon>
              <b-icon
                icon="gear-fill"
                animation="spin"
                class="float-left"
                v-show="baseInfo_collapse_open">
              </b-icon>
              修改个人账户信息
              <b-icon
                icon="caret-left-fill"
                shift-v="-1.25"
                class="float-right"
                v-show="!baseInfo_collapse_open">
              </b-icon>
              <b-icon
                icon="caret-down-fill"
                class="float-right"
                shift-v="-1.25"
                v-show="baseInfo_collapse_open">
              </b-icon>
            </b-button>
          </div>
          <b-collapse
            id="baseInfo_collapse">
            <b-form
              class="mb-5"
              align="left"
              @submit="baseInfo_modify_submit">
              <b-input-group
                class="mt-3 mb-3">
                <b-input-group-prepend>
                  <b-button
                    class="bg-white"
                    variant="white border-0">
                  姓
                  </b-button>
                </b-input-group-prepend>
                <b-form-input
                  id="baseInfo_lastname"
                  v-model="lastname"
                  required
                  trim
                  class="border-white">
                </b-form-input>
              </b-input-group>
              <b-input-group>
                <b-input-group-prepend>
                  <b-button
                    class="bg-white border-0"
                    variant="white">
                  名
                  </b-button>
                </b-input-group-prepend>
                <b-form-input
                  id="baseInfo_firsename"
                  v-model="firstname"
                  required
                  trim
                  class="bg-white border-0">
                </b-form-input>
              </b-input-group>
              <b-input-group
                class="mt-3 mb-3">
                <b-input-group-prepend>
                  <button
                    class="bg-white border-0"
                    variant="white">
                    <b-icon
                      icon="envelope-fill"
                      font-scale="1.25">
                    </b-icon>
                  </button>
                </b-input-group-prepend>
              <b-form-input
                id="baseInfo_email"
                v-model="email"
                required
                trim
                class="bg-white border-0">
              </b-form-input>
            </b-input-group>
              <b-button
                type="submit"
                variant="outline-success"
                block
                class="mt-4"
                v-b-toggle.baseInfo_collapse>
                <div
                  v-on:click="baseInfo_collapse_open=false">
                  <b-icon
                    icon="box-arrow-in-right"
                    shift-v="-1.25"
                    class="float-left">
                  </b-icon>
                  修改账户信息
                </div>
              </b-button>
              <b-button
                v-on:click="modifyReset"
                variant="outline-danger"
                block>
                <b-icon
                  icon="arrow-clockwise"
                  shift-v="-1.25"
                  class="float-left">
                </b-icon>
                重置输入
                </b-button>
            </b-form>
          </b-collapse>
          <b-button
            block
            class="mt-3"
            variant="outline-success"
            v-b-toggle.subscriptionList_collapse>
            <div
              v-on:click="subscriptionList_collapse_open=!subscriptionList_collapse_open">
              <b-icon
                icon="calendar-check-fill"
                shift-v="-1.25"
                v-show="!subscriptionList_collapse_open"
                class="float-left">
              </b-icon>
              <b-icon
                icon="calendar-plus-fill"
                shift-v="-1.25"
                v-show="subscriptionList_collapse_open"
                class="float-left">
              </b-icon>
              设置订阅邮件
              <b-icon
                icon="caret-left-fill"
                shift-v="-1.25"
                v-show="!subscriptionList_collapse_open"
                class="float-right">
              </b-icon>
              <b-icon
                icon="caret-down-fill"
                shift-v="-1.25"
                v-show="subscriptionList_collapse_open"
                class="float-right">
              </b-icon>
            </div>
          </b-button>
          <b-collapse
            id="subscriptionList_collapse">
            <b-form-checkbox-group
              id="subscriptionList_detail"
              v-model="subscriptionList_sec"
              :options="subscriptionList_opt"
              switches
              stacked
              class="ml-3 mt-3 mb-3"
              align="left">
            </b-form-checkbox-group>
            <b-button
              type="submit"
              block
              variant="outline-success"
              class="mt-4"
              v-on:click="subscriptionList_modify_submit"
              v-b-toggle.subscriptionList_collapse>
              <div
                v-on:click="subscriptionList_collapse_open=false">
                <b-icon
                  icon="box-arrow-in-right"
                  class="float-left"
                  shift-v="-1.25">
                </b-icon>
                修改订阅设置
              </div>
            </b-button>
            <b-button
              block
              variant="outline-danger"
              v-on:click="modifyReset"
              class="mb-5">
              <b-icon
                icon="arrow-clockwise"
                shift-v="-1.25"
                class="float-left">
              </b-icon>
              重置修改
            </b-button>
          </b-collapse>
          <b-button
            block
            class="mt-3"
            variant="outline-dark"
            v-on:click="resetPassword_submit"
            :disabled="!resetPassword_afterWait">
            <div
              v-show="resetPassword_afterWait">
              <b-icon
                icon="lock-fill"
                shift-v="-1.25"
                class="float-left">
              </b-icon>
              通过邮箱重置密码
            </div>
            <div
              v-show="resetPassword_waitTime">
              <b-icon
                icon="unlock-fill"
                shift-v="-1.25"
                class="float-left">
              </b-icon>
              请前往邮箱（重新发送 {{resetPassword_waitTime}}）
            </div>
          </b-button>
          <b-button
            variant="outline-danger"
            v-on:click="logout"
            block
            class="mt-3">
            <b-icon
              icon="box-arrow-left"
              shift-v="-1.25"
              class="float-left">
            </b-icon>
            退出/切换账号
          </b-button>
        </div>
        <b-button
          variant="outline-success"
          v-on:click="login"
          v-show="!isLogin"
          block
          class="mt-3">
          <b-icon
            icon="box-arrow-in-right"
            shift-v="-1.25"
            class="float-left">
          </b-icon>
          登入验证
        </b-button>
        <b-button
          variant="outline-danger"
          block
          v-b-toggle.accountProfile_sidebar
          class="mt-3">
          <b-icon
            icon="power"
            class="float-left">
          </b-icon>
          关闭账户菜单
        </b-button>
      </b-jumbotron>
    </b-sidebar>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'app-account',
  data () {
    return {
      accountProfile_btn_clr: '',
      username: '登入账号',
      lastname: '',
      firstname: '',
      email: '',
      id: '',
      fullname: '',
      dismissSecs: 2,
      dismissFailAlert: 0,
      dismissSuccessAlert: 0,
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
      subscriptionList_sec: []
    }
  },
  computed: {
    isLogin () {
      if (this.$store.state.auth.status === 'success') {
        return true
      } else {
        return false
      }
    }
  },
  watch: {
    isLogin (val) {
      if (val) {
        this.getAccount()
        this.accountProfile_btn_clr = 'outline-success'
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
    baseInfo_modify_submit () {
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
            this.showSuccessAlert()
          }
        )
        .catch(
          () => {
            this.showFailAlert()
          }
        )
    }
  }
}
</script>

<style>

</style>
