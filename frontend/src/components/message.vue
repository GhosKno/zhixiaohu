<template>
  <div class="message">
    <div slot="header" class="header">
      <p>我的消息</p>
    </div>
    <div class="message-body">
      <Scroll 
        :on-reach-bottom="handleReachBottom" 
        height="300">
        <div class="no-data-content" v-if="messages.length == 0">
          还没有消息
        </div>
        <div 
          v-for="(msg,index) in messages"
          :class="{'message-content': true, 'has-read': msg.has_read}"
          :key="index"
        >
          <span class="user">{{msg.author}}</span>
          <span class="text">回答了</span>
          <span class="question" @click="toQuestion(msg.question.id,msg.answer,msg.id)">
            {{msg.question.title.slice(0,30)}}
          </span>
          <!-- <span class="time">{{msg.time}}</span> -->
        </div>
      </Scroll>
    </div>
  </div>
</template>

<script>
import api from "@/utils/api";

export default {
  name: "message",
  data() {
    return {
      messages: [],
      nextUrl: "",
      currentAnswer: ""
    };
  },
  methods: {
    open() {
      api.getMessages().then(res => {
        this.messages = res.body.data.results;
        this.nextUrl = res.body.data.next;
      });
    },
    toQuestion(questionid, answerid, id) {
      api.markRead(id).then(res => {
        if(res.body.success){
          this.$emit('readed')
        }
        // TODO: handle err
      });
      this.$router.push({path: `/question/${questionid}/answer/${answerid}`})
    },
    handleReachBottom() {
      return new Promise(resolve => {
        if (this.nextUrl) {
          api.getMessages().then(res => {
            setTimeout(() => {
              this.messages.push(...res.body.data.results);
              resolve();
            }, 1000);
            this.nextUrl = res.body.data.next;
          });
        }
      });
    }
  },
  created() {}
};
</script>

<style lang="less" scoped>
.ivu-modal {
  left: 20px !important;
  margin: 0 !important;
}
.header {
  p {
    text-align: center;
    font-size: 1.5em;
    font-weight: bold;
  }
}
.message-body {
  ::-webkit-scrollbar {
    display: none;
  }
  .no-data-content {
    font-size: 15px;
    color: #8590a6;
    text-align: center;
    padding-top: 100px;
  }
  .message-content {
    // height: 40px;
    font-size: 15px;
    padding: 5px 0px;
    width: 95%;
    margin: 0 auto;
    border-bottom: 1px #dddee1 solid;
    overflow: hidden;
      white-space: nowrap;
  text-overflow: ellipsis;
    .user,
    .question {
      color: #3e7ac2;
    }
    .text {
      margin: 0 3px;
    }
    .question {
      cursor: pointer;
    }
    // span{word-break:normal; width:auto; display:block; white-space:pre-wrap;word-wrap : break-word ;overflow: hidden ;}
    .time {
      color: #8590a6;
      display: block;
      text-align: end;
    }
  }
}
.has-read {
  color: #8590a6 !important;
  .user,
  .question {
    color: #8590a6 !important;
  }
}
</style>
