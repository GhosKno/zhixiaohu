<template>
<div class="layout">
    <div class="title">关于 {{$route.query.query}} 的搜索结果：</div>
    <Tabs :animated="false">
        <TabPane class="panel" :label="'问题('+QuestionCount+')'" icon="chatbox-working">
            <div
            class="question-card card"
            v-for="(ques, index) in Questions"
            :key="index">
                <a class="title" @click="$router.push({path:'/question/' + ques.id})">
                <Icon type="android-hangout" color="#3e7ac2" v-if="ques.answer_count>5"></Icon>
                {{ques.title}}
                  <span class="time"> 提问于{{timeago(ques.add_time)}}</span>
                  <span class="answer-count">{{ques.answer_count}} 个回答</span>
                </a>
                <div class="content" v-html="getContent(ques.detail)"></div>
            </div>
            <Page class="pagination" :total="QuestionCount" @on-change="searchQuestion"></Page>
        </TabPane>

        <TabPane class="panel" :label="'回答('+AnswerCount+')'" icon="chatbubbles">
            <AnswerCard
              v-for="(ans, index) in Answers"
              :key="index"
              :answer="ans">
            </AnswerCard>
            <Page class="pagination" :total="AnswerCount" @on-change="searchAnswer"></Page>
        </TabPane>

        <TabPane class="panel" :label="'话题('+TopicCount+')'" icon="pound">
          <div
            class="topic-card"
            v-for="(tp, index) in Topics"
            :key="index" @click="$router.push({path:'/topic/' + tp.id})">
            <span class="tag">{{tp.label}}</span>
            <span class="intro">{{(tp.introduction.substring(0, 70))}}</span>
          </div>
          <Page class="pagination" :total="TopicCount" @on-change="searchTopic"></Page>
        </TabPane>
        <TabPane class="panel" :label="'用户('+ProfileCount+')'" icon="person-stalker">
          <div
            class="user-card card"
            v-for="(user, index) in Profiles"
            :key="index" @click="$router.push({path:'/profile/' + user.id})">
            <Avatar size="large" :src="user.avatar"></Avatar>
          <span class="name">{{user.nickname}}</span>
          <span class="intro">{{user.description}}</span>
          </div>
          <Page class="pagination" :total="ProfileCount" @on-change="searchProfile"></Page>
        
        </TabPane>
    </Tabs>
       
    
</div>
  
</template>

<script>
const AnswerCard = resolve =>
  require(["@/components/answerCard"], resolve);
import api from "@/utils/api";
import common from "@/utils/common";

export default {
  name: "searchPage",
  data() {
    return {
      Questions: [],
      Answers: [],
      Topics: [],
      Profiles: [],
      SearchQuery: "",
      QuestionCount: 0,
      AnswerCount: 0,
      TopicCount: 0,
      ProfileCount: 0
    };
  },
  components: { AnswerCard },
  methods: {
    searchQuestion(page = 0) {
      api.searchQuestion(this.SearchQuery, page).then(
        res => {
          if (res.body.success) {
            this.Questions = res.body.data.results;
            this.QuestionCount = res.body.data.count;
          } else {
            this.$Message.error(res.body.msg);
          }
        },
        err => {
          this.$Message.error(err.status + " " + api.errInfo[err.status]);
        }
      );
    },
    searchAnswer(page = 0) {
      api.searchAnswers(this.SearchQuery, page).then(
        res => {
          if (res.body.success) {
            this.Answers = res.body.data.results;
            this.AnswerCount = res.body.data.count;
          } else {
            this.$Message.error(res.body.msg);
          }
        },
        err => {
          this.$Message.error(err.status + " " + api.errInfo[err.status]);
        }
      );
    },
    searchTopic(page = 0) {
      api.searchTopics(this.SearchQuery, page).then(
        res => {
          if (res.body.success) {
            this.Topics = res.body.data.results;
            this.TopicCount = res.body.data.count;
          } else {
            this.$Message.error(res.body.msg);
          }
        },
        err => {
          this.$Message.error(err.status + " " + api.errInfo[err.status]);
        }
      );
    },
    searchProfile(page = 0) {
      api.searchProfile(this.SearchQuery, page).then(
        res => {
          if (res.body.success) {
            this.Profiles = res.body.data.results;
            this.ProfileCount = res.body.data.count;
          } else {
            this.$Message.error(res.body.msg);
          }
        },
        err => {
          this.$Message.error(err.status + " " + api.errInfo[err.status]);
        }
      );
    },
    search() {
      this.SearchQuery = this.$route.query.query;
      if (this.SearchQuery == "") {
        this.$emit("err");
        return;
      }
      this.searchQuestion();
      this.searchAnswer();
      this.searchTopic();
      this.searchProfile();
    },
    getContent(html) {
      const MaxLen=110;
      return common.getContent(html, MaxLen);
    }
  },
  mounted() {
    this.search();
  },
  watch: {
    $route(to, from) {
      this.search();
    }
  }
};
</script>

<style lang="less" scoped>
.layout {
  width: 1000px;
  margin: 10px auto;
  background: #fff;
  padding: 20px;
  .title {
    font-size: 16px;
    font-weight: 500;
  }
  .panel {
    padding: 10px;
  }
  .question-card {
    margin: 10px 0;
    padding: 15px;
    .title {
      font-weight: 600;
      font-size: 20px;
      color: #1e1e1e;
    }
    .title::after {
      display: block;
      margin: 5px 0;
      border-bottom: 1px solid #f0f2f7;
      content: "";
    }
    .time {
      color: #8590a6;
      font-weight: normal;
      font-size: 13px;
    }
    .answer-count {
      float: right;
      font-size: 12px;
      color: #8590a6;
    }
    .content {
      overflow: hidden;
      text-overflow: ellipsis;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      -webkit-line-clamp: 3;
      width: 100%;
      height: auto;
      max-height: 73px;
    }
  }
  .intro {
    font-size: 14px;
    color: #8590a6;
  }
  .topic-card {
    padding: 10px 5px;
    cursor: pointer;
    &:hover{
      background: #f8fafd;
    }
    .tag {
      padding: 5px 10px;
      color: #3e7ac2;
      background: #eef4fa;
      border-radius: 100px;
    }
  }
  .user-card {
    padding: 10px;
    margin: 10px 0;
    cursor: pointer;
    .name{
      margin: 0 5px;
      font-weight: 500;
    }
  }
  .card:hover {
    box-shadow: rgba(45, 45, 45, 0.05) 0px 2px 2px,
      rgba(49, 49, 49, 0.05) 0px 4px 4px, rgba(42, 42, 42, 0.05) 0px 8px 8px;
    transition: box-shadow 0.3s ease-out, transform 0.3s ease-out,
      opacity 0.2s ease-out;
    transition-delay: 0.1s;
  }
  .pagination{
    margin-top: 20px;
  }
}
</style>
