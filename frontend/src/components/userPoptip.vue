<template>
  <div class="user-poptip">
    <Spin v-if="loading" size="large" fix></Spin>
    <div class="top-info">
      <Row>
        <Col span="5" class="avatar-content">
          <img :src="user.avatar || '/static/avatar.jpg'">
        </Col>
        <Col span="19" class="info-content">
          <div class="nickname" @click="$router.push({path: `/profile/${id}`})">
            {{user.nickname}}
          </div>
          <div class="description">
            {{user.description}}
          </div>
        </Col>
      </Row>
    </div>
    <div class="bottom-info">
      <Row>
        <Col span="8">
          <div class="title">回答</div>
          <div class="count">{{user.answerCount}}</div>
        </Col>
        <Col span="8">
          <div class="title">关注了</div>
          <div class="count">{{user.watchCount}}</div>
        </Col>
        <Col span="8">
          <div class="title">关注者</div>
          <div class="count">{{user.beWatchCount}}</div>
        </Col>
      </Row>
    </div>
  </div>
</template>

<script>
export default {
  name: 'userPopTipContent',
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  data () {
    return {
      user: {
        avatar: '/static/avatar.jpg',
        nickname: '小看山',
        description: 'null',
        answerCount: 0,
        watchCount: 0,
        beWatchCount: 0
      },
      loading: true
    }
  },
  methods: {
    load() {
      this.loading = true
      this.$http.get(`/api/profiles/${this.id}/`)
        .then(res => {
          this.user = res.body.data
          setTimeout(() => {
            this.loading = false
          }, 1000)
        })
    },
    blur() {
      this.loading = true
    }
  },
  created () {
    // this.load()
  }
}
</script>


<style lang="less" scoped>
.user-poptip {
  .top-info {
    width: 95%;
    margin: 0 auto;
    padding-bottom: 15px;
    margin-bottom: 15px;
    border-bottom: 1px #dddee1 solid;
    .avatar-content {
      height: 60px;
      margin: 0 auto;
      width: 60px;
      img {
        height: 100%;
        width: 100%;
      }
    }
    .info-content {
      padding-left: 20px;
      .nickname {
        cursor: pointer;
        font-size: 1.2em;
        font-weight: bold;
      } 
      .description {
        margin-top:5px;
      }
    }
  }
  .bottom-info {
    margin-bottom: 20px;
    .title, .count {
      text-align: center;
      cursor: pointer;
    }
    .title:hover + .count, .title:hover, .count:hover + .title, .count:hover{
      color: #175199 !important;
    }
    .title {
      font-size: 14px;
      color: #8590a6;
    }
    .count {
      margin-top: 5px;
      font-weight: bold;
      font-size: 20px;
      color: #262626; 
    }
  }
}
</style>

