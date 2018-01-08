<template>
  <div class="answer-card">
      <div class="info">
        <Avatar class="avatar" shape="square" size="large"  :src="authorAvatar"  />
        <div class="author-text">
            <div class="name">
                {{authorName}}
            </div>
            <div class="badge-text">
                {{authorBadge}}
            </div>
        </div>
      </div>
      <common-editor
          ref="quillEditor"
          placeholder="在这里写下你的回答"
        ></common-editor>
    <Button type="primary" class="postBtn" @click="postAnswer">提交回答</Button>
  </div>
</template>
<script>
import commonEditor from '@/components/commonEditor'
export default {
  name: 'AnswerEditor',
  components: {
    commonEditor
  },
  props: {
      authorAvatar:{
          default: ('/static/avatar.jpg'),
      },
      authorName:{
          default: 'hhh'
      },
      authorBadge:{
          default: "已婚人士/专业数星星团队成员/编程狂热者/不只是Python/并行框架/DL爱好者"
      },
      pk: {}
  },
  data(){
      return {
        answerForm: {
            question: this.pk,
            detail: ''
        },
      }
  },
  methods:{
      postAnswer: function(){
        this.answerForm.detail = this.$refs['quillEditor'].getHtmlContent()
        console.log(this.answerForm)
        this.$http.post(`/api/answers/`, this.answerForm)
          .then(res => {
            if(res.body.success==true) {
              this.$Message.success("回答成功");
            } else {
              this.$Message.error(res.body.msg);
            }
          }, function(response){
            // 响应错误回调 
            this.$Message.error(response.status+" "+response.statusText);
          });
    }
  },
}
</script>
<style scoped>
.answer-card{
    padding: 5px 15px;
}
.info{
    margin: 10px 0;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
}
.author-text{
    margin-left: 5px;
}
.name{
    font-weight: 700;
    font-size: 15px;
    line-height: 24px;
}
.badge-text{
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    font-size: 14px;
    line-height: 24px;
}
.postBtn{
    float: right;
    margin: 5px;
}
</style>
