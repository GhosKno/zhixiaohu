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
                  热点话题动态
                </div>
                <div class="watched-list">
                  <Button 
                    :class="{'topic-button': true, 'topic-button-active': el.label === curTopic}"
                    type="ghost" 
                    size="small"
                    shape="circle"
                    v-for="(el,index) in heatedTopoics" 
                    :key="index">{{el.label}}
                  </Button>
                </div>
              </div>
              <div class="answer-list">
                    <AnswerListCard 
                      v-for="(answer, index) in answerList" 
                      :key="index"
                      :answer="answer.detail"
                      :question="answer.question"
                      ></AnswerListCard>
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
        windowHeight: '',
        heatedTopoics: [],
        curPage: 1,
        topicNumofPage: 8,
        curTopic: '', // 当前查看话题列表
        answerList: [],
        number: 5
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
      this.$nextTick(() => {
        this.windowHeight = document.body.clientHeight
      })
    },
    created () {
      this.$http.get(`/api/topics/heat/${this.curPage}/${this.topicNumofPage}`)
        .then(res => {
          if(res.body.success) {
            this.heatedTopoics = res.body.data
            this.curTopic = this.heatedTopoics[0].label
          }
        })
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
