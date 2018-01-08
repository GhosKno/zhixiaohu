<template>
  <div class="message">
    <div slot="header" class="header">
      <p>我的消息</p>
    </div>
    <div class="message-body">
      <Scroll 
        :on-reach-bottom="handleReachBottom" 
        height="300">
        <div 
          v-for="(msg,index) in messages"
          :class="{'message-content': true, 'has-read': msg.has_read}"
          :key="index"
        >
          <span class="user">{{msg.author}}</span>
          <span class="text">回答了</span>
          <span class="question" @click="toQuestion(msg.answer,msg.id)">{{msg.question}}</span>
          <span class="time">{{msg.time}}</span>
        </div>
      </Scroll>
    </div>
    <Modal 
      v-model="showDetailModal" 
      width="800"
      :styles="{left: '20px', 'margin-left': '0px'}"
    >
      <AnswerListCard
        :avatar="currentAnswer.avatar"
        :name="currentAnswer.name"
        :pk="currentAnswer.pk"
        :feed-title="currentAnswer.feedTitle" 
        :coverImg="currentAnswer.coverImg"
        :question="currentAnswer.question" 
        :answer="currentAnswer.answer"
      >
      </AnswerListCard>
    </Modal>
  </div>
</template>

<script>
const AnswerListCard = resolve =>
  require(["@/components/answerListCard"], resolve);
export default {
  name: 'message',
  data () {
    return {
      messages:[],
      nextUrl: '',
      showDetailModal: false,
      currentAnswer: ''
    }
  },
  components: {
    AnswerListCard
  },
  methods: {
    getMessages() {
      this.$http.get('/api/users/messages/')
        .then(res => {
          this.messages = res.body.data.results
          this.nextUrl = res.body.data.next
        })
    },
    open() {
      this.getMessages()
    },
    toQuestion(answerUrl, id) {
      this.$http.get(`/api/messages/${id}/readed/`)
      this.$http.get(answerUrl)
        .then(res => {
          this.currentAnswer = res.body.data
        })
          this.showDetailModal = true
    },
    handleReachBottom() {
      return new Promise(resolve => {
        if(this.nextUrl) {
          this.$http.get('/api/users/messages/')
            .then(res => {
              this.messages.push(...(res.body.data.results))
              this.nextUrl = res.body.data.next
            })
        }
        setTimeout(() => {
          resolve()
        }, 2000)
      })
    }
  },
  created () {
  }
}
</script>

<style lang="less" scoped>
  .ivu-modal{
    left:20px !important;
    margin:0 !important;
  }
  .header {
    p{
      text-align: center;
      font-size: 1.5em;
      font-weight: bold;
    }
  }
  .message-body {
    ::-webkit-scrollbar {
      display:none;
    }
    .message-content{
      height: 40px;
      font-size: 15px;
      padding: 5px 0px;
      width: 95%;
      margin: 0 auto;
      border-bottom: 1px #dddee1 solid;
      .user, .question{
        color: #3e7ac2;
      }
      .text {
        margin: 0 5px;
      }
      .question {
        cursor: pointer;
      }
      .time {
        right: 5px;
        position: absolute;
      }
    }
  }
</style>
