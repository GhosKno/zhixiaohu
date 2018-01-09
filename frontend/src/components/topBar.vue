<template>
  <Affix>
    <header>
      <div class="header-inner">
        <Button type="text" @click="$router.push({name: 'home'})">
        <Logo class="logo" scale="0.9"></Logo>
        </Button>
        <Nav>
          <a :class="{'nav-item': true, 'active': $route.name === 'home'}" @click="$router.push({name: 'home'})">
              广场
          </a>
          <a :class="{'nav-item': true, 'active': $route.name === 'heat'}" @click="$router.push({name: 'heat'})">
              热点
          </a>
          <a :class="{'nav-item': true, 'active': $route.name === 'topic'}"  @click="$router.push({name: 'topics'})">
              话题
          </a>
        </Nav>

        <div class="search">
          <input class="searchInput" maxlength="50" type="text" placeholder="搜索你感兴趣的内容..." required @focus="showAskBtn = false" @blur="showAskBtn = true">
          <Button type="text" class="searchBtn"><Icon type="ios-search-strong" class="searchIcon" size=20 ></Icon></Button>  
        </div>
        <Button type="primary" class="askBtn" :class="{'is-active':showAskBtn}" @click="$refs['questionModal'].open()">提问</Button>
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
            <message ref="message" slot="content"></message>
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
const questionModal = resolve => require(['@/components/questionAskModal.vue'], resolve)
const updatePwdModal = resolve => require(['@/components/updatePasswordModal.vue'], resolve)
const Logo = resolve => require(['@/components/logo.vue'], resolve)
const Message = resolve => require(['@/components/message.vue'], resolve)
export default {
  name: "topBar",
  mixins: [cookieManage, initInfo],
  data() {
    return {
      theme1: "light",
      showAskBtn: true,
      unreadMsgsCount: 0
    };
  },
  methods: {
    logout() {
      this.$http.get('/api/users/logout/')
          .then(res => {
            if(res.body.success) {
              this.cookieLogout();
              this.$router.go(0);
            } else {
              this.$Message.error(res.data.msg)
            }
          }, function(response){
            // 响应错误回调 
             this.$Message.error(response.status+" "+response.statusText)
          });
    },
    getUnreadMsg() {
      this.$http.get('/api/messages/unread/')
        .then(res => {
          this.unreadMsgsCount = res.body.data.count
        }, function(response){
            // 响应错误回调 
             this.$Message.error(response.status+" "+response.statusText)
        });
    }
  },
  components: {
    questionModal,
    updatePwdModal,
    Logo,
    Message,
  },
  created () {
    if(this.initInfo())
      this.getUnreadMsg()
  }
};
</script>

<style scoped>
header {
  min-width: 1260px;
  width: 100%;
  min-width: 1032px;
  overflow: hidden;
  background: #fff;
  -webkit-box-shadow: 0 1px 3px 0 rgba(0, 34, 77, 0.1);
  box-shadow: 0 1px 3px 0 rgba(0, 34, 77, 0.1);
  background-clip: content-box;
  z-index: 100;
  overflow: inherit;
}
nav {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
  height: 30px;
  color: #999;
}
.header-inner {
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
}
.nav-item {
  font-weight: 500;
  padding: 0 15px;
  font-size: 15px;
  line-height: 30px;
  color: #8590a6;
}
.nav-item:hover {
  color: #175199;
}

.nav-item.active {
  color: #333;
}
.search {
  position: relative;
  margin: 15px;
}
.searchInput {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
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
  resize: none;
  -webkit-transition: background 0.3s, width 0.2s;
  transition: background 0.3s, width 0.2s;
}
.search .searchInput:focus {
  width: 400px;
  background: #fff;
  border: 1px solid #9fadc7;
}
.searchBtn {
  position: absolute;
  right: 0;
  top: 0;
}
.askBtn.is-active {
  opacity: 1;
  transform: scale(1);
}
.askBtn {
  opacity: 0;
  transform: scale(0);
  -webkit-transform: scale(0);
  transition: opacity 0.2s, transform 0.2s,
    -webkit-transform 0.2s;
}
.searchIcon {
  color: #8590a6;
}

.searchInput::-webkit-input-placeholder {
  color: #9fadc7;
  font-weight: 500;
}

.searchInput:-ms-input-placeholder {
  color: #9fadc7;
  font-weight: 500;
}
.searchInput::placeholder {
  color: #9fadc7;
  font-weight: 500;
}
.searchInput:focus + .searchBtn .searchIcon {
  color: #0f88eb;
}
.searchInput:valid + .searchBtn .searchIcon {
  color: #fff;
}
.searchInput:valid + .searchBtn {
  background: #0f88eb;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
  height: 100%;
}
.rightBtns,
.userInfo {
  position: absolute;
  right: 80px;
}
.userInfo .messageRing {
  font-size: 2em;
  color: #9fadc7;
  margin-right: 20px;
}
.userMenu button {
  font-size: 1.2em;
}
</style>
