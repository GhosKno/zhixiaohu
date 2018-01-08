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
import { Tabs, TabPane } from 'element-ui'
import timeago from '@/utils/time';

Vue.component(Tabs.name, Tabs)
Vue.component(TabPane.name, TabPane)

Vue.config.productionTip = false
Vue.use(VueResource)
Vue.use(vueCookie)
Vue.use(iView)
Vue.use(timeago)

new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})