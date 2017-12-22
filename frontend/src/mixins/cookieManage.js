const codeHandle = require('@/utils/code')
const cookieManage = {
  created() {},
  date() {
    return {}
  },
  methods: {
    setCookie(loginState, userId, userName) {
      this.$cookie.set('isLogin', codeHandle.mulEncode(JSON.stringify(true)), 1)
      this.$cookie.set('userId', codeHandle.mulEncode(JSON.stringify(userId)), 1)
      this.$cookie.set('userName', codeHandle.mulEncode(JSON.stringify(userName)), 1)
    },
    getCookie(key) {
      try {
        return JSON.parse(codeHandle.mulDecode(this.$cookie.get(key))) || false
      } catch (e) {
        return false
      }
    },
    deleteCookie(key) {
      try {
        this.$cookie.delete(key)
        return true
      } catch (e) {
        return false
      }
    },
    cookieLogout() {
      this.$cookie.delete('isLogin')
      this.$cookie.delete('userId')
      this.$cookie.delete('userName')
    }
  }
}
export default cookieManage