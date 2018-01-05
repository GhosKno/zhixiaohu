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
    <Form ref="pwdForm" :rules="updateRule">
      <FormItem prop="password" label="新密码">
        <Input v-model="passwordForm.password" placeholder="请输入新密码"></Input>
      </FormItem>
      <FormItem prop="checkPassword" label="确认密码">
        <Input v-model="passwordForm.checkPassword" placeholder="请再次输入密码"></Input>
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
        callback(new Error('Please enter your password again'))
      } else if (value !== this.regForm.password) {
        callback(new Error('The two input passwords do not match!'))
      } else {
        callback()
      }
    }
    return {
      passwordForm: {
        password: '',
        checkPassword: '',
      },
      updateRule: {
        password: [
          { required: true, message: 'Please fill in the password.', trigger: 'blur' },
          { type: 'string', min: 6, message: 'The password length cannot be less than 6 bits', trigger: 'blur' }
        ],
        checkPassword: [
          { required: true, message: 'Please fill in the password.', trigger: 'blur' },
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
