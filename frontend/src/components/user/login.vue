<template lang="pug">
  div.login
    Row.login-content(type="flex" justify="center")
      Col(:sx="16" :sm="14" :md="10" :lg="6")
        div.logo
          svg(width="180" height="60")
            //- text(x="21.84" y="43.658" fill="#3b89e4" font-family="Wawati SC" font-size="42.667") 知小乎
            <path fill="#3b89e4" fill-rule="evenodd" d="M30.54 34.1c1.34-.25 2.61-.12 5.34-.4-.18-3.1-.18-22.63-.18-22.63a16.07 16.07 0 0 1 .24-3.64 100.01 100.01 0 0 1-13.61 0 16.72 16.72 0 0 1 .24 3.64L22.1 34.1c3.46-.47 3.75 0 3.75 0l.3 3.6a11.53 11.53 0 0 0 4.4-3.6zm-5.22-3V10.47h7.45V31.1H31.1l-3.31 2.48-.82-2.48h-1.66zM14.2 20.4c.12-2.05.16-4.37.2-7.85 2.28 0 4.36.04 5.69.16 0 0 .47-2.53-.8-2.99-2-.14-6.17-.17-6.17-.17s-4.08 0-4.24-.04C10.22 5.8 10.92 6.38 11.72 4c-6.15.54-7.6 11.13-9.55 13.09 2.02.17 4.2-2.04 5.62-4.53h3.4c.04 3.08-.04 5.36-.2 7.84-3.8 0-3.82-.43-7.17-.01a4.96 4.96 0 0 0-2.37 3.4 91.58 91.58 0 0 1 9.26-.4c-.8 5.7-5.85 12.2-9.72 16.44a4.74 4.74 0 0 0 4.48-1.29c1.14-1.08 5.3-5.33 6.93-9.38 2.4 2.57 5.23 6.87 6.3 6.9.7.2.3-1.83-.2-4.05a21.78 21.78 0 0 0-3.93-5.02c-.15-.15-1.65 1.65-1.65 1.65s.68-2.37.48-2.56a16.63 16.63 0 0 0 .52-2.68c2.92.04 5.08.16 6.85.36a3.44 3.44 0 0 0-1.34-3.48c-4.25.13-2.47.08-5.23.12zM60.19 5.15c.6-.4.51-1.03-.24-.99-1.35.08-3.1.18-4.02 1.35-.12.96-.12 2.02-.15 4.99v22.58c0 1.42-.44 1.86-5 1.66-.5 1.71.45 2.31 1.84 2.96 3.32 1.53 6.74-.26 6.74-3.59V7.82c0-1.43.11-2.26.83-2.66zM75.2 27.7c-.46-1.47-6.6-13.64-7.74-13.9s-3.18 1.35-3.18 1.35c2.62 3.96 5.66 8.77 7.37 13.48 0 0 3.39.3 3.55-.93zM50.22 15.82c1-.56.91-1.03-.12-1.15a4.89 4.89 0 0 0-4.1 1.58 36.76 36.76 0 0 1-5.99 12.44c1.04.53 1.62.4 3.5-.06a31.48 31.48 0 0 0 5.44-10.4c.48-1.42.87-2.18 1.27-2.41zm41.27 3.73c.25-.56-5.3-6.89-6-7.13-2.18-.52-2.27 1.35-2.23 1.56.96 1.73 4.41 5.06 4.93 5.57.88.87 3.06.57 3.3 0zm17.2-6.3c.2-.36.69-.6.18-1.13-.57-.57-2.07.3-3.31.83-2.08 2.15-2.86 3.75-4.96 6.6a18.66 18.66 0 0 1 2.45.82c3.17-2.78 5.2-6.85 5.64-7.13zM94.67 9.83v12.12c-8.25 0-12.27-.25-16.41.07 0 0-.27 2.85.77 3.01 1.16.17 7.46-.55 15.77-.54v10.73c0 1.54-1.67.95-6.08.12a12.25 12.25 0 0 0 2.77 4c5.61 1.86 6.62-.52 6.62-4.12V24.5c6.75 0 8.97.55 13.75.44.31.39 1.14-2.92 1.14-2.92-5.05-.3-8.14 0-14.89 0l.18-12.66c6.9-.99 8.81-1.15 10.68-1.03.71.04.65-.11.24-.71-.6-.87-1.02-2.3-2.83-2.92a86.37 86.37 0 0 1-9.84 1.77 105.76 105.76 0 0 1-16.4 1.42 13.42 13.42 0 0 0 2.26 2.58 103.84 103.84 0 0 0 12.27-.63z"/>
            <path fill="#fff" fill-rule="evenodd" d="M24.01 6.99a24.72 24.72 0 0 1 7.1.5c2.32.65 3.63 2.6 2.54 1.97.81.47 1.06.18 2.03 0s1.74-3.05 0-3.46a31.8 31.8 0 0 0-7.61-1.48c-3.21-.06-3.92.43-4.06 2.47zm13.54 6.1s-2.1-.83-1.12 1.23 3 .59 2.8 0a4 4 0 0 0-1.68-1.23z"/>
            <path fill="#ebebeb" fill-rule="evenodd" d="M24.52 6.99s8.82-.24 9.64 1.48 2.54-.5 2.54-.5a1.5 1.5 0 0 1-1.52 1.49c-1.53.08-4.4-1.4-5.58-1.48s-5.07-.5-5.07-.5v-.5zm13.7 6.42s.49 2.46-1.52 1.48c.22.69 1.64 1.8 2.54.5s-1.02-1.98-1.02-1.98z"/>
            <path fill="red" fill-rule="evenodd" d="M25.03 5.01S27.92.44 36.19 1.06c7.64.58 5.5 4.34 5.58 4.94s-2.97 7.45-4.57 8.4a23.6 23.6 0 0 0 .5-4.94 2.62 2.62 0 0 0-2.02-1.97c-.86-.34-2.9-2.05-4.06-1.98s-4.68-1.41-6.6-.5z"/>
            <path fill="#eb2a2a" fill-rule="evenodd" d="M36.7 7.98l2.54-2.47c0 1.61-.66 6.22-1.53 7.4-.95-.21 1.42-4.27-1.01-4.93z" data-name="形状 6"/>
        div.slogan
          span 与世界分享你的知识、经验和见解
        Tabs(:value="defaultPaneName")
          TabPane(name="login" label="登陆") 
            Form(:model="loginForm"
                 ref="loginForm"
                 :rules="loginRule")
              FormItem(prop="username")
                Input(type="text" v-model="loginForm.username" placeholder="用户名或邮箱")
              FormItem(prop="password")
                Input(type="password" v-model="loginForm.password" placeholder="密码")
              FormItem.button-content(style="text-align:center")
                Button(type="primary" @click="loginSubmit()" long size="large") 登陆
                Button(type="ghost" @click="handleReset('loginForm')" long size="large") 重置
          TabPane(name="reg" label="注册") 
            Form(:model="regForm"
                 ref="regForm"
                 :rules="regRule")
              FormItem(prop="username")
                Input(type="text" v-model="regForm.username" placeholder="用户名")
              FormItem(prop="email")
                Input(type="email" v-model="regForm.email" placeholder="邮箱")
              FormItem(prop="password")
                Input(type="password" v-model="regForm.password" placeholder="密码")
              FormItem(prop="checkPassword")
                Input(type="password" v-model="regForm.checkPassword" placeholder="再次输入密码")
              FormItem.button-content(style="text-align:center")
                Button(type="primary" @click="regSubmit()" long size="large") 注册知小乎
                Button(type="ghost" @click="handleReset('regForm')" long size="large") 重置
