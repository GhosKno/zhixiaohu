<template>
  <div class="heat">
    <TopBar class="top-bar"></TopBar>
    <Scroll 
      :on-reach-bottom="handleReachBottom" 
      :height="windowHeight">
      <Row type="flex" justify="center" class="content">
        <Col :sx="18" :sm="18" :md="16" :lg="14">
          <Row>
            <Col :span="24" style="padding:0 30px;">
              <div class="topic-list-content">
                <div class="header">
                  <Icon type="ios-list-outline" style="margin-right:10px"></Icon>
                  热点话题动态
                </div>
                <div class="watched-list">
                  <Button 
                    :class="{'topic-button': true, 'topic-button-active': el.id === curTopicId}"
                    type="ghost"
                    @click="viewTopicDetail(el.id)"
                    size="small"
                    shape="circle"
                    v-for="(el,index) in heatedTopoics" 
                    :key="index">{{el.label}}
                  </Button>
                </div>
              </div>
              <div class="answer-list">
                <AnswerListCard
									v-for="(item, index) in answerList"
									:key="index"
									:answer="item"
								>
								</AnswerListCard>
              </div>
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
  export default {
    name: 'heat',
    data () {
      return {
        windowHeight: '',
        filename: '',
        heatedTopoics: [],
        curTopicId: '', // 当前查看话题列表
        answerList: []
      }
    },
    methods: {
      handleReachBottom () {
        return new Promise(resolve => {
          if(!this.nextUrl){
            this.$Message.info('没有更多的内容了')
            return resolve()
          }
          this.$http.get(this.nextUrl)
            .then(res => {
              setTimeout(() => {
                this.answerList.push(...res.body.data.results)
                resolve();
              }, 1000);
            })
        })
      },
      getHotTopics() {
        this.$http.get('/api/topics/hot')
          .then(res => {
            this.heatedTopoics = res.body.data
            this.curTopicId = this.heatedTopoics[0].id
          })
      },
      viewTopicDetail(id) {
        this.curTopicId = id
        this.$http.get(`/api/topics/${id}/get_answers/`)
          .then(res => {
            this.answerList = res.body.data.results
            this.nextUrl = res.body.data.next
          })
      }
    },
    components: {
      TopBar,
      AnswerListCard
    },
    mounted () {
      this.$nextTick(() => {
        this.windowHeight = document.body.clientHeight
      })
    },
    created () {
      this.getHotTopics()
    }
  }
</script>

<style lang="less" scoped>
.heat {
  height: 100vh;
  ::-webkit-scrollbar {
    // display:none;
  }
  .content {
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
