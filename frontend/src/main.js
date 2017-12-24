// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueResource from 'vue-resource'
import vueCookie from 'vue-cookie'
import vuex from 'vuex'
import iView from 'iview'
import '@/zxh-theme/index.less'
import store from '@/store'


Vue.config.productionTip = false
Vue.use(VueResource)
Vue.use(vueCookie)
Vue.use(iView)

new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})