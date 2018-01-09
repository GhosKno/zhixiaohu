<template>
  <div>
    <div v-if="loading"></div>
    <NotFoundPage v-else-if="noFound"></NotFoundPage>
    <ErrPage v-else-if="err" :errCode="errCode" :errText="errText"></ErrPage>
    <div v-else>
      <TopBar class="top-bar"></TopBar>
      <div class="header">
          <div class="content">
            <div class="description">
                <div class="topics">
                <a :href="`/topic/${topic.id}`" class="Tag" v-for="topic in question.topics" :key="topic.id">{{topic.label}}</a>
                </div>
                <h1 class="title">
                    {{question.title}}
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
            @writeAnswer="showEditor=!showEditor"
            @watch="question.watch_count++"
            @cancelWatch="question.watch_count--"
            :postTime="question.add_time"
            :pk="$route.params.id"
            :isWatch="question.is_watch"
            :isOwner="$store.state.userid == question.author"
           ></TextWithToolBar>
          </div>
      </div>
      <div class="main">
        <div class="answer-flow">
          <AnswerEditor class="answer-editor card" v-if="showEditor" :pk="$route.params.id"></AnswerEditor>    
          <div class="card">
            <div class="topbar">
                <div class="title">
                    {{answerCount}} 个回答
                </div>
                <Select style="float: right;width:100px" placeholder="默认排序">
                    <Option v-for="item in answerSort" :value="item.value" :key="item.value">{{ item.label }}</Option>
                </Select>
            </div>
            <AnswerCard
              v-for="(item, index) in answerList"
              :key="index"
              :answer="item">
            </AnswerCard>
          </div>
        </div>
        <SideBar class="sidebar"></SideBar>
      </div>
    </div>
    </div>
</template>

<script>
const NotFoundPage = resolve => require(['@/views/errors/404'], resolve)
const ErrPage = resolve => require(['@/views/errors/err'], resolve)
const AnswerCard = resolve =>
  require(["@/components/answerCard"], resolve);
const TextWithToolBar = resolve => require(["@/components/textWithToolBar"], resolve);
const SideBar = resolve => require(["@/components/sideBar"], resolve);
const TopBar = resolve => require(['@/components/topBar'], resolve);
const AnswerEditor = resolve => require(['@/components/answerEditor'], resolve);
import cookieManage from "@/mixins/cookieManage";
import initInfo from "@/mixins/initInfo";
export default {
  name: "QuestionPage",
  mixins: [cookieManage, initInfo],
  components: { AnswerCard,AnswerEditor,NotFoundPage,ErrPage, TopBar, TextWithToolBar, SideBar },
  data() {
    return {
      windowHeight: "",
      question: {},
      answerCount: {},
      answerList: [],
      comments: [],
      answerSort: [
          {
              value: 'default',
              label: '默认排序'
          },
          {
              value: 'time',
              label: '按时间排序'
          }
      ],
      noFound: false,
      err: false,
      errText: "",
      errCode: 0,
      loading: true,
      showEditor: false,
    };
  },
  methods: {
    handleReachBottom() {
      return new Promise(resolve => {
        setTimeout(() => {
          this.answerList.push(...this.answerList);
          resolve();
        }, 2000);
      });
    },
    fetchQuestion: function(){
      this.$http.get(`/api/questions/${this.$route.params.id}/`)
          .then(res => {
            if(res.body.success==true) {
              this.question=res.body.data
              document.title=this.question.title+' - 知小乎'
              this.fetchAnswer()
            } else {
              this.noFound=true
            }
          }, function(response){
            // 响应错误回调 
             this.err=true
             this.errCode=response.status
             this.errText=response.statusText
          });
          this.loading=false
    },
    fetchAnswer: function(){
      this.$http.get(`/api/questions/${this.$route.params.id}/get_answers/`)
          .then(res => {
            if(res.body.success==true) {
              this.answerList=res.body.data.results
              this.answerCount=res.body.data.count
            } else {
              this.$Message.error(res.body.msg);
            }
          }, function(response){
            // 响应错误回调 
             this.err=true
             this.errCode=response.status
             this.errText=response.statusText
          });
    },
    
  },
  mounted() {
      this.fetchQuestion()
  }
};
</script>

<style scoped>
.topbar {
  background: #fff;
  border-bottom: 1px solid #f0f2f7;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  height: 50px;
  padding: 0 20px;
}
.topbar .title {
  display: inline-block;
  font-size: 15px;
  font-weight: 600;
  font-synthesis: style;
  color: #1e1e1e;
}

.header {
  padding: 16px 0;
  position: relative;
  min-width: 1032px;
  overflow: hidden;
  background: #fff;
  -webkit-box-shadow: 0 1px 3px 0 rgba(0, 37, 55, 0.1);
  box-shadow: 0 1px 3px 0 rgba(0, 37, 55, 0.1);
}
.content,.main {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
  width: 1000px;
  height: 100%;
  padding: 0 16px;
  margin: 0 auto;
}

.answer-flow{
  width: 696px;
}
.sidebar{
  width:257px;
}
.title {
  margin-top: 12px;
  margin-bottom: 4px;
  font-size: 22px;
  font-weight: 600;
  font-synthesis: style;
  line-height: 32px;
  color: #1e1e1e;
}
.footer {
  width: 1000px;
  padding: 0 16px;
  margin: 0 auto;
}
.countItem{
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
.detail{
    margin-bottom: 10px;
}
.Tag{
    margin: 3px 5px 3px 0;
    vertical-align: middle;
    position: relative;
    display: inline-block;
    height: 30px;
    padding: 0 12px;
    font-size: 14px;
    line-height: 30px;
    color: #3e7ac2;
    vertical-align: top;
    background: #eef4fa;
    border-radius: 100px;
}
.main{
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    justify-content: space-between;
    -webkit-box-align: start;
    -ms-flex-align: start;
    align-items: flex-start;
    margin: 10px auto;
    padding: 0 16px;
    width: 1000px;
    min-height: 100vh;
}
.answer{
  position: relative;
  padding: 5px 18px;
  margin-top: 10px;
  width: 694px;
}
.answer+.answer:after {
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    margin: 0 20px;
    display: block;
    border-bottom: 1px solid #f0f2f7;
    content: "";
}
.answer-editor{
 width: 696px;
 margin-bottom: 12px;
}
</style>
