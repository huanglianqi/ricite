<template>
  <div id="app">
    <div
      id="nav-bar">
      <NavMenu/>
      <AccountProfile/>
    </div>
    <hr>
    <router-view/>
    <div
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
        to='/volunteerManagement'>
        <b-icon
          icon="people-fill"
          scale="1.25"
          aria-hidden="true">
        </b-icon>
        社群
      </router-link>
      |
      <router-link
        to='/feedbackCheck'>
        <b-icon
          icon="receipt-cutoff"
          scale="1.25"
          aria-hidden="true">
        </b-icon>
        课程
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
        to='/about'>
        <b-icon
          icon="info-circle-fill"
          scale="1.25"
          aria-hidden="true">
        </b-icon>
        关于
      </router-link>
    </div>
    <div
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
      </a>
    </div>
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

#nav-bar > * {
  display: inline-block;
  padding: 10px 10px 0px 10px;
}

</style>
