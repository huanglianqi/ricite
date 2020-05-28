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
        <b-button
          variant="outline-danger"
          v-on:click="logout"
          v-if="isAuth">
          退出登入
        </b-button>
        <b-button
          variant="outline-success"
          v-on:click="login"
          v-else>
          登入验证
        </b-button>
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
      email: ''
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
    isAuth (val, old) {
      if (val) {
        this.getAccount()
        this.authOrNotCrl = 'success'
      } else {
        this.username = 'Unknown'
        this.authOrNotCrl = 'dark'
      }
    }
  },
  methods: {
    getAccount () {
      axios.get(
        'users/?search=',
        {
          params: {
            username: sessionStorage.username
          }
        }
      )
        .then(
          res => {
            this.username = res.data[0].username
            this.firstname = res.data[0].firstname
            this.lastname = res.data[0].lastname
            this.email = res.data[0].email
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
