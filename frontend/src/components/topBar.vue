<template>
  <Affix>
    <header>
      <div class="inner">
        <Button type="text" @click="$router.push({name: 'home'})">
          <svg class="logo">
            <use xlink:href="#logo"></use>
          </svg>
        </Button>
        <Nav>
          <a class="item" :class="{'active': $route.name === 'home'}" @click="$router.push({name: 'home'})">
              广场
          </a>
          <a class="item" :class="{'active': $route.name === 'heat'}" @click="$router.push({name: 'heat'})">
              热点
          </a>
          <a class="item" :class="{'active': $route.name === 'topic'}"  @click="$router.push({name: 'topics'})">
              话题
          </a>
        </Nav>
        <Dropdown trigger="custom" :visible="!showAskBtn" :transfer="true" placement="bottom-start" @on-click="handleSearchResult">    
          <div class="search" :class="{'is-active':showAskBtn}">
            <div class="wrapper">
              <input class="input" 
                maxlength="50" 
                type="text" 
                placeholder="搜索你想知道的问题..." required 
                v-model="searchData"
                @focus="showAskBtn = false" 
                @blur="showAskBtn = true"
                @keyup="handleSearch()">
              <Button type="text" class="searchBtn"><Icon type="ios-search-strong" class="searchIcon" size=20 ></Icon></Button>  
            </div>
            <Button type="primary" class="askBtn" :class="{'is-active':showAskBtn}" @click="$refs['questionModal'].open()">提问</Button>
          </div>
          <DropdownMenu slot="list" style="width: 380px;" 
              v-if="searchQuestions.length > 0 || 
              searchTopics.length > 0 || 
              searchAnswers.length > 0">
              <DropdownItem 
              v-for="item in searchTopics"      
              :key="item.id"
              :name="item.id"
              >{{item.label}}
              </DropdownItem>
              <DropdownItem 
              v-for="(item, index) in searchQuestions"
              :divided="index == 0"
              :key="item.id"
              :name="item.id"
              >{{item.title}}
              </DropdownItem>
              <DropdownItem 
              v-for="(item, index) in searchAnswers"
              :divided="index == 0"
              :key="item.id"
              :name="item.id"
              >{{item.title}}
              </DropdownItem>
          </DropdownMenu>
        </Dropdown>
        <div class="rightBtns" v-if="!$store.state.isLogin">
          <Button type="ghost" class="loginBtn" @click="$router.push({name: 'login'})">登录</Button>
          <Button type="primary" class="joinBtn" @click="$router.push({name: 'login', params: {register: true}})">加入知小乎</Button>
        </div>
        <div class="userInfo" v-else>
          <Poptip placement="bottom" width="400">
            <Button type="text" class="messageRing" @click="$refs['message'].open()">
              <Badge :count="unreadMsgsCount" overflow-count="999">
                <Icon type="ios-bell"></Icon>
              </Badge>
            </Button>
            <message 
              ref="message" 
              slot="content"
              :readHandle="getUnreadMsg"
            ></message>
          </Poptip>
          <Dropdown trigger="click">
            <Avatar :src="$store.state.avatarUrl" />
            <DropdownMenu slot="list" class="userMenu">
              <DropdownItem><Button type="text" icon="person" @click="$router.push({path: `/profile/${$store.state.userid}`})">我的主页</Button></DropdownItem>
              <DropdownItem><Button type="text" icon="gear-b" @click="$refs['updatePwd'].open()">设置</Button></DropdownItem>
              <DropdownItem><Button type="text" icon="log-out" @click="logout">退出</Button></DropdownItem>
            </DropdownMenu>
          </Dropdown>
        </div>
      </div>
      <question-modal ref="questionModal"></question-modal>
    </header>
    <update-pwd-modal ref="updatePwd"></update-pwd-modal>
  </Affix>
</template>

<script>
import cookieManage from "@/mixins/cookieManage";
import initInfo from "@/mixins/initInfo";
import api from "@/utils/api";

const questionModal = resolve =>
  require(["@/components/questionAskModal.vue"], resolve);
const updatePwdModal = resolve =>
  require(["@/components/updatePasswordModal.vue"], resolve);
