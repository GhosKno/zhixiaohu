import Vue from 'vue'
const initHandle = {
  created() {},
  data() {},
  methods: {
    initInfo() {
      let loginState = this.getCookie('isLogin')
      if (loginState) {
        Vue.http.headers.common['X-CSRFTOKEN'] = this.$cookie.get('csrftoken')
        this.$store.commit('LOGIN');
        this.$store.commit('USER', {
          id: this.getCookie('userId') || '',
          userName: this.getCookie('userName') || ''
        })
        this.$http.get(`/api/profiles/${this.$store.state.userid}/`)
          .then(res => {
            if (res.body.success) {
              this.$store.commit('AVATAR', res.body.data.avatar || '/static/avatar.jpg')
            }
          })
      }
      return loginState
    }
  }
}
export default initHandle