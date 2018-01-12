<template>
  <div>
		<Scroll :on-reach-bottom="handleReachBottom" :height="windowHeight">
		  <div class="container">
				<div class="main">
          <div class="card sub-menu-bar">
            <Button type="text" class="sub-menu-btn" @click="$refs['questionModal'].open()">
                <svg class="icon" >
                    <use xlink:href="#ask"></use>
                </svg>
                提问
            </Button>
            <Button type="text" class="sub-menu-btn" @click="handleShowQuestion()">
                <svg class="icon" >
                    <use xlink:href="#answer"></use>
                </svg>
                {{showQuestion?'围观':'回答'}}
            </Button>
            <Button type="text" class="sub-menu-btn" @click="$Notice.info({desc:'提问里也可以写文章哦（此功能待开发..(๑•ᴗ•๑)'})">
                <svg class="icon" >
                    <use xlink:href="#write"></use>
                </svg>
                写文章
            </Button>
            <Button type="text" class="sub-menu-btn btn-right" @click="$Notice.info({desc:'草稿箱为空（此功能待开发..(๑•ᴗ•๑)'})">
                草稿
            </Button>
            <QuestionModal ref="questionModal"></QuestionModal>
        </div>
          <div class="section">
            <div v-if="showQuestion">
            <QuestionCard
              class="question-card card"
              v-for="(ques, index) in questionList"
              :key="index"
              :title="ques.title"
              :time="ques.add_time"
              :answers="ques.answer_count"
              :watchers="ques.watch_count"
              :id="ques.id"
            ></QuestionCard>
            </div>
            <div v-else>
            <AnswerListCard
              v-for="(ans, index) in answerList"
              :key="index"
              :answer="ans">
            </AnswerListCard>
            </div>
            <div style="color: #9eaad1;text-align: center;" v-if="emptyList">
              <div style="font-size: 70px;">щ(ﾟДﾟщ)!||<br/> 空无一物</div>
              _(:з」∠)_快去写点回答吧
            </div>
            <Spin size="large" fix v-if="loading"></Spin>
          </div>
		    </div>
				<SideBar class="sidebar"></SideBar>
			</div>
		</Scroll>
  </div>
</template>

<script>
const AnswerListCard = resolve =>
  require(["@/components/answerListCard"], resolve);
const SideBar = resolve => require(["@/components/sideBar"], resolve);
const QuestionModal = resolve =>
  require(["@/components/questionAskModal"], resolve);
const QuestionCard = resolve => require(["@/components/questionCard"], resolve);

import cookieManage from "@/mixins/cookieManage";
import initInfo from "@/mixins/initInfo";
import api from "@/utils/api";

export default {
  name: "home",
  mixins: [cookieManage, initInfo],
  components: { AnswerListCard, SideBar, QuestionModal, QuestionCard },
  data() {
    return {
      windowHeight: 900,
      answerList: [],
      questionList: [],
      nextUrl: "",
      emptyList: false,
      loading: true,
      showQuestion: false
    };
  },
  methods: {
    fetchAnswerList() {
      api.getAnswers().then(
        res => {
          if (res.body.success == true) {
            this.answerList = res.body.data.results;
            this.nextUrl = res.body.data.next;
          } else {
            this.$Message.error(res.body.msg);
          }
          this.loading = false;
        },
        res => {
          this.$Message.error(res.status + " " + res.statusText);
          this.loading = false;
        }
      );
    },
    handleReachBottom() {
      return new Promise(resolve => {
        if (this.nextUrl == null || this.nextUrl.length == 0) {
          this.$Message.info("没有更多的内容了");
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
    fetchQuestionList() {
      api.getQuestions().then(
        res => {
          if (res.body.success == true) {
            this.questionList = res.body.data.results;
            this.nextUrl = res.body.data.next;
          } else {
            this.$Message.error(res.body.msg);
          }
          this.loading = false;
        },
        res => {
          this.$Message.error(res.status + " " + res.statusText);
          this.loading = false;
        }
      );
    },
    handleShowQuestion() {
      if (this.showQuestion) {
        this.fetchAnswerList();
        this.showQuestion = false;
      } else {
        this.fetchQuestionList();
        this.showQuestion = true;
      }
    }
  },
  created() {
    this.fetchAnswerList();
  },
  watch: {
    loading() {
      if (!this.answerList.length) {
        this.emptyList = true;
      }
      if (this.answerList.length < 3) {
        this.windowHeight = window.innerHeight - 60;
      }
    }
  }
};
</script>

<style scoped>
.container {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: start;
  -ms-flex-align: start;
  align-items: flex-start;
  position: relative;
  width: 1000px;
  margin-top: 10px;
  margin: 10px auto;
}
.main {
  width: 679px;
}
.sub-menu-bar {
  line-height: 58px;
}
.sub-menu-btn {
  font-size: 16px;
  width: 100px;
  height: 58px;
}
.btn-right {
  font-weight: 600;
  color: #8590a6;
  float: right;
}
.icon {
  vertical-align: text-bottom;
  margin-bottom: -5px;
  width: 24px;
  height: 24px;
}
.question-card{
  margin: 5px 0;
}
.sidebar {
  width: 296px;
  padding: 0 16px;
}
</style>
