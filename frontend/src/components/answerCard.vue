<template>
<div class="answer" ref="answerCard">
    <div class="feed-title">
        {{feedTitle}}
    </div>
    <div class="info">
        <Poptip trigger="hover" placement="right" width="400">
            <Avatar class="avatar" shape="square" size="large"  :src="author.avatar?author.avatar:'/static/avatar.jpg'"  />
            <div class="api" slot="content">
                
            </div>
        </Poptip>
        <div class="author-text">
        <div class="name">
            {{author.nickname}}
        </div>
        <div class="badge-text">
            {{author.description?author.description:"这个人很懒,没有设置简介"}}
        </div>
        </div>
    </div>
    <TextWithToolBar 
        :text="answer" 
        :commentCount="commentCount"
        :postTime="answerTime"
        ></TextWithToolBar></div>
</template>
<script>
const TextWithToolBar = resolve => require(["@/components/textWithToolBar"], resolve);
export default {
  name: "answerCard",
  components: { TextWithToolBar },
  props:{
      feedTitle:{},
      answer:{
          default: "泻药.这个答案是一个示例答案."
      },
      pk:{
          default: "0"
      },
      author:{},
      commentCount:{},
      answerTime:{}
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
    color: #555;
}
</style>
