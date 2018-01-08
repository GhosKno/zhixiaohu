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
    <TextWithToolBar :text="answer" ></TextWithToolBar></div>
</template>
<script>
const TextWithToolBar = resolve => require(["@/components/textWithToolBar"], resolve);
export default {
  name: "answerCard",
  components: { TextWithToolBar },
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
      }
  },
  data() {
      return {
          
      }
  },
  methods: {
  },
  mounted(){
      
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