</template>


<script>
import Vue from 'vue'
import cookieManage from '@/mixins/cookieManage'
import initInfo from '@/mixins/initInfo'
export default {
  name: 'login',
  mixins: [cookieManage, initInfo],
  data () {
    const validatePassCheck = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('Please enter your password again'))
      } else if (value !== this.regForm.password) {
        callback(new Error('The two input passwords do not match!'))
      } else {
        callback()
      }
    }
    return {
      defaultPaneName: 'login',
      loginForm: {
        username: '',
        password: ''
      },
      regForm: {
        username: '',
        password: '',
        email: '',
        checkPassword: ''
      },
      loginRule: {
        username: [
          { required: true, message: 'Please fill in the user name', trigger: 'blur' }
        ],
        password: [
          { required: true, message: 'Please fill in the password.', trigger: 'blur' },
          { type: 'string', min: 6, message: 'The password length cannot be less than 6 bits', trigger: 'blur' }
        ]
      },
      regRule: {
        username: [
          { required: true, message: 'Please fill in the user name', trigger: 'blur' }
        ],
        password: [
          { required: true, message: 'Please fill in the password.', trigger: 'blur' },
          { type: 'string', min: 6, message: 'The password length cannot be less than 6 bits', trigger: 'blur' }
        ],
        checkPassword: [
          { validator: validatePassCheck, trigger: 'blur' }
        ],
        email: [
          { required: true, message: 'Mailbox cannot be empty', trigger: 'blur' },
          { type: 'email', message: 'Incorrect email format', trigger: 'blur' }
        ],
      }
    }
  },
  methods: {
    handleReset(form) {
      this.$refs[form].resetFields()
    },
    loginSubmit() {
      const submit  = () => {
        this.$http.post('/api/users/login/', this.loginForm)
          .then(res => {
            if(res.body.success) {
              this.$Message.success('登陆成功')
              Vue.http.headers.common['X-CSRF-TOKEN'] = this.$cookie.get('csrftoken')
              this.setCookie(true, res.body.data.id, res.body.data.nickname)
              this.$store.commit('LOGIN')
              this.$store.commit('USER', {id: res.body.data.id, userName: res.body.data.nickname})
              this.$store.commit('AVATAR', res.body.data.avatar)
              this.$router.push({name: 'home'})
            } else {
              this.$Message.error(res.data.msg)
            }
          })
      }
      this.$refs['loginForm'].validate(valid => {
        if(valid) submit()
      })
    },
    regSubmit() {
       const submit  = () => {
        this.$http.post('/api/users/register/', this.regForm)
          .then(res => {
            if(res.body.success) {
              this.$Message.success('注册成功')
              Vue.http.headers.common['X-CSRF-TOKEN'] = this.$cookie.get('csrftoken')
              this.setCookie(true, res.body.data.id, res.body.data.nickname)
              this.$store.commit('LOGIN')
              this.$store.commit('USER', {id: res.body.data.id, userName: res.body.data.nickname})
              this.$store.commit('AVATAR', res.body.data.avatar)
              this.$router.push({name: 'home'})
            } else {
              this.$Message.error(res.data.msg)
            }
          })
      }
      this.$refs['regForm'].validate(valid => {
        if(valid) submit()
      })
    }
  },
  created () {
    if (this.initInfo()) {
      this.$router.push({name: 'home'})
    }
    if(this.$route.params['register']) {
      this.defaultPaneName = 'reg'
    }
  }
}
</script>

<style lang="less" scoped>
.login {
  height: 100vh;
  width: 100vw;
  position: fixed;
  .login-content {
    height: initial;
    margin-top: 10%;
    .logo {
      text-align: center;
    }
    .slogan {
      margin: 4px 0;
      text-align: center;
      font-size: 1.5em;
    }
    .button-content button{
      margin-bottom: 10px;
    }
  }
}
</style>


