<template>
  <div class="topic">
    <TopBar class="top-bar"></TopBar>
    <Scroll 
      :on-reach-bottom="handleReachBottom" 
      :height="windowHeight">
      <Row type="flex" justify="center" class="content">
        <Col :sx="18" :sm="18" :md="16" :lg="14">
          <Row>
            <Col :span="24" style="padding:0 30px;">
              <div class="content-header">
                <Icon size="20" type="grid"></Icon>
                <span>话题广场</span>
                <span>共{{topicsCount}}个话题</span>
                <Button 
                  type="text" 
                  style="font-size:13px;"
                  @click="$refs['addTopic'].open()"
                >添加话题</Button>
              </div>
              <div class="content-body">
                <Row class="topics-content">
                  <div
                    v-if="topicsList.length == 0" 
                    class="no-topic">
                    还没有话题，快去添加话题吧
                  </div>
                  <Col 
                    v-for="(topic, index) in topicsList"
                    :key="index"
                    span="12"
                    class="topic-content-body"
                  >
                  <div class="topic-header" @click="$router.push({path: `topic/${1}`})">
                    {{topic.label}}
                  </div>
                  <div class="topic-introduction">
                    {{topic.introduction}}
                  </div>
                  </Col>
                </Row>
              </div>
            </Col>
          </Row>
        </Col>
      </Row>
    </Scroll>
    <z-modal
      action="/api/topics/"
      :onSuccess="addTopicHandle"
      :params="topicForm"
      successMsg="成功添加话题"
      title="添加话题"
      :validated='topicForm.label.length > 0 && topicForm.introduction.length > 0'
      ref="addTopic"
    >
      <div slot="body" class="topic-form">
        <Input v-model="topicForm.label" placeholder="填写新的话题标题"></Input>
        <Input type="textarea" :rows='4' v-model="topicForm.introduction" placeholder="为该话题增加一些描述"></Input>
      </div>
    </z-modal>
  </div>
</template>

<script>
  const TopBar = resolve => require(['@/components/topBar'], resolve)
  const ZModal = resolve => require(['@/components/z-modal'], resolve)
  const AnswerListCard = resolve => require(['@/components/answerListCard'], resolve)
  export default {
    name: 'topic',
    data () {
      return {
        windowHeight: '',
        topicsList: [],
        topicsCount: '',
        nextPageUrl: '',
        topicForm: {
          label: '',
          introduction: ''
        }
      }
    },
    methods: {
      handleReachBottom () {
        let re = /(\w+):\/\/([^\:|\/]+)(\:\d*)?(.*\/)([^#|\?|\n]+)?(#.*)?(\?.*)?/i;
        return new Promise(resolve => {
          if(!this.nextPageUrl){
            this.$Message.info('没有下一页了')
            resolve()
            return
          }
          this.$http.get(this.nextPageUrl.match(re).slice(4).join(''))
            .then(res => {
              this.nextPageUrl = res.body.data.next
              this.topicsCount = res.body.data.count
              setTimeout(() => {
                resolve();
                this.topicsList.push(...(res.body.data.results))
              }, 500);
            })
        });
      },
      addTopicHandle (res) {
        if(res.body.success) {
          this.getTopics()
        }
      },
      getTopics() {
        this.$http.get('/api/topics/')
          .then(res => {
            this.topicsList = res.body.data.results
            this.topicsCount = res.body.data.count
            if(res.body.data.next) {
              this.nextPageUrl = res.body.data.next
            }
          })
      }
    },
    components: {
      TopBar,
      AnswerListCard,
      ZModal
    },
    mounted () {
      this.$nextTick(() => {
        this.windowHeight = document.body.clientHeight
      })
    },
    created () {
      this.getTopics()
    }
  }
</script>

<style lang="less" scoped>
.topic {
  height: 100vh;
  // background: #fff;
  ::-webkit-scrollbar {
    // display:none;
  }
  .content {
    >div:first-child {
      background: #fff;
    }
    .content-header {
      height: 50px;
      border-bottom: 1px solid #ccc;
      line-height: 50px;
      *:first-child {
        margin-right: 15px;
        color:#ccc;
      }
      span:nth-child(2) {
        font-weight: bold;
      }
      span:nth-child(3) {
        float: right;
        font-size: 0.8em;
        color: #ccc;
      }
    }
    .content-body {
      min-height: 300px;
      .no-topic {
        height: 200px;
        font-size: 15px;
        color: #8590a6;
        text-align: center;
        padding-top: 100px;
      }
      .topics-content {
        .topic-content-body {
          height: 100px;
          padding: 20px 10px;
          border-bottom: 1px #eee dotted;
          .topic-header {
            font-weight: bold;
            cursor: pointer;
          }
          .topic-header:hover {
            color: #175199;
          }
          .topic-introduction {
            margin-top: 3px;
            font-size: 0.8em;
          }
        }
      }
    }
  }
}
.topic-form {
  width: 60%;
  margin: 0 auto;
  >div {
    margin: 10px 0;
  }
}
</style>
