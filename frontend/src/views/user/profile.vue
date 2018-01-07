<template>
  <div class="profile">
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
                  <div class="avatar-content"
                    :style="`background-image:url(${avatarUrl})`"
                  >
                  </div>
                </Col>
                <Col span="7" class="parent-height">
                  <div style="font-size:2em;font-weight:bold;">{{nickName}}</div>
                  <div style="font-size:1.3em;">{{description}}</div>
                </Col>
                <Col span="3" offset="8" class="parent-height">
                  <Button 
                    v-if="$route.params.id == $store.state.userid"
                    type="ghost" 
                    size="large"
                    style="bottom: 5px;position: absolute;"
                    @click="$router.push({name: 'profileEdit'})"
                  >编辑个人资料</Button>
                  <Button 
                    v-else
                    type="primary" 
                    size="large"
                    style="bottom: 5px;position: absolute;"
                    @click="$router.push({name: 'profileEdit'})"
                  >关注Ta</Button>
                </Col>
              </Row>
            </div>
          </Row>
          <Row class="profile-body">
            <Col span="16" class="profile-body-left">
              <div>
                <el-tabs 
                  :value="profilePaneActiveName" 
                  @tab-click="tabClick"
                  class="profile-pane">
                  <el-tab-pane label="动态" name="timeline">
                    <div class="profile-pane-header">{{$route.params.id == $store.state.userid ? '我' : 'Ta'}}的动态</div>
                    <div class="profile-pane-body">
                      <!-- //todo -->
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
                  </el-tab-pane>
                  <el-tab-pane label="回答" name="answer">
                    <div class="profile-pane-header">{{$route.params.id == $store.state.userid ? '我' : 'Ta'}}的回答</div>
                    <div class="profile-pane-body">
                      <div
                        class="no-data-content" 
                        v-if="answerList.length == 0"
                      >
                        还没有回答
                      </div>
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
                  </el-tab-pane>
                  <el-tab-pane label="提问" name="question">
                    <div class="profile-pane-header">{{$route.params.id == $store.state.userid ? '我' : 'Ta'}}的提问</div>
                    <div class="profile-pane-body">
                      <div 
                        class="no-data-content" 
                        v-if="askQuestion.length == 0"
                      >
                        还没有问题
                      </div>
                      <question-card
                        v-for="(item, index) in askQuestion"
                        :key="index"
                        :title="item.title"
                        :time="item.time"
                        :answers="item.answer"
                        :watchers="item.watch"
                      ></question-card>
                    </div>
                  </el-tab-pane>
                  <el-tab-pane label="更多" name="more">
                    <el-tabs :value="morePaneActiveName" class="morePane">
                      <el-tab-pane :label="`${$route.params.id == $store.state.userid ? '我' : 'Ta'}关注的人`" name="watch">
                        <div
                          class="no-data-content" 
                          v-if="watchedUser.length == 0"
                        >
                          还没有关注用户
                        </div>
                        <user-card
                          v-for="(user, index) in watchedUser"
                          :key="index"
                          :userName="user.nickName"
                          :description="user,description"
                          :answer="user.answers"
                          :watched="user.watchedBy"
                        ></user-card>
                      </el-tab-pane>
                      <el-tab-pane :label="`关注${$route.params.id == $store.state.userid ? '我' : 'Ta'}的人`" name="watched">
                        <div 
                          class="no-data-content" 
                          v-if="watchedBy.length == 0"
                        >
                          还没有关注用户
                        </div>
                        <user-card
                          v-for="(user, index) in watchedBy"
                          :key="index"
                          :userName="user.nickName"
                          :description="user,description"
                          :answer="user.answers"
                          :watched="user.watchedBy"
                        ></user-card>
                      </el-tab-pane>
                      <el-tab-pane label="关注的问题" name="watchQuestion">
                        <div 
                          class="no-data-content"  
                          v-if="watchedQuestion.length == 0"
                        >
                          还没有问题
                        </div>
                        <question-card
                          v-for="(item, index) in watchedQuestion"
                          :key="index"
                          :title="item.title"
                          :time="item.time"
                          :answers="item.answer"
                          :watchers="item.watch"
                        ></question-card>
                      </el-tab-pane>
                      <el-tab-pane label="收藏的回答" name="collectedAnswer">
                        <div 
                          class="no-data-content"  
                          v-if="favorites.length == 0"
                        >
                          还没有收藏的回答
                        </div>
                        <AnswerListCard
                          v-for="(item, index) in favorites"
                          :key="index"
                          :avatar="item.avatar"
                          :name="item.name" 
                          :qlink="item.qlink" 
                          :feed-title="item.feedTitle" 
                          :question="item.question" 
                          :answer="item.answer"
                        >
                        </AnswerListCard>
                      </el-tab-pane>
                      <el-tab-pane label="围观历史" name="history">
                        <div 
                          class="no-data-content" 
                          v-if="history.length == 0"
                        >
                          还没有围观历史
                        </div>
                        <question-card
                          v-for="(item, index) in history"
                          :key="index"
                          :title="item.title"
                          :time="item.time"
                          :answers="item.answer"
                          :watchers="item.watch"
                        ></question-card>
                      </el-tab-pane>
                    </el-tabs>
                  </el-tab-pane>
                </el-tabs >
              </div>
            </Col>
            <Col span="8" class="profile-body-right">
              <div>
                <div class="watch-bar">
                  <div class="watch-people" @click="profilePaneActiveName = 'more';morePaneActiveName = 'watch';">
                    <div>关注了</div>
                    <div>{{watchedUser.length}}</div>
                  </div>
                  <div class="watched-people" @click="morePaneActiveName = 'watched';profilePaneActiveName = 'more';">
                    <div>关注者</div>
                    <div>{{watchedBy.length}}</div>
                  </div>
                </div>
                <div class="profile-lightItem" @click="morePaneActiveName = 'watchQuestion';profilePaneActiveName = 'more';">
                  <span>
                    关注的问题
                  </span>
                  <span>
                    {{watchedQuestion.length}}
                  </span>
                </div>
                <div class="profile-lightItem" @click="morePaneActiveName = 'collectedAnswer';profilePaneActiveName = 'more';">
                  <span>
                    收藏的回答
                  </span>
                  <span>
                    {{favorites.length}}
                  </span>
                </div>
                <div class="profile-lightItem" @click="morePaneActiveName = 'history';profilePaneActiveName = 'more';">
                  <span>
                    围观历史
                  </span>
                  <span>
                    {{history.length}}
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
  const AnswerListCard = resolve => require(['@/components/answerListCard'], resolve)
  const userCard = resolve => require(['@/components/userCard'], resolve)
  const questionCard = resolve => require(['@/components/questionCard'], resolve)

  import cookieManage from '@/mixins/cookieManage'
  import initInfo from '@/mixins/initInfo'
  export default {
    name: 'profile',
    mixins: [cookieManage, initInfo],
    components: {
      AnswerListCard,
      userCard,
      questionCard
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
				],
        morePaneActiveName: 'watch',
        profilePaneActiveName: 'timeline',
        //user info
        avatarUrl: '',
        nickName: '',
        description: '',
        watchedUser: [],
        watchedBy: [],
        watchedQuestion: [],
        askQuestion: [],
        history: [],
        favorites: []
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
      },
      tabClick(pane) {
        this.profilePaneActiveName = pane.name;
      }
    },
    created () {
      if(this.initInfo()){
        this.$http.get(`/api/profiles/${this.$route.params.id}/`)
        .then(res => {
          if(res.body.success) {
            let data = res.body.data
            this.nickName = data.nickname
            this.description = data.description.length == 0 ? "这个用户很懒，什么也没留下" : data.description
            this.watchedUser = data.watchedUser || []
            this.watchedBy = data.watchedBy || []
            this.watchedQuestion = data.watchedQuestion || []
            this.askQuestion = data.askQuestion || []
            this.history = data.history || []
            this.favorites = data.favorites || []
            this.avatarUrl = data.avatar || ''
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
        background-repeat: no-repeat;
        background-size: cover;
        height: 170px;
        width: 170px;
        margin: 0 auto;
        top: -40px;
        position: relative;
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
          padding: 0 20px;
          .profile-pane-header{
            font-size: 1.2em;
            font-weight: bold;
            border-bottom: 1px solid #dddee1;
            padding: 0 0 5px 5px;
            // margin: 0 15px;
          }
          .morePane {
            // width: 95%;
            margin: 0 auto;
          }
          .no-data-content {
            height: 200px;
            font-size: 15px;
            color: #8590a6;
            text-align: center;
            padding-top: 100px;
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
          cursor: pointer;
        }
        .profile-lightItem:hover > span{
          color:#175199 !important;
        }
        .profile-lightItem:last-child{
          border-bottom: 1px #dddee1 solid;
        }
      }
    }
  }
}
</style>