const Message = resolve => require(["@/components/message.vue"], resolve);
export default {
  name: "topBar",
  mixins: [cookieManage, initInfo],
  data() {
    return {
      theme1: "light",
      showAskBtn: true,
      unreadMsgsCount: 0,
      searchData: "",
      searchQuestions: [],
      searchAnswers: [],
      searchTopics: [] 
    };
  },
  methods: {
    logout() {
      api.logout().then(
        res => {
          if (res.body.success) {
            this.cookieLogout();
            this.$router.push({ name: "login" });
          } else {
            this.$Message.error(res.data.msg);
          }
        },
        err => {
          this.$Message.error(err.status + " " + err.statusText);
          this.cookieLogout();
        }
      );
    },
    getUnreadMsg() {
      api.getUnreadNum().then(
        res => {
          this.unreadMsgsCount = res.body.data.count;
        },
        err => {
          this.$Message.error(err.status + " " + err.statusText);
        }
      );
    },
    handleSearch() {
      if (this.searchData != "") {
        api.searchQuestion(this.searchData).then(
          res => {
            if (res.body.success) {
              this.searchQuestions = res.body.data.results;
            } else {
              this.$Message.error(res.body.msg);
            }
          },
          err => {
            this.$Message.error(err.status + " " + err.statusText);
          }
        );
        // api.searchAnswers(this.searchData).then(res => {
        //     if (res.body.success) {
        //       this.searchAnswers = res.body.data.results;
        //     } else {
        //       this.$Message.error(res.body.msg);
        //     }
        //   },
        //   err => {
        //     this.$Message.error(err.status + " " + err.statusText);
        //   }
        // );
        api.searchTopics(this.searchData).then(res => {
            if (res.body.success) {
              this.searchTopics = res.body.data.results;
            } else {
              this.$Message.error(res.body.msg);
            }
          },
          err => {
            this.$Message.error(err.status + " " + err.statusText);
          }
        );
      }
    },
    handleSearchResult(id) {
      if(!id) return
      window.location = "/question/" + id;
    }
  },
  components: {
    questionModal,
    updatePwdModal,
    Message
  },
  created() {
    if (this.initInfo()) this.getUnreadMsg();
  }
};
</script>

<style lang="less" scoped>
header {
  width: 100%;
  min-width: 1032px;
  background: #fff;
  -webkit-box-shadow: 0 1px 3px 0 rgba(0, 34, 77, 0.1);
  box-shadow: 0 1px 3px 0 rgba(0, 34, 77, 0.1);
  background-clip: content-box;
  z-index: 100;
  overflow: inherit;
  .inner {
    position: relative;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    min-width: 1000px;
    width: 80%;
    height: 52px;
    padding: 0 16px;
    margin: 0 auto;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    .logo {
      width: 120px;
      height: 43px;
      vertical-align: text-bottom;
    }
    nav {
      display: inherit;
      margin-right: 20px;
      .item {
        font-weight: 500;
        padding: 0 15px;
        font-size: 15px;
        line-height: 30px;
        color: #8590a6;
        &:hover {
          color: #175199;
        }
        &.active {
          color: #333;
        }
      }
    }
    .rightBtns,
    .userInfo {
      position: absolute;
      right: 80px;
      .messageRing {
        font-size: 2em;
        color: #9fadc7;
        margin-right: 20px;
        line-height: 24px;
      }
    }
    .userMenu button {
      font-size: 1.2em;
    }
  }
}
.search {
  position: relative;
  -webkit-transition: all .2s;
  transition: all .2s;
  &.is-active {
    padding-right: 94px;
  }
  .wrapper {
    position: relative;
    .input {
      width: 300px;
      height: 34px;
      padding-left: 10px;
      padding-right: 50px;
      font-size: 14px;
      border: 1px solid #e7eaf1;
      border-radius: 3px;
      -webkit-box-sizing: border-box;
      box-sizing: border-box;
      background: #f7f8fa;
      border: none;
      outline: none;
      -webkit-transition: all .2s;
      transition: all .2s;
      &:focus {
        width: 380px;
        background: #fff;
        border: 1px solid #9fadc7;
      }
      &::placeholder {
        color: #9fadc7;
        font-weight: 500;
      }
    }
    .input:focus + .searchBtn .searchIcon {
      color: #0f88eb;
    }
    .input:valid + .searchBtn .searchIcon {
      color: #fff;
    }
    .input:valid + .searchBtn {
      background: #0f88eb;
      border-top-left-radius: 0;
      border-bottom-left-radius: 0;
      height: 100%;
    }
    .searchBtn {
      position: absolute;
      right: 0;
      top: 0;
    }
    .searchIcon {
      color: #8590a6;
    }
  }
  .askBtn {
    position: absolute;
    right: 15px;
    bottom: 0;
    opacity: 0;
    transform: scale(0);
    -webkit-transform: scale(0);
    transition: opacity 0.2s, transform 0.2s, -webkit-transform 0.2s;
    &.is-active {
      opacity: 1;
      transform: scale(1);
    }
  }
}
</style>
