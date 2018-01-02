<template>
  <div class="topic">
    <TopBar></TopBar>
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
                <AnswerListCard avatar="h" name="ccc" qlink="" feed-title="热门内容,来自: 历史" question="历史上外交时有哪些尴尬场面？" answer="南海仲裁案之后，2016年7月16日，在美国国务院记者会上，凤凰卫视记者王冰汝向美国国务院发言人马克·托纳提问：“新加坡国立大学国际法中心在网站上刊登了地图和地名词典，其中一份地图，它的来源是美国政府，而且这张地图上写的是太平岛，而不是太平礁，这跟南海仲裁案“仲裁”结果不..."></AnswerListCard>
								<AnswerListCard qlink="" question="Mac 上的每个菜单命令，都能自定义快捷键吗?" cover-img="https://ss0.baidu.com/73F1bjeh1BF3odCf/it/u=3420588888,2752900295&fm=85&s=03809E4D4422EB430E34E03103008043" answer = "通常情况下，一个应用在 Mac 菜单栏显示的菜单命令，可以囊括了这个应用的大部分功能。同时也会为常用的菜单设置快捷键，比如最常见的「新建」功能，默认都是 Command + N。 为什么要自定义快捷键,许多开发者有自己的习惯,或..."></AnswerListCard>
								<AnswerListCard feed-title="你可能感兴趣: 生活"></AnswerListCard>
                <AnswerListCard
									v-for="(item, index) in answerList"
									:key="index"
									:avatar="item.avatar"
									:name="item.name" 
									:qlink="item.qlink" 
									:feed-title="item.feedTitle" 
									:question="item.question" 
									:answer="item.answer"
								>
								</AnswerListCard>
              </div>
            </Col>
            <!-- <Col span="6" style="padding:0 20px;">
              <TopicSidebar></TopicSidebar>
            </Col> -->
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
        heatedTopoics: [
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
        curPage: 1,
        topicNumofPage: 8,
        curTopic: '', // 当前查看话题列表
        answerList: [
					{
						avatar:"h",
						name:"ccc",
						qlink:"",
						feedTitle:"热门内容,来自: 历史",
						question:"历史上外交时有哪些尴尬场面？",
						answer:"南海仲裁案之后，2016年7月16日，在美国国务院记者会上，凤凰卫视记者王冰汝向美国国务院发言人马克·托纳提问：“新加坡国立大学国际法中心在网站上刊登了地图和地名词典，其中一份地图，它的来源是美国政府，而且这张地图上写的是太平岛，而不是太平礁，这跟南海仲裁案“仲裁”结果不..."
					}
				]
      }
    },
    methods: {
      handleReachBottom () {
        return new Promise(resolve => {
          setTimeout(() => {
            // this.number = this.number + 5
            this.answerList.push(...this.answerList)
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
      return
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
    // display:none;
  }
  .content {
    margin-top: 60px;
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
