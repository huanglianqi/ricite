<template>
  <div id="app">
    <div aria-label="nav-bar"
      id="nav-bar"
      class="ml-1 mt-1">
      <AccountProfile/>
      <br>
      <NavMenu/>
    </div>
    <router-view/>
    <div aria-label="nav-top"
      id="nav-top">
      <router-link
        to='/'>
        <b-icon
          icon="house-fill"
          scale="1.25"
          aria-hidden="true">
        </b-icon>
        首页
      </router-link>
      |
      <router-link
        to='/pictureManage'>
        <b-icon
          icon="images"
          scale="1.25"
          aria-hidden="true">
        </b-icon>
        图片
      </router-link>
      |
      <router-link
        to='/processControl'>
        <b-icon
          icon="bezier2"
          scale="1.25"
          aria-hidden="true">
        </b-icon>
        流程
      </router-link>
      |
      <router-link
        to='/feedbackCheck'>
        <b-icon
          icon="card-checklist"
          scale="1.25"
          aria-hidden="true">
        </b-icon>
        反馈
      </router-link></div>
    <div aria-label="nac-bottom"
      id="nav">
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
      </a></div>
  </div>
</template>

<script>
import AccountProfile from '@/components/AccountProfile.vue'
import NavMenu from '@/components/NavMenu.vue'

export default {
  name: 'App',
  components: {
    AccountProfile,
    NavMenu
  },
  data () {
    return {
      currentYear: new Date().getFullYear(),
      menuShow: false
    }
  },
  methods: {

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
  padding: 1rem;
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

#nav-bar {
  display: block;
  position: fixed;
  top: 0%;
  left: 0%;
  height: 10%;
  padding: 10px 10px 0px 10px;
  z-index: 100;
}

#nav-bar > * {
  display: block;
}

</style>
