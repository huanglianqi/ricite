const state = {
  dismissSecs: 2,
  dismissFailAlert: 0,
  dismissSuccessAlert: 0
}

const mutations = {
  operateSuccess (state) {
    state.dismissSuccessAlert = state.dismissSecs
  },
  operateFail (state) {
    state.dismissFailAlert = state.dismissSecs
  }
}

const actions = {
  showSuccessAlert ({commit}) {
    commit('operateSuccess')
  },
  showFailAlert ({commit}) {
    commit('operateFailAlert')
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
