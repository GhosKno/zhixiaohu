<template>
  <div class="profile-edit">
    <Row>
      <Col span="18" offset="3" class="main-content">
        <div class="background"></div>
        <div class="edit-content">
          <Row>
            <Col span="6">
              <div class="avatar-content" :style="`background-image: url(${avatarUrl})`">
                <Upload
                  class="upload"
                  :headers="{
                    'X-CSRFTOKEN': this.$cookie.get('csrftoken'),
                  }"
                  action="/api/accounts/avatar/"
                >
                  <div style="padding-top: 40px;text-align: center;width: 160px;height: 160px;background: rgba(0, 0, 0, 0.5);">
                    <Icon type="camera" size="45"></Icon>
                    <p>修改我的头像</p>
                  </div>
              </Upload>
              </div>
            </Col>
            <Col span="18">
              <div class="content-header">
                <span>
                  {{nickName}}
                </span>
                <Button type="text" @click="$router.push({name: 'profile'})">
                  返回我的主页&nbsp;&nbsp;
                  <Icon type="chevron-right"></Icon>
                </Button>
              </div>
              <div class="edit-item">
                <Row>
                  <Col span="6" class="label">
                  昵称
                  </Col>
                  <Col span="18" class="detail">
                    <template v-if="!isEditNickName">
                      {{nickName}}
                      <Button type="text" class="edit-handle" icon="edit" @click="isEditNickName = true">修改</Button>
                    </template>                
                    <div class="edit-input" v-else>
                      <Input 
                        v-model="newNickName"
                        style="width: 200px;"
                      ></Input>
                      <div class="button-handle">
                        <Button @click="updateNickName()" type="primary">保存</Button>
                        <Button @click="isEditNickName = false">取消</Button>
                      </div>
                    </div>
                  </Col>
                </Row>
              </div>
              <div class="edit-item">
                <Row>
                  <Col span="6" class="label">
                  一句话介绍
                  </Col>
                  <Col span="18" class="detail">
                    <template v-if="!isEditDescription">
                      {{description}}
                      <Button type="text" class="edit-handle" icon="edit" @click="isEditDescription = true">修改</Button>
                    </template>                
                    <div class="edit-input" v-else>
                      <Input 
                        v-model="newDescription"
                        style="width: 200px;"
                      ></Input>
                      <div class="button-handle">
                        <Button @click="updatedescription()" type="primary">保存</Button>
                        <Button @click="isEditDescription = false">取消</Button>
                      </div>
                    </div>
                  </Col>
                </Row>
              </div>
            </Col>
          </Row>
        </div>
      </Col>
    </Row>
  </div>
</template>

<script>
import cookieManage from '@/mixins/cookieManage'
import initInfo from '@/mixins/initInfo'
export default {
  name: 'profileEdit',
  mixins: [cookieManage, initInfo],
  data() {
    return {
      nickName: '',
      description: '',
      isEditNickName: false,
      newNickName: '',
      isEditDescription: false,
      newDescription: '',
      avatarUrl: ''
    }
  },
  methods: {
    updateNickName() {
      this.$http.post()
    },
    updatedescription() {
      //todo update description
    }
  },
  created () {
    if(this.initInfo()){
      this.$http.get(`/api/accounts/profile/${this.$store.state.userid}/`)
      .then(res => {
        if(res.body.success) {
          let data = res.body.data
          this.nickName = data.nickname
          this.description = data.description.length == 0 ? "这个用户很懒，什么也没留下" : data.description
          this.newNickName = this.nickName
          this.newDescription = this.description
          this.avatarUrl = data.avatar || 'media/1.png'
        }
      })
    }
  }
}
</script>

<style lang="less" scoped>
.profile-edit {
  .main-content {
    margin-top: 60px;
    margin-bottom: 40px;
    background: #fff;
    box-shadow: 0 1px 3px rgba(0,0,0,.1);
  }
  .background {
    background: #f7f8fa;
    height: 240px;
  }
  .edit-content {
    background: #fff;
    margin-bottom: 60px;
    .avatar-content {
      height: 160px;
      width: 160px;
      // background: #969696;
      margin: 0 auto;
      background-repeat: no-repeat;
      background-size: cover;
      position: relative;
      top: -35px;
      border-radius: 10px;
      .upload , .upload>div{
        width: 100%;
        height: 100%;
      }
    }
    .content-header {
      margin-top: 20px;
      margin-bottom: 50px;
      span {
        font-size: 1.5em;
        font-weight: bold;
      }
      button {
        position: absolute;
        right: 0px;
      }
      .ivu-btn-text {
        color: #8590a6;
      }
      .ivu-btn-text:hover {
        color: #62a1e9;
        background-color: transparent;
        border-color: transparent;
      }
    }
    // .edit-item:last-child{
    //   border-bottom: 0px;
    // }
    .edit-item {
      border-bottom: 1px solid #dddee1;
      >div {
        height: 30px;
        position: relative;
        top: 50%;
        transform: translateY(-50%);  
      }
      margin-top: 20px;
      min-height: 100px;
      padding-top: 30px;
      .label {
        font-size: 1em;
        font-weight: bold;
        padding-left: 30px;
      }
      .detail {
        .edit-handle{
          display: none;
          padding: 0 0 0 10px;
        }
        .edit-input {
          .button-handle {
            margin: 10px 0;
          }
        }
      }
      .detail:hover>.edit-handle{
        display: inline !important;
      }
    }
  }
}
</style>

