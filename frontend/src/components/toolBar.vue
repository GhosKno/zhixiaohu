<template>
  <div class="toolBar">
      <Button class="voteBtn"><Icon type="arrow-up-b" class="voteIcon" size=16></Icon><span class="voteNum">1.7k</span></Button>
      <Button class="voteBtn"><Icon type="arrow-down-b" class="voteIcon" size=16></Icon></Button>
      <Button type="text" class="actionBtn" @click="commentBtn=(showComment?'评论':'收起评论');showComment=!showComment;"><svg class="actionIcon" fill="currentColor" viewBox="0 0 24 24" width="1.2em" height="1.2em"><path d="M10.241 19.313a.97.97 0 0 0-.77.2 7.908 7.908 0 0 1-3.772 1.482.409.409 0 0 1-.38-.637 5.825 5.825 0 0 0 1.11-2.237.605.605 0 0 0-.227-.59A7.935 7.935 0 0 1 3 11.25C3 6.7 7.03 3 12 3s9 3.7 9 8.25-4.373 9.108-10.759 8.063z" fill-rule="evenodd"></path></svg>{{commentBtn}}</Button>
      <Button type="text" class="actionBtn"><svg class="actionIcon" fill="currentColor" viewBox="0 0 24 24" width="1.2em" height="1.2em"><path d="M2.931 7.89c-1.067.24-1.275 1.669-.318 2.207l5.277 2.908 8.168-4.776c.25-.127.477.198.273.39L9.05 14.66l.927 5.953c.18 1.084 1.593 1.376 2.182.456l9.644-15.242c.584-.892-.212-2.029-1.234-1.796L2.93 7.89z" fill-rule="evenodd"></path></svg> 分享</Button>
      <Button type="text" class="actionBtn"><svg class="actionIcon" fill="currentColor" viewBox="0 0 24 24" width="1.2em" height="1.2em"><path d="M5.515 19.64l.918-5.355-3.89-3.792c-.926-.902-.639-1.784.64-1.97L8.56 7.74l2.404-4.871c.572-1.16 1.5-1.16 2.072 0L15.44 7.74l5.377.782c1.28.186 1.566 1.068.64 1.97l-3.89 3.793.918 5.354c.219 1.274-.532 1.82-1.676 1.218L12 18.33l-4.808 2.528c-1.145.602-1.896.056-1.677-1.218z" fill-rule="evenodd"></path></svg> 收藏</Button>
      <Button type="text" class="actionBtn"><svg class="actionIcon" fill="currentColor" viewBox="0 0 24 24" width="1.2em" height="1.2em"><path d="M5 14a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm7 0a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm7 0a2 2 0 1 1 0-4 2 2 0 0 1 0 4z" fill-rule="evenodd"></path></svg></Button>
  <CommentList numOfComment="14" v-show="showComment">

  </CommentList>
  </div>
</template>
<script>
const CommentList = resolve => require(["@/components/commentList"], resolve);

export default {
  name:'toolBar',
  components: { CommentList },
  data() {
    return {
        showComment: false,
        commentBtn: '评论'
    }
},
}
</script>
<style>
.toolBar{
    margin-top: 10px;
    clear: both;
}
.voteBtn{
    line-height: 30px;
    padding: 0 12px;
    font-size: 14px;
    color: #2d84cc;
    background: #ebf3fb;
    border-color: #ebf3fb;
}
.voteBtn:hover{
    background-color: #e4ebf3;
    border-color: #e4ebf3;
}
.voteIcon{
    vertical-align: text-bottom;
}
.voteBtn.is-active{
    color: #eef3f7;
    background: #2d84cc;
    border-color: #2d84cc;
}
.voteNum{
    margin-left: 8px;
}
.actionBtn{
    display: inline-block;
    font-size: 14px;
    color: #8590a6;
    text-align: center;
    cursor: pointer;
}
.actionIcon{
    margin-right: 4px;
    vertical-align: text-bottom;
}

.actionBtn:hover{
    color:#7a8599;
}
</style>

