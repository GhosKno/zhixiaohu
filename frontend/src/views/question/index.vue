<template>
  <div>
    <div class="header">
        <div class="content">
          <div class="description">
              <div class="topics">
              <a href="/" class="Tag" v-for="topic in question.topics" :key="topic">{{topic}}</a>
              </div>
              <h1 class="title">
                  {{question.title}}
              </h1>
              <div class="summary">
                  {{question.summary}}
                  <Button type="text" class="read-all">显示全部 <Icon type="chevron-down"></Icon></Button>
              </div>
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
                      398,231
                  </div>
              </div>
          </div>

        </div>
        <div class="footer">
        <ToolBar :question="true"></ToolBar>
        </div>
    </div>
    <div class="main">
      <div class="answer-flow  card">
        <div class="topbar">
            <div class="title">
                {{numOfAnswer}} 个回答
            </div>
            <Select v-model="model1" style="float: right;width:200px" value="default">
                <Option v-for="item in answerSort" :value="item.value" :key="item.value">{{ item.label }}</Option>
            </Select>
        </div>
      <AnswerCard class="answer">
      </AnswerCard>
      <AnswerCard class="answer card"
        v-for="(item, index) in answerList"
        :key="index"
        :avatar="item.avatar"
        :name="item.name" 
        :pk="item.pk" 
        :feed-title="item.feedTitle" 
        :question="item.question" 
        :answer="item.answer">

      </AnswerCard>
      </div>
    </div>
  </div>
</template>

<script>
const AnswerCard = resolve =>
  require(["@/components/answerCard"], resolve);
const ToolBar = resolve => require(["@/components/toolBar"], resolve);
import cookieManage from "@/mixins/cookieManage";
import initInfo from "@/mixins/initInfo";
export default {
  name: "QuestionPage",
  mixins: [cookieManage, initInfo],
  components: { AnswerCard, ToolBar },
  data() {
    return {
      windowHeight: "",
      answerList: [
        {
          avatar: "h",
          name: "ccc",
          pk: "",
          feedTitle: "热门内容,来自: 历史",
          question: "历史上外交时有哪些尴尬场面？",
          answer:
            "南海仲裁案之后，2016年7月16日，在美国国务院记者会上，凤凰卫视记者王冰汝向美国国务院发言人马克·托纳提问：“新加坡国立大学国际法中心在网站上刊登了地图和地名词典，其中一份地图，它的来源是美国政府，而且这张地图上写的是太平岛，而不是太平礁，这跟南海仲裁案“仲裁”结果不..."
        }
      ],
      comments: [
        { id: 0, author: "失豆", time: "2 天前", text: "心疼 好可怕", zan: 12 },
        { id: 1, author: "橘子超人", time: "1 天前", text: "呵呵", zan: 0 },
        { id: 2, author: "想乖乖写代码的喵", time: "1 天前", text: "超吓人的啊", zan: 2 }
      ],
      showCommentBtn: false,
      question: {
        title: "作为一名程序员，我这属于什么水平？",
        summary:
          "已开源，源码URL请往下翻，剧情要反转了！ 不明真相的群众，请看帖子详细编辑过程。 野生的程序员们，这次我斗胆站出来，为你们呐喊。 是否像我这样迷惘过？ 没…",
        topics: ['IT','程序员','C(编程语言)','C++'],
      },
      numOfAnswer: 12,
      answerSort: [
          {
              value: 'default',
              label: '按默认排序'
          },
          {
              value: 'time',
              label: '按时间排序'
          }
      ],
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
    }
  },
  created() {

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
.content {
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
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
  width: 1000px;
  height: 100%;
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
.read-all {
  height: auto;
  padding: 0;
  line-height: inherit;
  background-color: transparent;
  border: none;
  border-radius: 0;
  color: #8590a6;
}
.summary{
    cursor: pointer;
    margin-bottom: 10px;
}
.summary:hover{
    opacity: 0.8;
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
      width: 694px;
    padding-bottom: 20px;
}
</style>
