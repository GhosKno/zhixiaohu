<template>
  <div>
    <div class="topicDetail">
      <Row class="topic-header card">
        <div class="title">
          话题 「 {{topicTitle}} 」
        </div>
        <div class="introduction">
          介绍： {{introduction}}
        </div>
      </Row>
      <Row class="topic-body card">
        <div class="no-data-content" v-if="questions.length == 0">
          当前话题下还没有内容
        </div>
        <question-card
          v-for="(item, index) in questions"
          :key="index"
          :title="item.title"
          :time="item.add_time"
          :answers="item.answer_count"
          :watchers="item.watch_count"
          :id="item.id"
        ></question-card>
      </Row>
    </div>
  </div>
</template>

<script>
const questionCard = resolve => require(["@/components/questionCard"], resolve);
import api from "@/utils/api";

export default {
  name: "topicDetail",
  data() {
    return {
      questions: [],
      questionCount: "",
      nextUrl: "",
      topicTitle: "",
      introduction: ""
    };
  },
  components: {
    questionCard
  },
  methods: {
    getQuestions() {
      if (this.nextUrl == null) {
        this.$Message.info("没有更多的问题了");
        return;
      }
      let url =
        this.nextUrl.length == 0
          ? `/api/topics/${this.$route.params.id}/get_questions/`
          : this.nextUrl;
      this.$http.get(this.transUrl(url)).then(
        res => {
          if (res.body.success) {
            this.questions.push(...res.body.data.results);
            this.nextUrl = res.body.data.next;
            this.questionCount = res.body.data.count;
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
  created() {
    api.getTopic(this.$route.params.id).then(
      res => {
        if (res.body.success) {
          this.topicTitle = res.body.data.label;
          this.introduction = res.body.data.introduction;
        } else {
          this.$Message.error(res.body.msg);
        }
      },
      err => {
        this.$Message.error(err.status + " " + err.statusText);
      }
    );
    this.getQuestions();
  }
};
</script>

<style lang="less" scoped>
.topicDetail {
  top: 20px;
  min-height: 500px;
  width: 60%;
  margin: 0 auto;
  position: relative;
  .topic-header,
  .topic-body {
    padding: 16px 20px;
    padding-left: 50px;
    margin-bottom: 10px;
  }
  .topic-header {
    .title {
      font-size: 22px;
      font-weight: 600;
    }
    .introduction {
      line-height: 26px;
      font-size: 15px;
      color: #555;
    }
  }
  .topic-body {
    margin-top: 20px;
    min-height: 300px;
  }
}
.no-data-content {
  height: 200px;
  font-size: 15px;
  color: #8590a6;
  text-align: center;
  padding-top: 100px;
}
</style>

