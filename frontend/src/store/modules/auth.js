import axios from 'axios'

const state = {
  status: '',
  token: localStorage.getItem('token') || '',
  user: {},
  username: 'Unknown',
  firstname: '',
  lastname: '',
  id: '',
  email: ''
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
  idOut (state) {
    state.id = ''
  },
  usernameOut (state) {
    state.username = 'Unknown'
  },
  emailOut (state) {
    state.email = ''
  },
  firstnameOut (state) {
    state.firstname = ''
  },
  lastnameOut (state) {
    state.lastname = ''
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
        commit('idOut')
        commit('usernameOut')
        commit('emailOut')
        commit('firstnameOut')
        commit('lastnameOut')
        localStorage.removeItem('token')
        sessionStorage.removeItem('username')
        delete axios.defaults.headers.common['Authorization']
        resolve()
      }
    )
  },
  getAccount ({commit}, username) {
    return new Promise(
      (resolve, reject) => {
        axios
          .get(`users/?search=${username}`)
          .then(
            res => {
              commit(
                'username',
                res.data[0].username
              )
              commit(
                'id',
                res.data[0].id
              )
              commit(
                'emial',
                res.data[0].email
              )
              commit(
                'firstname',
                res.data[0].first_name
              )
              commit(
                'lastname',
                res.data[0].last_name
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

const getters = {
  account: () => {
    axios
      .get(
        'users/',
        {
          username: sessionStorage.username
        }
      )
      .then(
        res => {
          console.log(res.data[0].id)
        }
      )
      .catch(
        err => {
          console.log(err)
        }
      )
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
