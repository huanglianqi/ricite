import axios from 'axios'

const state = {
  status: '',
  token: sessionStorage.getItem('token') || '',
  user: {},
  username: '登入账号',
  firstname: '',
  lastname: '',
  id: '',
  email: '',
  subscribeEmails: []
}

const mutations = {
  auth_request (state) {
    state.status = 'loading'
  },
  auth_success (state, token, user) {
    state.status = 'success'
    state.token = token
    state.user = user
  },
  auth_error (state) {
    state.status = 'error'
  },
  logout (state) {
    state.status = ''
    state.token = ''
    state.user = {}
  },
  id (state, id) {
    state.id = id
  },
  username (state, username) {
    state.username = username
  },
  emial (state, email) {
    state.email = email
  },
  firstname (state, firstname) {
    state.firstname = firstname
  },
  lastname (state, lastname) {
    state.lastname = lastname
  },
  subscribeEmails (state, subscribeEmails) {
    state.subscribeEmails = subscribeEmails
  },
  idOut (state) {
    state.id = ''
  },
  usernameOut (state) {
    state.username = '登入账号'
  },
  emailOut (state) {
    state.email = ''
  },
  firstnameOut (state) {
    state.firstname = ''
  },
  lastnameOut (state) {
    state.lastname = ''
  },
  subscribeEmailsOut (state) {
    state.subscribeEmails = []
  }
}

const actions = {
  login ({commit}, user) {
    return new Promise(
      (resolve, reject) => {
        commit('auth_request')
        axios(
          {
            url: 'token_auth/',
            data: user,
            method: 'POST'
          }
        )
          .then(
            res => {
              const token = 'JWT' + ' ' + res.data.token
              sessionStorage.setItem(
                'token',
                token
              )
              sessionStorage.setItem(
                'username',
                user.username
              )
              sessionStorage.setItem(
                'password',
                user.password
              )
              axios.defaults.headers.common = {
                'Authorization': token
              }
              commit(
                'auth_success',
                token,
                user
              )
              resolve(res)
            }
          )
          .catch(
            err => {
              commit('auth_error')
              sessionStorage.removeItem('token')
              sessionStorage.removeItem('username')
              sessionStorage.removeItem('password')
              reject(err)
            }
          )
      }
    )
  },
  logout ({commit}) {
    return new Promise(
      (resolve, reject) => {
        commit('logout')
        commit('idOut')
        commit('usernameOut')
        commit('emailOut')
        commit('firstnameOut')
        commit('lastnameOut')
        commit('subscribeEmailsOut')
        sessionStorage.removeItem('token')
        sessionStorage.removeItem('username')
        sessionStorage.removeItem('password')
        delete axios.defaults.headers.common['Authorization']
        resolve()
      }
    )
  },
  getAccount ({commit}, username) {
    return new Promise(
      (resolve, reject) => {
        axios
          .get(`user/account/${username}/`)
          .then(
            res => {
              commit(
                'username',
                res.data.username
              )
              commit(
                'id',
                res.data.id
              )
              commit(
                'emial',
                res.data.email
              )
              commit(
                'firstname',
                res.data.first_name
              )
              commit(
                'lastname',
                res.data.last_name
              )
              commit(
                'subscribeEmails',
                res.data.subscribeEmails
              )
              resolve(res)
            }
          )
          .catch(
            err => {
              reject(err)
            }
          )
      }
    )
  }
}

const getters = {}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
