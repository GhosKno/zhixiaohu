<template>
<div class="answer card" ref="answerCard">
    <div class="feed-title">
        {{feedTitle}}
    </div>
    <AuthorInfo :authorAvatar="aavatar" :authorName="aname"></AuthorInfo>
    <div class="question">
        <a :href="'/question/'+pk" class="title">{{question}}</a>
    </div>
    <div class="content">
        <div class="cover" v-show="coverImg" ><img width="190" :src="coverImg">
        </div>
        <div class="inner">
        <span class="inner-text">{{answer}}</span>
        <Button type="text" class="foldBtn" v-if="fold" @click="toggleRead">
            阅读全文 <Icon type="chevron-down"></Icon>
        </Button>
        </div>
    </div>
    <ToolBar :fold="fold" @unfold="toggleRead"></ToolBar>
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
      },
      'pk':{
          default: "0"
      },
      'aavatar':{
          default: ('/static/avatar.jpg'),
      },
      'aname':{
          default: 'hhh'
      },
  },
  data() {
      return {
          fold: true,
      }
  },
  methods: {
      toggleRead:function(){
          if(this.fold){
             this.$http.get('/api/questions/'+this.pk)
                .then(res => {
                    if(res.body.success) {
                    this.$Message.success('登陆成功')
                    Vue.http.headers.common['X-CSRF-TOKEN'] = this.$cookie.get('csrftoken')
                    this.setCookie(true, res.body.data.id, res.body.data.nickname)
                    this.$store.commit('LOGIN')
                    this.$store.commit('USER', {id: res.body.data.id, name: res.body.data.nickname})
                    this.$router.push({name: 'home'})
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
.foldBtn {
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
.inner-text {
  font-size: 14px;
  font-weight: normal;
  line-height: 1.67;
  max-height: 100px;
  margin-bottom: -4px;
  overflow: hidden;
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
.toolBar{
    background: #fff;
    padding: 5px;
}
</style>
