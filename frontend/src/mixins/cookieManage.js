const codeHandle = require('@/utils/code')
const cookieManage = {
  created() {},
  date() {
    return {}
  },
  methods: {
    setCookie(loginState, userId, userName) {
      this.$cookie.set('isLogin', codeHandle.multiEncode(JSON.stringify(true)), 1)
      this.$cookie.set('userId', codeHandle.multiEncode(JSON.stringify(userId)), 1)
      this.$cookie.set('userName', codeHandle.multiEncode(JSON.stringify(userName)), 1)
    },
    getCookie(key) {
      try {
        return JSON.parse(codeHandle.multiDecode(this.$cookie.get(key))) || false
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
      this.$cookie.delete('csrftoken')
      this.$cookie.delete('sessionid')
    }
  }
}
export default cookieManage