const initHandle = {
  created () {},
  data () {},
  methods: {
    initInfo () {
      let loginState = this.getCookie('isLogin')
      if (loginState) {
        console.log('get cookie success')
        this.$store.commit('LOGIN');
        this.$store.commit('USER',{
          id: this.getCookie('userId') || '',
          name: this.getCookie('userName') || '' 
        })
      }
      return loginState
    }
  }
}
export default initHandle