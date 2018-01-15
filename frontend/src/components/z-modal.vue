<template lang="pug">
  Modal(
    v-model="showModal"
    :loading="loading"
    :title="title"
    :width="width"
    @on-ok="submitModal"
    @on-cancel="cancelModal"
  )
    slot(name="body")
</template>

<script>
export default {
  name: 'zModal',
  props: {
    action: {
      type: String,
      required: true
    },
    width: {
      type: Number,
      default: 60
    },
    onSuccess: {
      type: Function,
      default: undefined
    },
    params: {
      type: Object,
      required: true
    },
    successMsg: {
      type: String,
      default: undefined
    },
    title: {
      type: String,
      default: ''
    },
    validated: {
      type: Boolean,
      required: true
    }
  },
  data () {
    return {
      showModal: false,
      loading: true
    }
  },
  methods: {
    open () {
      this.showModal = true
    },
    submitModal () {
      if (!this.validated) {
        this.$Message.warning('请完整填写所有内容')
        setTimeout(() => {
          this.loading = false;
          this.$nextTick(() => {
              this.loading = true;
          });
        }, 0);
        return
      }
      if (this.action) {
        this.loading = true
        this.$http.post(this.action, this.params)
          .then(res => {
            if (!res.body.success) {
              this.$Message.error(res.body.msg)
            } else {
              if (this.onSuccess && typeof this.onSuccess == 'function') {
                this.onSuccess(res)
              }
              if (this.successMsg && typeof this.successMsg == 'string') {
                this.$Message.success(this.successMsg)
              }
              this.showModal = false
            }
            this.$nextTick(() => {
              this.loading = false
            });
          }, res => {
            this.$Message.error('error occur!')
            setTimeout(() => {
              this.loading = false;
              this.$nextTick(() => {
                  this.loading = true;
              });
            }, 0);
          })
      } else {
        this.$Message.error('submit handle error!')
      }
    },
    cancelModal () {
      this.showModal = false
    }
  }
}
</script>


