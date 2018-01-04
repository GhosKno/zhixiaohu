<template>
  <div class="questionCard">
    <div class="header">
      <span @click="toQuestionDetail()">{{title}}</span>
    </div>
    <div class="info">
      <span>{{time}}</span>
      <span>{{answers}}个回答</span>
      <span>{{watchers}}个关注</span>
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
    }
  },
  methods: {
    toQuestionDetail() {
      //todo router to question detail page
    }
  }
}
</script>

<style lang="less" scoped>
.questionCard{ 
  border-bottom: 1px #dddee1 solid;
  padding: 15px 5px;
  .header {
    font-size: 1.3em;
    font-weight: bold;
    span {
      cursor: pointer;
    }
    span:hover{
      color: #175199;
    }
  }

  .info {
    margin-top: 5px;
    span {
      color: #8590a6
    }
    span:not(:first-child):before {
      margin: 0 5px;
      content: "\B7";
    }
  }
}
</style>

