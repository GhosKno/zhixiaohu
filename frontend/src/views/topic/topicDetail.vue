<template>
  <div>
    <TopBar class="top-bar"></TopBar>
    <div class="topicDetail">
      <Row class="topic-header">
        <div class="title">
          {{topicTitle}}
        </div>
        <div class="introduction">
          {{introduction}}
        </div>
      </Row>
      <Row class="topic-body">
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
const TopBar = resolve => require(['@/components/topBar'], resolve)
const questionCard = resolve => require(['@/components/questionCard'], resolve)
export default {
  name: 'topicDetail',
  data () {
    return {
      questions: [],
      questionCount:'',
      nextUrl: '',
      topicTitle: '',
      introduction: ''
    }
  },
  components: {
    questionCard,
    TopBar
  },
  methods: {
    getQuestions () {
      if(this.nextUrl == null){
        this.$Message.info('没有更多的问题了')
        return
      }
      let url = (this.nextUrl.length == 0) ? `/api/topics/${this.$route.params.id}/get_questions/` : this.nextUrl
      this.$http.get(url).then(res => {
        this.questions.push(...(res.body.data.results))
        this.nextUrl = res.body.data.next
        this.questionCount = res.body.data.count
      })
    }
  },
  created () {
    this.$http.get(`/api/topics/${this.$route.params.id}/`)
      .then(res => {
        this.topicTitle = res.body.data.label
        this.introduction = res.body.data.introduction
      })
    this.getQuestions()
  }
}
</script>

<style lang="less" scoped>
.topicDetail {
  top: 20px;
  min-height: 500px;
  width: 60%;
  margin: 0 auto;
  position: relative;
  .topic-header, .topic-body {
    background: #fff;
    padding: 16px 20px;
    padding-left: 50px;
    margin-bottom: 10px;
    border-radius: 2px;
    -webkit-box-shadow: 0 1px 3px rgba(0,0,0,.1);
    box-shadow: 0 1px 3px rgba(0,0,0,.1);
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

