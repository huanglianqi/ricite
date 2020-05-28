<template>
  <div id="login">
    <b-progress
      variant="success"
      :value="value"
      :max="max"
      class="mb-3"
      height="3px">
    </b-progress>
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
          title="账号密码登入">
          <b-form
            class="mt-5"
            align="left"
            @submit="loginSubmit"
            @reset="loginReset">
            <b-input-group
              class="mt-3 mb-3">
              <b-icon
                icon="person-fill"
                font-scale="1.5"
                class="mr-2 mt-2">
              </b-icon>
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
              <b-icon
                  icon="lock-fill"
                  font-scale="1.5"
                  class="mr-2 mt-2">
              </b-icon>
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
            title="获取账号/忘记密码">
            <b-jumbotron
              bg-variant="white">
              <h5>
                找回密码/获取账号请联系
                <br>
                <b-badge
                  variant="success"
                  class="mt-4">
                  <b-icon
                    icon="envelope"
                    animation="throb">
                  </b-icon>
                  huanglianqi@ricifoundation.com
                </b-badge>
              </h5>
            </b-jumbotron>
          </b-tab>
      </b-tabs>
    </b-jumbotron>
  </div>
</template>

<script>
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
      value: 0
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
            // location.reload()
          }
        )
    },
    loginReset () {
      this.username = ''
      this.password = ''
    }
  }
}
</script>
