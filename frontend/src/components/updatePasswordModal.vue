<template>
  <z-modal
    action="/"
    :onSuccess="settingHandle()"
    :params="passwordForm"
    successMsg="成功修改密码"
    title="修改密码"
    :validated="true"
    ref="updatePwd"
    :width='30'
  >
  <div slot="body">
    <Form ref="pwdForm" :rules="updateRule" :model="passwordForm">
      <FormItem prop="oldPassword" label="旧密码">
        <Input type="password" v-model="passwordForm.oldPassword" placeholder="请输入新密码"/>
      </FormItem>
      <FormItem prop="password" label="新密码">
        <Input type="password" v-model="passwordForm.password" placeholder="请输入新密码"/>
      </FormItem>
      <FormItem prop="checkPassword" label="确认密码">
        <Input type="password" v-model="passwordForm.checkPassword" placeholder="请再次输入密码"/>
      </FormItem>
    </Form>
  </div>
  </z-modal>
</template>

<script>
const ZModal = resolve => require(['@/components/z-modal'], resolve)
export default {
  name: 'updatePassword',
  data () {
    const validatePassCheck = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次完整输入新密码'))
      } else if (value !== this.passwordForm.password) {
        callback(new Error('两次密码不一致！'))
      } else {
        callback()
      }
    }
    return {
      passwordForm: {
        oldPassword:'',
        password: '',
        checkPassword: '',
      },
      updateRule: {
        oldPassword: [
          { required: true, message: '请完整输入旧的密码', trigger: 'blur' },
          { type: 'string', min: 6, message: '密码长度不能小于六位', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请完整输入新密码', trigger: 'blur' },
          { type: 'string', min: 6, message: '密码长度不能小于六位', trigger: 'blur' }
        ],
        checkPassword: [
          { required: true, message: '请再次完整输入新密码', trigger: 'blur' },
          { validator: validatePassCheck, trigger: 'blur' }
        ],
      }
    }
  },
  components: {
    ZModal
  },
  methods: {
    settingHandle() {

    },
    open() {
      this.$refs['updatePwd'].open()
    }
  }
}

</script>
