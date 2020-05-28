import axios from 'axios'

const state = {
  status: '',
  token: localStorage.getItem('token') || '',
  user: {}
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
              localStorage.setItem(
                'token',
                token
              )
              sessionStorage.setItem(
                'username',
                user.username
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
              localStorage.removeItem('token')
              sessionStorage.removeItem('username')
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
        localStorage.removeItem('token')
        sessionStorage.removeItem('username')
        delete axios.defaults.headers.common['Authorization']
        resolve()
      }
    )
  }
}

const getters = {
  authStatus: state => state.status
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
