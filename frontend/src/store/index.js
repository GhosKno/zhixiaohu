import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

import { LOGIN, LOGOUT, USER, AVATAR } from './mutation-types'
import * as actions from './actions'

const store = new Vuex.Store({
  state: {
    isLogin: false,
    userid: '',
    userName: '',
    avatarUrl: ''
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
    },
    [AVATAR](state, url = '') {
      state.avatarUrl = url
    }
  }
})

export default store