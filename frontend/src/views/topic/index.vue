<template>
  <div class="topic">
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
                <span>共998个话题</span>
                <Button 
                  type="text" 
                  style="font-size:13px;"
                  @click="$refs['addTopic'].open()"
                >添加话题</Button>
              </div>
              <div class="content-body">
                <Row class="topics-content">
                  <Col 
                    v-for="(topic, index) in topicsList"
                    :key="index"
                    span="12"
                    class="topic-content-body"
                  >
                  <div class="topic-header" @click="$router.push({path: `question/${1}`})">
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
      action="/"
      :onSuccess="addTopicHandle()"
      :params="topicForm"
      successMsg="成功添加话题"
      title="添加话题"
      :validated='topicForm.label.length > 0 && topicForm.length > 0'
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
        topicsList: [
          {label: "电影", introduction: '游戏 是一种在特定时间、空间范围内遵循某种特定规则的，追求精神…'},
          {label: "互联网", introduction: '游戏 是一种在特定时间、空间范围内遵循某种特定规则的，追求精神…'},
          {label: "移动互联网", introduction: '游戏 是一种在特定时间、空间范围内遵循某种特定规则的，追求精神…'},
          {label: "学习", introduction: '游戏 是一种在特定时间、空间范围内遵循某种特定规则的，追求精神…'},
          {label: "网页设计", introduction: '游戏 是一种在特定时间、空间范围内遵循某种特定规则的，追求精神…'},
          {label: "前端开发", introduction: '游戏 是一种在特定时间、空间范围内遵循某种特定规则的，追求精神…'},
          {label: "中国历史", introduction: '游戏 是一种在特定时间、空间范围内遵循某种特定规则的，追求精神…'},
          {label: "历史", introduction: '游戏 是一种在特定时间、空间范围内遵循某种特定规则的，追求精神…'},
          {label: "HTML", introduction: '游戏 是一种在特定时间、空间范围内遵循某种特定规则的，追求精神…'},
          {label: "维基百科", introduction: '游戏 是一种在特定时间、空间范围内遵循某种特定规则的，追求精神…'},
          {label: "产品设计", introduction: '游戏 是一种在特定时间、空间范围内遵循某种特定规则的，追求精神…'},
          {label: "程序员"},
          {label: "JacaScript"},
          {label: "自然科学"},
          {label: "知识产权"}
        ],
        topicForm: {
          label: '',
          introduction: ''
        }
      }
    },
    methods: {
      handleReachBottom () {
        return new Promise(resolve => {
          setTimeout(() => {
            // this.number = this.number + 5
            // this.answerList.push(...this.answerList)
            resolve();
          }, 2000);
        });
      },
      addTopicHandle () {
        
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
