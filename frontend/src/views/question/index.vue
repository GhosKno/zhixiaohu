<template>
  <div>
    <div class="header">
      <div class="content">
        <div class="description">
          <div class="topics">
          <a @click="$router.push({path:'/topic/'+topic.id})" class="Tag" v-for="topic in question.topics" :key="topic.id">{{topic.label}}</a>
          </div>
          <h1>
              <a @click="$router.push({path:'/question/'+question.id})" class="title">{{question.title}}</a>
          </h1>
        </div>
          <div class="countBoard">
            <div class="countItem">
              <div class="countName">
                  关注者
              </div>
              <div class="countNum">
                  {{question.watch_count}}
              </div>
            </div>
            <div class="countItem">
              <div class="countName">
                  浏览量
              </div>
              <div class="countNum">
                  {{question.visit_count}}
              </div>
            </div>
          </div>
          </div>
          <div class="footer">
          <TextWithToolBar 
            :text="question.detail" 
            :forQuestion="true"
            @writeAnswer="showEditor=true"
            @closeWriteAnswer="showEditor=false"
            @watch="question.watch_count++"
            @cancelWatch="question.watch_count--"
            :postTime="question.add_time"
            :pk="question.id"
            :isWatch="question.is_watch"
            :isOwner="$store.state.userid == question.author"
            :copyText="copyText"></TextWithToolBar>
      </div>
    </div>
    <div class="main">
      <div class="answer-flow">
        <AnswerEditor 
        class="answer-editor card" 
        v-if="showEditor" 
        @post="postAnswer"></AnswerEditor>
        <router-view 
        @err="$emit('err')" 
        :numOfAnswer="question.answer_count"
        @closeWriteAnswer="showEditor=false"></router-view>
      </div>
      <SideBar class="sidebar"></SideBar>
    </div>
  </div>
</template>

<script>
const TextWithToolBar = resolve =>
  require(["@/components/textWithToolBar"], resolve);
const SideBar = resolve => require(["@/components/sideBar"], resolve);
const AnswerEditor = resolve => require(["@/components/answerEditor"], resolve);
import api from "@/utils/api";

export default {
  name: "QuestionPage",
  components: {
    AnswerEditor,
    TextWithToolBar,
    SideBar
  },
  data() {
    return {
      question: {},
      comments: [],
      nextUrl: "",
      err: {},
      showEditor: false,
      answerForm: {},
      copyText: ""
    };
  },
  methods: {
    handleReachBottom() {
      return new Promise(resolve => {
        if (this.nextUrl == null || this.nextUrl.length == 0) {
          this.$Message.info("没有更多内容了");
          return resolve();
        }
        this.$http.get(this.transUrl(this.nextUrl)).then(res => {
          this.nextUrl = res.body.data.next;
          setTimeout(() => {
            this.answerList.push(...res.body.data.results);
            resolve();
          }, 1000);
        });
      });
    },
    fetchQuestion: function() {
      api.getQuestion(this.$route.params.q_id).then(
        res => {
          if (res.body.success == true) {
            this.question = res.body.data;
            document.title = this.question.title + " - 知小乎";
            this.copyText = document.title + " http://" +
              window.location.host +
              "/question/" +
              this.question.id;
          } else {
            this.$emit("err"); // 404
          }
        },
        err => {
          this.$emit("err", { code: err.status, text: err.statusText });
        }
      );
    },
    postAnswer: function(html) {
      this.answerForm.question = this.$route.params.q_id;
      this.answerForm.detail = html;
      api.postAnswer(this.answerForm).then(
        res => {
          if (res.body.success == true) {
            this.showEditor = false;
            this.$Message.success("回答成功");
            this.$router.push({path: '/question/'+this.$route.params.q_id+'/answer/'+res.body.data.id});
          } else {
            this.$Message.error(res.body.msg);
          }
        },
        err => {
          this.$Message.error(err.status + " " + err.statusText);
        }
      );
    }
  },
  mounted() {
    this.fetchQuestion();
  },
  watch: {
    $route(to, from) {
      this.fetchQuestion();
    }
  }
};
</script>

<style lang="less" scoped>
.header {
  padding: 16px 0;
  position: relative;
  min-width: 1032px;
  overflow: hidden;
  background: #fff;
  -webkit-box-shadow: 0 1px 3px 0 rgba(0, 37, 55, 0.1);
  box-shadow: 0 1px 3px 0 rgba(0, 37, 55, 0.1);
  .title {
    cursor: pointer;
    color: #1e1e1e;
  }
  .title:hover {
    color: #0032bb;
  }
}
.content,
.main {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
  width: 1000px;
  height: 100%;
  margin: 10px auto;
}
.main{
  margin-bottom: 20px;
}
.answer-flow {
  width: 696px;
}
.sidebar {
  width: 280px;
}
.footer {
  width: 1000px;
  margin: 0 auto;
}
.countItem {
  display: inline-block;
  padding: 0 8px;
  text-align: center;
  line-height: 1.6;
}
.countItem + .countItem {
  border-left: 1px solid #e7eaf1;
}
.countName {
  font-size: 14px;
  color: #8590a6;
}
.countNum {
  margin-top: 4px;
  display: inline-block;
  font-size: 18px;
  color: #262626;
  font-weight: 600;
  font-synthesis: style;
}
.description {
  width: 640px;
}
.detail {
  margin-bottom: 10px;
}
.Tag {
  margin: 3px 5px 3px 0;
  position: relative;
  display: inline-block;
  height: 30px;
  padding: 3px 12px;
  color: #3e7ac2;
  background: #eef4fa;
  border-radius: 100px;
}
.answer-editor {
  width: 696px;
  margin-bottom: 12px;
}
.question {
  .ivu-scroll-loader:first-child {
    background: #fff;
  }
}
</style>