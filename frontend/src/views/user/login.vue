<template lang="pug">
  div.login
    Row.login-content(type="flex" justify="center")
      Col(:sx="18" :sm="12" :md="8" :lg="4")
        div.logo
          svg(width="180" height="60")
            text(x="21.84" y="43.658" fill="#3b89e4" font-family="Wawati SC" font-size="42.667") 知小乎
            <path fill="#fff" d="M49 25.994a24.8 24.8 0 0 1 7.117.494c2.321.66 3.63 2.611 2.542 1.977.817.476 1.059.179 2.033 0s1.747-3.051 0-3.46a31.906 31.906 0 0 0-7.626-1.483c-3.221-.063-3.926.431-4.066 2.472z"/>
            <path fill="#fff" d="M49.508 25.994s8.835-.239 9.659 1.483 2.542-.494 2.542-.494a1.5 1.5 0 0 1-1.525 1.483c-1.532.085-4.414-1.393-5.592-1.483s-5.084-.494-5.084-.494v-.495z"/>
            <path fill="red" fill-rule="evenodd" d="M50.017 24.017s2.9-4.579 11.184-3.955c7.657.577 5.507 4.347 5.592 4.943s-2.975 7.46-4.575 8.4a23.6 23.6 0 0 0 .508-4.943 2.625 2.625 0 0 0-2.034-1.977c-.857-.34-2.912-2.049-4.067-1.977s-4.691-1.408-6.608-.491z"/>
            <path fill="#fff" d="M62.569 32.1s-2.107-.833-1.122 1.236 3 .582 2.8 0a4.012 4.012 0 0 0-1.678-1.236z"/>
            <path fill="#ebebeb" d="M63.235 32.42s.489 2.468-1.525 1.483c.224.687 1.649 1.8 2.542.494s-1.017-1.977-1.017-1.977z"/>
            <path fill="#eb2a2a" fill-rule="evenodd" d="M61.71 26.983s2.089-2.025 2.542-2.472c.012 1.62-.655 6.232-1.525 7.415-.949-.211 1.422-4.277-1.017-4.943z"/>
        div.slogan
          span 与世界分享你的知识、经验和见解
        Tabs(value="login")
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
                Input(type="text" v-model="regForm.checkPassword" placeholder="再次输入密码")
              FormItem.button-content(style="text-align:center")
                Button(type="primary" @click="regSubmit()" long size="large") 注册知小乎
                Button(type="ghost" @click="handleReset('regForm')" long size="large") 重置
</template>


<script>
export default {
  name: 'login',
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
        this.$http.post('/api/accounts/login/', this.loginForm)
          .then(res => {
            if(res.body.success) {
              this.$Message.success('登陆成功')
              //todo
              console.log(res.body.data)
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
        this.$http.post('/api/accounts/register/', this.regForm)
          .then(res => {
            if(res.body.success) {
              this.$Message.success('注册成功')
              //todo
              console.log(res.body.data)
            } else {
              this.$Message.error(res.data.msg)
            }
          })
      }
      this.$refs['regForm'].validate(valid => {
        if(valid) submit()
      })
    }

  }
}
</script>

<style lang="less" scoped>
.login {
  height: 100vh;
  width: 100vw;
  padding-top: 15%;
  .login-content {
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


