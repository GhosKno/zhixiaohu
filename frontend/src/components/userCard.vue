<template>
  <div class="user-card">
    <Row style="height:100%;">
    <Col span="5" class="avatar">
      <div class="avatar-content"></div>
    </Col>
    <Col span="14" class="info">
      <div class="user-name">{{userName}}</div>
      <div class="description">{{description}}</div>
      <!-- <div class="detail">
        <span>{{answer}}*回答</span>
        <span>{{watched}}*关注者</span>
      </div> -->
    </Col>
    <Col span="5" class="button-handle">
      <Button 
        size="large" 
        class="watch-button"
        @click="cancelWatchPeople()"
      >
        <span>已关注</span>
        <span style="display:none;">取消关注</span>
      </Button>
    </Col>
    </Row>
  </div>
</template>


<script>
  export default {
    name: 'userCard',
    data() {
      return {}
    },
    props: {
      userName: {
        type: String,
        required: true
      },
      description: {
        type: String,
        required: true
      },
      // answer: {
      //   type: Number,
      //   required: true
      // },
      // watched: {
      //   type: Number,
      //   required: true
      // }
    },
    methods: {
      cancelWatchPeople() {

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
      background: #969696;
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
      font-size: 1.3em;
      font-weight: bold;
      line-height: 100%;
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
