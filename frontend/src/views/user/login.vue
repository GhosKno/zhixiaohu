<template lang="pug">
  
  div.login
    Row.login-content(type="flex" justify="center")
      Col(:sx="16" :sm="14" :md="10" :lg="6")
        div.logo
          svg
            use(xlink:href="#logo")
        div.slogan
          span 与世界分享你的知识、经验和见解
        Tabs(:value="defaultPaneName")
          TabPane.pane(name="login" label="登陆") 
            Form(:model="loginForm"
                 ref="loginForm"
                 :rules="loginRule")
              FormItem(prop="username")
                Input(type="text" v-model="loginForm.username" placeholder="用户名或邮箱")
              FormItem(prop="password")
                Input(type="password" v-model="loginForm.password" placeholder="密码"  @keyup.enter="loginSubmit()")
              FormItem.button-content(style="text-align:center")
                Button(type="primary" @click="loginSubmit()" long size="large") 登陆
                Button(type="ghost" @click="handleReset('loginForm')" long size="large") 重置
          TabPane.pane(name="reg" label="注册") 
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
    svgIcon
</template>


<script>
import Vue from "vue";
import cookieManage from "@/mixins/cookieManage";
import initInfo from "@/mixins/initInfo";
import svgIcon from "@/components/svg";
import api from "@/utils/api";

export default {
  name: "login",
  mixins: [cookieManage, initInfo],
  components: { svgIcon },
  data() {
    const validatePassCheck = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次完整输入密码"));
      } else if (value !== this.regForm.password) {
        callback(new Error("两次密码不一致！"));
      } else {
        callback();
      }
    };
    return {
      defaultPaneName: "login",
      loginForm: {
        username: "",
        password: ""
      },
      regForm: {
        username: "",
        password: "",
        email: "",
        checkPassword: ""
      },
      loginRule: {
        username: [{ required: true, message: "请输入您的用户名", trigger: "blur" }],
        password: [
          { required: true, message: "请完整输入密码", trigger: "blur" },
          { type: "string", min: 6, message: "密码长度不能小于六位", trigger: "blur" }
        ]
      },
      regRule: {
        username: [{ required: true, message: "请输入您的用户名", trigger: "blur" }],
        password: [
          { required: true, message: "请完整输入密码", trigger: "blur" },
          { type: "string", min: 6, message: "密码长度不能小于六位", trigger: "blur" }
        ],
        checkPassword: [{ validator: validatePassCheck, trigger: "blur" }],
        email: [
          { required: true, message: "邮箱不能为空", trigger: "blur" },
          { type: "email", message: "请输入正确的邮箱", trigger: "blur" }
        ]
      }
    };
  },
  methods: {
    handleReset(form) {
      this.$refs[form].resetFields();
    },
    loginSubmit() {

            console.log(this.loginForm)
      const submit = () => {
        api.login(this.loginForm).then(
          res => {
            if (res.body.success) {
              this.$Message.success("登陆成功");
              Vue.http.headers.common["X-CSRFTOKEN"] = this.$cookie.get(
                "csrftoken"
              );
              this.setCookie(true, res.body.data.id, res.body.data.nickname);
              this.$store.commit("LOGIN");
              this.$store.commit("USER", {
                id: res.body.data.id,
                userName: res.body.data.nickname
              });
              this.$store.commit(
                "AVATAR",
                res.body.data.avatar
              );
              this.$router.push({ name: "home" });
            } else {
              this.$Message.error(res.data.msg);
            }
          },
          err => {
            this.$Message.error(err.status + " " + err.statusText);
          }
        );
      };
      this.$refs["loginForm"].validate(valid => {
        if (valid) submit();
      });
    },
    regSubmit() {
      const submit = () => {
        api.register(this.regForm).then(
          res => {
            if (res.body.success) {
              this.$Message.success("注册成功");
              Vue.http.headers.common["X-CSRFTOKEN"] = this.$cookie.get(
                "csrftoken"
              );
              this.setCookie(true, res.body.data.id, res.body.data.nickname);
              this.$store.commit("LOGIN");
              this.$store.commit("USER", {
                id: res.body.data.id,
                userName: res.body.data.nickname
              });
              this.$store.commit("AVATAR", res.body.data.avatar);
              this.$router.push({ name: "home" });
            } else {
              this.$Message.error(res.data.msg);
            }
          },
          err => {
            this.$Message.error(err.status + " " + err.statusText);
          }
        );
      };
      this.$refs["regForm"].validate(valid => {
        if (valid) submit();
      });
    }
  },
  created() {
    this.$cookie.delete("sessionid");
    if (this.initInfo()) {
      this.$router.push({ name: "home" });
    }
    if (this.$route.params["register"]) {
      this.defaultPaneName = "reg";
    }
  }
};
</script>

<style lang="less" scoped>
.login {
  overflow: auto;
  height: 100vh;
  width: 100vw;
  position: fixed;
  .login-content {
    height: initial;
    width: 100%;
    margin-top: 3%;
    .logo {
      text-align: center;
    }
    .slogan {
      margin: 4px 0;
      text-align: center;
      font-size: 1em;
    }
    .button-content button {
      margin-bottom: 10px;
    }
  }
}
.pane {
  padding: 0 15px;
}
</style>


