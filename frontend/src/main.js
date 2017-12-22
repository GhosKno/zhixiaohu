// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueResource from 'vue-resource'
import vueCookie from 'vue-cookie'
import iView from 'iview'
import 'iview/dist/styles/iview.css'
import store from '@/store'


Vue.config.productionTip = false
Vue.use(VueResource)
Vue.use(vueCookie)
Vue.use(iView)
Vue.use(store)
  /* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})