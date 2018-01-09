<template>
  <div class="questionCard">
    <div class="header">
      <span @click="toQuestionDetail()">{{title}}</span>
    </div>
    <div class="info">
      <span>{{(new Date(time)).toISOString().split('T')[0]}}</span>
      <span>{{answers}}个回答</span>
      <span>{{watchers}}个关注</span>
      <Button type="ghost" @click="toQuestionDetail()">去写回答</Button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'questionCard',
  data () {
    return {}
  },
  props: {
    title: {
      type: String,
      required: true
    },
    time: {
      type: String,
      required: true
    },
    answers: {
      type: Number,
      required: true
    },
    watchers: {
      type: Number,
      required: true
    },
    url: {
      type: String,
      //todo
      default: '/home'
    },
    id: {
      type: Number,
      default: 0
    }
  },
  methods: {
    toQuestionDetail() {
      this.$router.push({path: `/question/${this.id}`})
    }
  }
}
</script>

<style lang="less" scoped>
.questionCard{ 
  border-bottom: 1px #dddee1 solid;
  padding: 15px 30px;
  .header {
    font-size: 1.5em;
    font-weight: bold;
    span {
      cursor: pointer;
    }
    span:hover{
      color: #175199;
    }
  }

  .info {
    // margin-top: 5px;
    span {
      color: #8590a6;
    }
    span:not(:first-child):before {
      margin: 0 5px;
      content: "\B7";
    }
    button {
      // position: absolute;
      margin-left: 50px;
    }
  }
}
</style>

