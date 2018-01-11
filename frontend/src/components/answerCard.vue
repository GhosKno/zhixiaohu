<template>
<div class="answer" ref="answerCard">
    <div class="feed-title">
        {{feedTitle}}
    </div>
    <div class="info">
        <Poptip trigger="hover" 
            placement="right-start" 
            width="400"
            @on-popper-hide="() => $refs['userPoptip'].blur()"
            @on-popper-show="() => $refs['userPoptip'].load()">
            <Avatar class="avatar" shape="square" size="large"  :src="author.avatar"  />
            <div class="api" slot="content">
                <user-poptip ref="userPoptip" :id="author.id||0"></user-poptip>
            </div>
        </Poptip>
        <div class="author-text">
        <div class="name">
            {{author.nickname}}
        </div>
        <div class="badge-text">
            {{author.description||"这个人很懒,没有设置简介"}}
        </div>
        </div>
    </div>
    <TextWithToolBar 
        :text="answer.detail" 
        :commentCount="answer.comment_count"
        :postTime="answer.add_time"
        :approve="answer.approve"
        :hasApprove="answer.has_approve"
        :hasAgainst="answer.has_against"
        :hasFavorite="answer.has_favorite"
        :pk="answer.id"
        :isOwner="$store.state.userid == author.id"
        ></TextWithToolBar></div>
</template>
<script>
const TextWithToolBar = resolve => require(["@/components/textWithToolBar"], resolve);
const UserPoptip = resolve => require(["@/components/userPoptip"], resolve);
export default {
  name: "answerCard",
  components: { TextWithToolBar, UserPoptip},
  props:{
      feedTitle:{},
      answer:{required:true},
  },
  data() {
      return {
          author:{}
      }
  },
  methods: {
  },
  mounted(){
      this.author=this.answer.userSummary
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
