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
        <question-card
          v-for="(item, index) in questions"
          :key="index"
          :title="item.title"
          :time="item.add_time"
          :answers="item.answer_count"
          :watchers="item.watch_count"
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
      topicTitle: '区域经济学',
      introduction: '区域经济学(Regional Economics，也称地区经济学)是经济学与地理学交叉而形成的应用经济学。区域经济学是从经济学角度研究区域经济发展与区域关系协调的科学。'
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
    this.getQuestions()
    return
    this.$http.get(`/api/topics/${this.$route.params.id}/`)
      .then(res => {
        this.topicTitle = res.body.data.label
        this.introduction = res.body.data.introduction
      })
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

  }
}
</style>

