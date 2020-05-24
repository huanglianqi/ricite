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
        state.state = 'success'
        state.token = token
        state.user = user
    },
    auth_error (state) {
        state.status = 'error'
    }
}

const actions = {
    login ({commit}, user) {
        return new Promise (
            (resolve, reject) =>
        )
    }
}