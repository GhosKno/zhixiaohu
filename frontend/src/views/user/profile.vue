<template>
  <div class="profile">
    <TopBar></TopBar>
    <Scroll 
      :on-reach-bottom="handleReachBottom" 
      :height="windowHeight">
      <Row type="flex" class="profile-content" style="min-height: 700px;">
        <Col span="18" offset="3">
          <Row>
            <div class="profile-header-top">
            </div>
            <div class="profile-header-bottom">
              <Row class="parent-height">
                <Col span="6" class="parent-height">
                  <div class="avatar-content">

                  </div>
                </Col>
                <Col span="7" class="parent-height">
                  <div style="font-size:2em;font-weight:bold;">用户昵称</div>
                  <div style="font-size:1.3em;">用户的简单介绍</div>
                </Col>
                <Col span="3" offset="8" class="parent-height">
                  <Button 
                    type="ghost" 
                    size="large"
                    style="bottom: 5px;position: absolute;"
                  >编辑个人资料</Button>
                </Col>
              </Row>
            </div>
          </Row>
          <Row class="profile-body">
            <Col span="16" class="profile-body-left">
              <div>
                <Tabs value="timeline" class="profile-pane">
                  <TabPane label="动态" name="timeline">
                    <div class="profile-pane-header">我的动态</div>
                    <div class="profile-pane-body">
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
                  </TabPane>
                  <TabPane label="回答" name="answer">
                    <div class="profile-pane-header">我的回答</div>
                    <div class="profile-pane-body">
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
                    </TabPane>
                  <TabPane label="提问" name="question">
                    <div class="profile-pane-header">我的提问</div>
                    <div class="profile-pane-body">
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
                  </TabPane>
                </Tabs>
              </div>
            </Col>
            <Col span="8" class="profile-body-right">
              <div>
                <div class="watch-bar">
                  <div class="watch-people">
                    <div>关注了</div>
                    <div>8</div>
                  </div>
                  <div class="watched-people">
                    <div>关注者</div>
                    <div>5</div>
                  </div>
                </div>
                <div class="profile-lightItem">
                  <span>
                    关注的问题
                  </span>
                  <span>
                    20
                  </span>
                </div>
                <div class="profile-lightItem">
                  <span>
                    收藏的回答
                  </span>
                  <span>
                    20
                  </span>
                </div>
                <div class="profile-lightItem">
                  <span>
                    围观历史
                  </span>
                  <span>
                    20
                  </span>
                </div>
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
  import cookieManage from '@/mixins/cookieManage'
  import initInfo from '@/mixins/initInfo'
  export default {
    name: 'profile',
    mixins: [cookieManage, initInfo],
    components: {
      TopBar,
      AnswerListCard
    },
    data() {
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
            this.answerList.push(...this.answerList)
            resolve();
          }, 2000);
        });
      }
    },
    created () {
      if(this.initInfo()){
        this.$http.get(`/api/accounts/profile/${this.$store.state.userid}/`)
        .then(res => {
          if(res.body.success) {
            console.log(res.body.data)
          }
        })
      }
    },
    mounted () {
      this.$nextTick(() => {
        this.windowHeight = document.body.clientHeight
      })
    }
  }
</script>

<style lang="less" scoped>
.profile{
  height: 100vh;
  ::-webkit-scrollbar {
    // display:none;
  }
  .parent-height{
    height: 100%;
  }
  .profile-content{
    margin-top: 60px;
    .profile-header-top{
      height: 110px;
      background: #96a1a9;
      border-radius: 5px 5px 0 0;
    }
    .profile-header-bottom {
      background: #fff;
      height: 160px;
      padding: 10px 10px;
      border-radius: 0 0 5px 5px ;
      .avatar-content{
        height: 170px;
        width: 170px;
        margin: 0 auto;
        top: -40px;
        position: relative;
        background: #f9f9f9;
        border-radius: 5px;
      }
    }
    .profile-body {
      margin-top: 10px;
      .profile-body-left > div{
        background: #fff;       
      }
      .profile-body-left{
        padding-right: 10px;
        .profile-pane{
          .profile-pane-header{
            font-size: 1.2em;
            font-weight: bold;
            border-bottom: 1px solid #dddee1;
            padding-left: 5px;
            margin: 0 15px;
          }
        }
      }
      .profile-body-right{
        .watch-bar{
          margin-bottom: 10px;
        }
        .watch-bar > div:hover > div{
          color:#175199 !important;
        }
        .watch-bar > div{
          cursor: pointer;
          display: inline-block;
          background: #fff;
          width: 48%;
          height: 80px;
          div{
            text-align: center; 
          }
          div:nth-child(1){
            line-height: 35px;
            color: #8590a6;
          }
          div:nth-child(2){
            font-size: 1.5em;
            font-weight: bold;
          }
        }
        .watched-people{
          float: right;
        }
        .profile-lightItem{
          height: 50px;
          border-top: 1px #dddee1 solid;
          span{
            line-height: 50px;  
          }
          span:nth-child(2) {
            float: right;
          }
        }
        .profile-lightItem:last-child{
          border-bottom: 1px #dddee1 solid;
        }
      }
    }
  }
}
</style>

