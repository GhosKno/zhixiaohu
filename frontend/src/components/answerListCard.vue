<template>
<div class="card answer">
    <div class="feed-title">
        {{feedTitle}}
    </div>
    <AuthorInfo></AuthorInfo>
    <div class="question">
        {{question}}
    </div>
    <div class="content">
        <div class="cover" v-show="coverImg" ><img width="190" :src="coverImg">
        </div>
        <div class="inner">
        {{answer}}
        <Button type="text" class="read-all">阅读全文 <Icon type="chevron-down"></Icon></Button>
        </div>
        <ToolBar></ToolBar>
    </div>
</div>
</template>
<script>
const AuthorInfo = resolve => require(["@/components/authorInfo"], resolve);
const ToolBar = resolve => require(["@/components/toolBar"], resolve);
export default {
  name: "answerListCard",
  components: { AuthorInfo, ToolBar },
  props:{
      'feedTitle':{},
      'question':{
          default: "作为一个示例问题是怎样的体验?"
      },
      'coverImg':{
          default: false
      },
      'answer':{
          default: "泻药.这个答案是一个示例答案."
      }
  }
};
</script>

<style scoped>
.card{
    padding: 13px 18px;
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
}
.read-all {
  padding: 0;
  margin-left: 4px;
  color: #175199;
}
.cover {
  position: relative;
  width: 190px;
  height: 105px;
  margin-top: -2px;
  margin-right: 18px;
  margin-bottom: 4px;
  float: left;
  overflow: hidden;
  background-position: 50%;
  background-size: cover;
  border-radius: 4px;
  -webkit-transform: translateZ(0);
  transform: translateZ(0);
}
.inner {
  font-size: 14px;
  font-weight: normal;
  line-height: 1.67;
  max-height: 100px;
  margin-bottom: -4px;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 4;
  overflow: hidden;
}
</style>
