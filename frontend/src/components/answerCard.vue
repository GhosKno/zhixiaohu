<template>
<div class="answer" ref="answerCard">
    <div class="feed-title">
        {{feedTitle}}
    </div>
    <div class="info">
        <Poptip trigger="hover" placement="right" width="400">
            <Avatar class="avatar" shape="square" size="large"  :src="authorAvatar"  />
            <div class="api" slot="content">
                
            </div>
        </Poptip>
        <div class="author-text">
        <div class="name">
            {{authorName}}
        </div>
        <div class="badge-text">
            {{authorBadge}}
        </div>
        </div>
    </div>
    <div class="content">
        <div class="inner" v-if="fold">
        <span class="inner-text" >{{answer}}</span>
        <Button type="text" class="foldBtn" @click="toggleRead">
            展开阅读全文 <Icon type="chevron-down"></Icon>
        </Button>
        </div>
        <div class="inner" v-else>
            <span class="inner-text" >{{fullAnswer}}</span>
        </div>
    </div>
    <ToolBar :fold="fold" @unfold="toggleRead"></ToolBar>
</div>
</template>
<script>
const ToolBar = resolve => require(["@/components/toolBar"], resolve);
export default {
  name: "answerCard",
  components: { ToolBar },
  props:{
      'feedTitle':{},
      'question':{
          default: "作为一个示例问题是怎样的体验?"
      },
      'answer':{
          default: "泻药.这个答案是一个示例答案."
      },
      'pk':{
          default: "0"
      },
      'authorAvatar':{
          default: ('/static/avatar.jpg'),
      },
      'authorName':{
          default: 'hhh'
      },
      'authorBadge':{
          default: "已婚人士/专业数星星团队成员/编程狂热者/不只是Python/并行框架/DL爱好者"
      },
      'fold': {
          default: true,
      }
  },
  data() {
      return {
          fullAnswer: '',
      }
  },
  methods: {
      toggleRead:function(){
          if(this.fold){
             this.$http.get(`/api/answers/${this.pk}`)
                .then(res => {
                    if(res.body.success) {
                        this.fullAnswer=res.body.detail
                    } else {
                        this.$Message.error(res.data.msg)
                    }
                })
          }else{

          }
          this.fold=!this.fold;

      }
  }
};
</script>

<style scoped>
.feed-title {
  color: #8590a6;
  line-height: 1;
  font-weight: 500;
  font-size: 14px;
  margin-bottom: 10px;
}
.question {
  color: #000;
  margin: 8px 0;
  font-size: 18px;
  font-weight: 700;
}
.content {
  line-height: 1.625;
  margin: 0;
}
.foldBtn {
  display: block;
  width: 100%;
  padding: 0;
  margin: 20px;
  color: #175199;
  font-size: 15px;
}
.inner{
    margin: 5px 0;
}
.inner-text {
  font-size: 14px;
  font-weight: normal;
  line-height: 1.67;
  max-height: 100px;
  
  overflow: hidden;
}
.toolBar{
    background: #fff;
    padding: 5px 0;
}
.info{
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
</style>
