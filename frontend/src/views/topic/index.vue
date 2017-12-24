<template>
  <div class="topic">
    <TopBar></TopBar>
    <Scroll :on-reach-bottom="handleReachBottom" :height="windowHeight">
      <Row type="flex" justify="center" class="content">
        <Col :sx="18" :sm="18" :md="16" :lg="14">
          <Row>
            <Col span="18" style="padding:0 30px;">
              <div class="topic-list-content">
                <div class="header">
                  <Icon type="ios-list-outline" style="margin-right:10px"></Icon>
                  已关注话题动态
                  <Button class="all-topic-button" type="text">共关注{{watchedTopic.length}}个话题</Button>
                </div>
                <div class="watched-list">
                  <Button 
                    :class="{'topic-button': true, 'topic-button-active': el.label === curTopic}"
                    type="ghost" 
                    size="small"
                    shape="circle"
                    v-for="(el,index) in watchedTopic" 
                    :key="index">{{el.label}}
                  </Button>
                </div>
              </div>
              <div class="answer-list">
                    <AnswerListCard v-for="n in number" :key="n"></AnswerListCard>
              </div>
            </Col>
            <Col span="6" style="padding:0 20px;">
              <TopicSidebar></TopicSidebar>
            </Col>
          </Row>
        </Col>
      </Row>
    </Scroll>
  </div>
</template>

<script>
  const TopBar = resolve => require(['@/components/topBar'], resolve)
  const AnswerListCard = resolve => require(['@/components/answerListCard'], resolve)
  const TopicSidebar = resolve => require(['@/components/topic/topicSidebar'], resolve)
  export default {
    name: 'topic',
    data () {
      return {
        watchedTopic: [ //用户关注的所有话题列表
          {label: "电影"},
          {label: "互联网"},
          {label: "移动互联网"},
          {label: "学习"},
          {label: "网页设计"},
          {label: "前端开发"},
          {label: "中国历史"},
          {label: "历史"},
          {label: "HTML"},
          {label: "维基百科"},
          {label: "产品设计"},
          {label: "程序员"},
          {label: "JacaScript"},
          {label: "自然科学"},
          {label: "知识产权"}
        ],
        curTopic: '程序员', // 当前查看话题列表
        number: 5, //tmp var TODO
      }
    },
    methods: {
      handleReachBottom () {
                return new Promise(resolve => {
                    setTimeout(() => {
                        this.number = this.number + 5
                        resolve();
                    }, 2000);
                });
            }
    },
    components: {
      TopBar,
      TopicSidebar,
      AnswerListCard
    },
    mounted () {
      this.windowHeight = document.body.clientHeight
    }
  }
</script>

<style lang="less" scoped>
.topic {
  height: 100vh;
  ::-webkit-scrollbar {
    display:none;
  }
  .content {
    margin-top: 100px;
    .topic-list-content {
      .header {
        width: 100%;
        font-size: 1.2em;
        border-bottom: 1px solid #ccc;
        padding-bottom: 7px;
        margin-bottom: 12px;
        .all-topic-button {
          position: relative;
          right: 0;
          // float: right;
          font-size: 1em;
          bottom: 2px;
        }
      }
      .watched-list {
        border-bottom: 1px solid #ccc;
        padding-bottom: 12px;
        margin-bottom: 12px;
        .topic-button {
          margin: 5px 8px;
        }
        .topic-button-active {
          // background: #2b85e4;
          border-color: #2b85e4;
        }
      }
    }
  }
}
</style>
