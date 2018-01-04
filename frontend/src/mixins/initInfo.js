const initHandle = {
  created() {},
  data() {},
  methods: {
    initInfo() {
      let loginState = this.getCookie('isLogin')
      if (loginState) {
        this.$store.commit('LOGIN');
        this.$store.commit('USER', {
          id: this.getCookie('userId') || '',
          userName: this.getCookie('userName') || ''
        })
      }
      return loginState
    }
  }
}
export default initHandle