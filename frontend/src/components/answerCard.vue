<template>
<div ref="answerCard" :class="{'card':showQuestion}">
    <div class="feed-title">
        {{feedTitle}}
    </div>
    <div class="info" v-if="author">
      <Poptip trigger="hover" width="400"
          placement="right-start" 
          @on-popper-hide="() => $refs['userPoptip'].blur()"
          @on-popper-show="() => $refs['userPoptip'].load()">
          <Avatar class="avatar" shape="square" size="large"  :src="author.avatar"  />
          <div class="api" slot="content">
              <user-poptip ref="userPoptip" :id="author.id"></user-poptip>
          </div>
      </Poptip>
      <div class="author-text">
      <div class="name">
          <span style="cursor:pointer;" @click="$router.push({path: '/profile/'+author.id})">{{author.nickname}}</span>
      </div>
      <div class="badge-text">
          {{author.description||"这个人很懒,没有设置简介"}}
      </div>
      </div>
    </div>
    <div class="question" v-if="answer && showQuestion">
        <a @click="$router.push({path:'/question/'+answer.question.id+'/answer/'+answer.id})" class="title">{{answer.question.title}}</a>
    </div>
    <TextWithToolBar 
        v-if="answer"
        :text="answer.detail" 
        :numOfComment="answer.comment_count"
        :postTime="answer.add_time"
        :approve="answer.approve"
        :hasApprove="answer.has_approve"
        :hasAgainst="answer.has_against"
        :hasFavorite="answer.has_favorite"
        @closeWriteAnswer="$emit('closeWriteAnswer')"
        :pk="answer.id"
        :isOwner="$store.state.userid == author.id"
        :fold="fold"
        :copyText="copyText"></TextWithToolBar></div>
</template>
<script>
const TextWithToolBar = resolve =>
  require(["@/components/textWithToolBar"], resolve);
const UserPoptip = resolve => require(["@/components/userPoptip"], resolve);
export default {
  name: "answerCard",
  components: { TextWithToolBar, UserPoptip },
  props: {
    feedTitle: "",
    answer: { default: null },
    fold: { default: true },
    showQuestion: { default: true }
  },
  computed: {
    author(){
      if (this.answer)
         return this.answer.userSummary;
      return null
    },
    copyText(){
      if (this.answer){
        return this.answer.question.title +
          " " +
          this.author.nickname +
          "的回答 - 知小乎 http://" +
          window.location.host +
          "/question/" +
          this.answer.question.id +
          "/answer/" +
          this.answer.id;
      }
      return ""
    }
  },
};
</script>

<style scoped>
.card{
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
.content {
  line-height: 1.625;
  margin: 0;
}
.question {
  margin: 8px 0;
}
.title {
  font-size: 18px;
  font-weight: 600;
  color: #1e1e1e;
}
.title:hover {
  color: #175199;
}
.info {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
}
.author-text {
  margin-left: 5px;
}
.name {
  font-weight: 700;
  font-size: 15px;
  line-height: 24px;
}
.badge-text {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  font-size: 14px;
  line-height: 24px;
  color: #555;
}
</style>
