<template>
  <div class="user-card">
    <Row style="height:100%;">
    <Col span="5" class="avatar">
      <div class="avatar-content">
        <Poptip trigger="hover" 
            placement="right-start" 
            width="400"
            @on-popper-hide="() => $refs['userPoptip'].blur()"
            @on-popper-show="() => $refs['userPoptip'].load()">
            <!-- <Avatar shape="square" size="large" :src="avatar"/> -->
            <img :src="avatar" alt="" style="height:100%;width:100%;">
            <div class="api" slot="content">
                <user-poptip ref="userPoptip" :id="userid"></user-poptip>
            </div>
        </Poptip>
      </div>
    </Col>
    <Col span="14" class="info">
      <div class="user-name" @click="$router.push({path: `/profile/${userid}`})">{{userName}}</div>
      <div class="description">{{description.length > 0 ? description : '这个用户很懒，什么都没留下'}}</div>
      <div class="detail" v-if="answer">
        <span>{{answer}} 个回答</span>
        <span>{{watched}} 个关注者</span>
      </div>
    </Col>
    <Col span="5" class="button-handle" v-if="userid !== $store.state.userid">
      <Button 
        size="large" 
        class="watch-button"
        @click="watchPeopleHandle()"
      >
        <span>{{isWatched ? '已关注' : '关注'}}</span>
        <span style="display:none;">{{isWatched ? '取消关注' : '关注'}}</span>
      </Button>
    </Col>
    </Row>
  </div>
</template>


<script>
import api from "@/utils/api";
const UserPoptip = resolve => require(["@/components/userPoptip"], resolve);
  export default {
    name: 'userCard',
    components: {
      UserPoptip
    },
    data() {
      return {}
    },
    props: {
      userid: {
        type: Number,
        required: true
      },
      userName: {
        type: String,
        required: true
      },
      description: {
        type: String,
        required: true
      },
      isWatched: {
        type: Boolean,
        required: true
      },
      answer: {
        type: Number,
        default: 0
      },
      watched: {
        type: Number,
        default: 0
      },
      avatar: String,
      watchHandle: {
        type: Function,
        required: true
      }
    },
    methods: {
      watchPeopleHandle() {
        if(!this.isWatched){
          api.watchSb(this.userid).then(res => {
            if(!res.body.success) {
              this.$Message.error('操作失败')
            }
            this.watchHandle()
          })
        }else{
          api.cancelWatchSb(this.userid).then(res => {
            if(!res.body.success) {
              this.$Message.error('操作失败')
            }
            this.watchHandle()
          })
        }
      }
    }
  }
</script>

<style lang="less" scoped>
.user-card {
  width: 100%;
  margin: 0 auto;
  margin-top: 20px;
  height: 100px;
  border-bottom: 1px #dddee1 solid;
  .avatar, .info, .button-handle {
    display: inline-block;
    height: 100%;
  }
  .avatar {
    .avatar-content {
      height: 70px;
      width: 70px;
      // background: #969696;
      position: relative;
      margin: 0 auto;
      border-radius: 5px;
    }
  }
  .info {
    >div{
      margin-bottom: 5px;
    }
    .user-name{
      cursor: pointer;
      font-size: 1.3em;
      font-weight: bold;
      line-height: 100%;
    }
    .user-name:hover {
      color:#175199;
    }
    .description{
      font-size: 15px;
      color: #555;
    }
    .detail{
      color: #8590a6;
      font-size: 14px; 
      span{
        margin: 0 5px;
      }
      span:not(:first-child):before {
        margin: 0 5px;
        content: "\B7";
      }
    }
  }
  .button-handle {
    .watch-button{
      width: 80%;
      position: relative;
      top: 50%;
      transform: translateY(-50%);
    }
    .watch-button:hover span:nth-child(2){
      display: inline !important;
    }
    .watch-button:hover span:nth-child(1){
      display: none !important;
    }
  }
}
</style>
