<template>
<div class="answer card" ref="answerCard">
    <div class="feed-title">
        {{feedTitle}}
    </div>
<div class="info">
    <Poptip 
        trigger="hover" 
        placement="right-start"
        @on-popper-hide="() => $refs['userPoptip'].blur()"
        @on-popper-show="() => $refs['userPoptip'].load()"
        width="400">
        <Avatar class="avatar" shape="square" size="small"  :src="author.avatar||require('@/assets/avatar.jpg')"  />
        <div class="api" slot="content"> 
            <user-poptip ref="userPoptip" :id="author.id||0"></user-poptip>
        </div>
    </Poptip>
    <div class="name">
        {{author.nickname}}
    </div>
    <div class="badge-text">
        {{author.description}}
    </div>
</div>
    <div class="question">
        <a :href="'/question/'+answer.question.id" class="title">{{answer.question.title}}</a>
    </div>
    <TextWithToolBar 
        :text="answer.detail" 
        :commentCount="answer.comment_count"
        :postTime="answer.add_time"
        :approve="answer.approve"
        :pk="answer.id"
        :coverImg="answer.coverImg"
        :hasApprove="answer.has_approve"
        :hasAgainst="answer.has_against"
        :hasFavorite="answer.has_favorite"
        :isOwner="$store.state.userid == author.id"
        :copyText="copyText"></TextWithToolBar>
</div>
</template>
<script>
const TextWithToolBar = resolve => require(["@/components/textWithToolBar"], resolve);
const UserPoptip = resolve => require(["@/components/userPoptip"], resolve);
export default {
  name: "answerListCard",
  components: { TextWithToolBar, UserPoptip },
  props:{
      feedTitle:'',
      answer:{required:true}
  },
  data() {
      return {
          author:{},
          copyText:{},
      }
  },
  computed: {
  },
  methods: {
      
  },
  mounted(){
      this.author=this.answer.userSummary
      this.copyText=this.answer.question.title+' '+this.author.nickname+'的回答 - 知小乎' + window.location.href
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
