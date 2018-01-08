<template>
<div class="answer card" ref="answerCard">
    <div class="feed-title">
        {{feedTitle}}
    </div>
<div class="info">
    <Poptip trigger="hover" placement="right" width="400">
        <Avatar class="avatar" shape="square" size="small"  :src="authorAvatar"  />
        <div class="api" slot="content"> 
        </div>
    </Poptip>
    <div class="name">
        {{authorName}}
    </div>
    <div class="badge-text">
        {{authorBadge}}
    </div>
</div>
    <div class="question">
        <a :href="'/question/'+pk" class="title">{{question}}</a>
    </div>
    <TextWithToolBar 
        :text="answer" 
        :coverImg="coverImg" ></TextWithToolBar>
</div>
</template>
<script>
const TextWithToolBar = resolve => require(["@/components/textWithToolBar"], resolve);
export default {
  name: "answerListCard",
  components: { TextWithToolBar },
  props:{
      feedTitle:{
          type: String,
          default: ''
      },
      question:{
          type: String,
          default: "作为一个示例问题是怎样的体验?"
      },
      answer:{
          type: String,
          default: "泻药.这个答案是一个示例答案.这个示例答案很短."
      },
      pk:{
          type: Number | String,
          default: "0"
      },
      authorAvatar:{
          type: String,
          default: '/static/avatar.jpg',
      },
      authorName:{
          type: String,
          default: '匿名用户'
      },
      authorBadge:{
          type: String,
          default: ""
      },
      coverImg:{
          default:false
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
.answer{
    padding: 13px 18px;
    margin-top: 10px;
}
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
  color: #4a4a4a;
  font-size: 14px;
  line-height: 1.625;
  margin: 0;
  position: relative;
}
.title{
    font-size: 18px;
    font-weight: 600;
    font-synthesis: style;
    line-height: 1.6;
    color: #1e1e1e;
    margin-top: -4px;
    margin-bottom: -4px;
}
.title:hover{
    color:#175199;
}
.name{
    margin-left: 5px;
    display: inline;
    font-weight: 700;
    font-size: 15px;
    line-height: 24px;
}
.badge-text{
    display: inline;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    font-size: 14px;
    line-height: 24px;
}
.avatar{
    vertical-align: top;
}
</style>
