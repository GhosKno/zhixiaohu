<template>
<div>
    <div class="text" ref="foldText" :class="{'is-fold':fold}">
        <div class="cover-img" :style="'background-image:url(' + coverImg + ');'" v-if="coverImg"></div>
        <span v-html="text"></span>
    </div>
    <div class="time">发布于{{this.timeago(postTime)}}</div>
    <ToolBar class="tool-bar"
        :fold="fold" 
        :forQuestion="forQuestion" 
        :showFoldBtn="FoldByDefault"
        :commentCount="commentCount"
        @toggleFold="fold=!fold;"
        @writeAnswer="$emit('writeAnswer')"
        @cancelWatch="$emit('cancelWatch')"
        @watch="$emit('watch')"
        :approve="approve"
        :hasApprove="hasApprove"
        :hasAgainst="hasAgainst"
        :pk="pk"
        :isWatch="isWatch"
        :isOwner="isOwner"></ToolBar>
</div>
</template>
<script>
const ToolBar = resolve => require(["@/components/toolBar"], resolve);
export default {
  name: "textWithToolBar",
  components: { ToolBar },
  props:{
      text:{},
      forQuestion:{
          default:false
      },
      coverImg:{
          default: false
      },
      commentCount:{},
      postTime:{},
      approve:{},
      pk:{},
      isWatch:{},
      hasApprove:{},
      hasAgainst:{},
      isOwner:{}
  },
  data() {
      return {
          fullAnswer: '',
          FoldByDefault: false,
          fold: true
      }
  },
  methods: {
    showFoldBtnFun: function(){ 
        var t=this.$refs.foldText
        this.FoldByDefault = (t && t.scrollHeight > 85);
    },
  },
  mounted(){
      setTimeout(()=>{
          this.showFoldBtnFun();
      },500)
  }
};
</script>

<style scoped>
.text {
  font-size: 15px;
  font-weight: normal;
  line-height: 1.67;
  margin: 5px 0;
}
.is-fold{
    max-height: 70px;
    overflow: hidden;
}
.tool-bar{
    background: #fff;
    padding: 5px 0;
}
.cover-img {
  position: relative;
  width: 190px;
  height: 105px;
  margin-right: 15px;
  float: left;
  overflow: hidden;
  background-position: 50%;
  background-size: cover;
  border-radius: 4px;
}
.time{
    margin-top: 10px;
    font-size: 14px;
    color: #8590a6;
}
</style>
