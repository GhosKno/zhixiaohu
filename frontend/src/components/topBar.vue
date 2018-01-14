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
        <SearchBox @ask="$refs['questionModal'].open()"></SearchBox>
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
              @readed="getUnreadMsg"
            ></message>
          </Poptip>
          <Dropdown trigger="click">
            <Avatar :src="$store.state.avatarUrl" />
            <DropdownMenu slot="list" class="userMenu">
              <DropdownItem><Button type="text" icon="person" @click="$router.push({path: `/profile/${$store.state.userid}`})">我的主页</Button></DropdownItem>
              <DropdownItem><Button type="text" icon="gear-b" @click="$refs['updatePwd'].open()">修改密码</Button></DropdownItem>
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
const SearchBox = resolve => require(["@/components/searchBox.vue"], resolve);
export default {
  name: "topBar",
  mixins: [cookieManage, initInfo],
  data() {
    return {
      unreadMsgsCount: 0,
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
          this.$Message.error(err.status + " " + api.errInfo[err.status]);
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
          this.$Message.error(err.status + " " + api.errInfo[err.status]);
        }
      );
    },
  },
  components: {
    questionModal,
    updatePwdModal,
    Message,
    SearchBox
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
</style>
