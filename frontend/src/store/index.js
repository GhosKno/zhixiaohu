import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

import { LOGIN, LOGOUT, USER } from './mutation-types'
import * as actions from './actions'

const store = new Vuex.Store({
  state: {
    isLogin: false,
    userid: '',
    userName: ''
  },
  actions,
  mutations: {
    [LOGIN](state) {
      state.isLogin = true
    },
    [LOGOUT](state) {
      state.isLogin = false
      state.userid = ''
      state.userName = ''
    },
    [USER](state, userInfo = { id: '', userName: '' }) {
      state.userid = userInfo.id
      state.userName = userInfo.userName
    }
  }
})

export default store