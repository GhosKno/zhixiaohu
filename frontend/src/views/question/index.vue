<template>
  <div>
    <NotFoundPage v-if="noFound"></NotFoundPage>
    <ErrPage v-else-if="err" :errCode="errCode" :errText="errText"></ErrPage>
    <div v-else>
      <TopBar class="top-bar"></TopBar>
    <div class="header">
        <div class="content">
          <div class="description">
              <div class="topics">
              <a href="/" class="Tag" v-for="topic in question.topics" :key="topic.id">{{topic.label}}</a>
              </div>
              <h1 class="title">
                  {{question.title}}
              </h1>
          </div>
          <div class="countBoard">
              <a type="text" class="countItem">
                  <div class="countName">
                      关注者
                  </div>
                  <div class="countNum">
                      123
                  </div>
              </a>

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
          :forQuestion="true" ></TextWithToolBar>
        </div>
    </div>
    <div class="main">
      <div class="answer-flow card">
        <div class="topbar">
            <div class="title">
                {{numOfAnswer}} 个回答
            </div>
            <Select style="float: right;width:100px" placeholder="默认排序">
                <Option v-for="item in answerSort" :value="item.value" :key="item.value">{{ item.label }}</Option>
            </Select>
        </div>
        <AnswerCard>
        </AnswerCard>
        <AnswerCard
          v-for="(item, index) in answerList"
          :key="index"
          :avatar="item.avatar"
          :name="item.name" 
          :pk="item.pk" 
          :feed-title="item.feedTitle"
          :answer="item.answer">

        </AnswerCard>
      </div>
      <SideBar class="sidebar"></SideBar>
    </div>
    </div>
    
  </div>
</template>

<script>
const AnswerCard = resolve =>
  require(["@/components/answerCard"], resolve);
const TextWithToolBar = resolve => require(["@/components/textWithToolBar"], resolve);
const SideBar = resolve => require(["@/components/sideBar"], resolve);
const TopBar = resolve => require(['@/components/topBar'], resolve)
const NotFoundPage = resolve => require(['@/views/errors/404'], resolve)
const ErrPage = resolve => require(['@/views/errors/err'], resolve)

import cookieManage from "@/mixins/cookieManage";
import initInfo from "@/mixins/initInfo";
export default {
  name: "QuestionPage",
  mixins: [cookieManage, initInfo],
  components: { AnswerCard,NotFoundPage,ErrPage, TopBar, TextWithToolBar, SideBar },
  data() {
    return {
      windowHeight: "",
      answerList: [
        {
          answer:
            "垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵垃圾呵呵"
        }
      ],
      comments: [
        { id: 0, author: "失豆", time: "2 天前", text: "心疼 好可怕", zan: 12 },
        { id: 1, author: "橘子超人", time: "1 天前", text: "呵呵", zan: 0 },
        { id: 2, author: "想乖乖写代码的喵", time: "1 天前", text: "超吓人的啊", zan: 2 }
      ],
      question: {
        "author": 1,
        "id": 1,
        "add_time": "2018-01-07T12:24:03.872424Z",
        "title": "???",
        "detail": "...",
        "topics": [
            {
                "id": 1,
                "label": "hhh",
                "introduction": "xxx"
            }
        ],
        "visit_count": 1,
        "is_watch": false
      },
      numOfAnswer: 12,
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
    fetchData: function(){
      this.$http.get(`/api/questions/${this.$route.params.id}/`)
          .then(res => {
            if(res.body.success==true) {
              this.question=res.body.data
            } else {
              this.noFound=true
            }
          }, function(response){
            // 响应错误回调 
             this.err=true
             this.errCode=response.status
             this.errText=response.statusText
          });
      this.$http.get(`/api/questions/${this.$route.params.id}/get_answers/`)
          .then(res => {
            if(res.body.success==true) {
              this.answerList=res.body.data.results
              this.numOfAnswer=res.body.data.count
            } else {
              this.$Message.error(res.body.msg);
            }
          }, function(response){
            // 响应错误回调 
             this.err=true
             this.errCode=response.status
             this.errText=response.statusText
          });
          
    }
  },
  mounted() {
      this.fetchData()
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
</style>
