<template>
  <div class="toolBar">
   <div class="btn-group" v-if="question">
      <Button type="primary">关注问题</Button>
      <Button type="ghost" class="writeBtn"><svg viewBox="0 0 12 12" class="writeIcon" width="14" height="16" aria-hidden="true"><g data-reactid="108"><path d="M.423 10.32L0 12l1.667-.474 1.55-.44-2.4-2.33-.394 1.564zM10.153.233c-.327-.318-.85-.31-1.17.018l-.793.817 2.49 2.414.792-.814c.318-.328.312-.852-.017-1.17l-1.3-1.263zM3.84 10.536L1.35 8.122l6.265-6.46 2.49 2.414-6.265 6.46z" fill-rule="evenodd"></path></g></svg>
        写回答
      </Button>
   </div>
   <!-- 点赞 -->
   <div class="btn-group" v-else>
      <Button class="voteBtn"><Icon type="arrow-up-b" class="voteIcon" size=16></Icon>
        <span class="voteNum">1.7k</span>
      </Button>
      <Button class="voteBtn"><Icon type="arrow-down-b" class="voteIcon" size=16></Icon></Button>
   </div>
      <Button type="text" class="actionBtn" @click="toggleComment"><svg class="actionIcon" fill="currentColor" viewBox="0 0 24 24" width="1.2em" height="1.2em"><path d="M10.241 19.313a.97.97 0 0 0-.77.2 7.908 7.908 0 0 1-3.772 1.482.409.409 0 0 1-.38-.637 5.825 5.825 0 0 0 1.11-2.237.605.605 0 0 0-.227-.59A7.935 7.935 0 0 1 3 11.25C3 6.7 7.03 3 12 3s9 3.7 9 8.25-4.373 9.108-10.759 8.063z" fill-rule="evenodd"></path></svg>
        {{commentBtn}}
      </Button>
      <Button type="text" class="actionBtn">
        <svg class="actionIcon" viewBox="0 0 24 24"><path d="M2.931 7.89c-1.067.24-1.275 1.669-.318 2.207l5.277 2.908 8.168-4.776c.25-.127.477.198.273.39L9.05 14.66l.927 5.953c.18 1.084 1.593 1.376 2.182.456l9.644-15.242c.584-.892-.212-2.029-1.234-1.796L2.93 7.89z" fill-rule="evenodd"></path></svg>
        分享
      </Button>
      <Button type="text" class="actionBtn" v-if="question">
        <svg class="actionIcon" viewBox="0 0 24 24" ><path d="M5.515 19.64l.918-5.355-3.89-3.792c-.926-.902-.639-1.784.64-1.97L8.56 7.74l2.404-4.871c.572-1.16 1.5-1.16 2.072 0L15.44 7.74l5.377.782c1.28.186 1.566 1.068.64 1.97l-3.89 3.793.918 5.354c.219 1.274-.532 1.82-1.676 1.218L12 18.33l-4.808 2.528c-1.145.602-1.896.056-1.677-1.218z" fill-rule="evenodd"></path></svg>
        邀请回答
      </Button>
      <Button type="text" class="actionBtn" v-else>
        <svg class="actionIcon" viewBox="0 0 24 24" ><path d="M5.515 19.64l.918-5.355-3.89-3.792c-.926-.902-.639-1.784.64-1.97L8.56 7.74l2.404-4.871c.572-1.16 1.5-1.16 2.072 0L15.44 7.74l5.377.782c1.28.186 1.566 1.068.64 1.97l-3.89 3.793.918 5.354c.219 1.274-.532 1.82-1.676 1.218L12 18.33l-4.808 2.528c-1.145.602-1.896.056-1.677-1.218z" fill-rule="evenodd"></path></svg>
        收藏
      </Button>
      <Button type="text" class="actionBtn">
        <svg class="actionIcon" viewBox="0 0 24 24"><path d="M5 14a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm7 0a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm7 0a2 2 0 1 1 0-4 2 2 0 0 1 0 4z" fill-rule="evenodd"></path></svg>
      </Button>
      <Button type="text" class="actionBtn right" v-show="!fold" @click="unfold">
          收起 <Icon type="chevron-up"></Icon>
      </Button>
<Modal v-model="showComment" v-if="question">
  <CommentList :numOfComment="numOfComment">
  </CommentList>
</Modal>
<div class="commentCard" v-else v-show="showComment">
  <CommentList :numOfComment="numOfComment">
  </CommentList>
  <div slot="footer"></div>
</div>
  </div>
</template>
<script>
const CommentList = resolve => require(["@/components/commentList"], resolve);

export default {
  name: "toolBar",
  components: { CommentList },
  methods: {
    toggleComment: function() {
      if (this.showComment) {
        if (this.numOfComment > 0) {
          this.commentBtn = this.numOfComment + " 条评论";
        } else {
          this.commentBtn = "评论";
        }
      } else if (!this.question){
        this.commentBtn = "收起评论";
      }
      this.showComment = !this.showComment;
    },
    unfold(){
      this.$emit('unfold')
    }
  },
  data() {
    return {
      showComment: false,
      commentBtn: "评论",
    };
  },
  props: {
    "question": {
      type: Boolean,
      default:false,
    },
    "numOfComment": {
      type:Number,
      default:0,
    },
    "fold":{
      type: Boolean,
      default: true,
    }
  },
  created() {
    if (this.numOfComment > 0) {
      this.commentBtn = this.numOfComment + " 条评论";
    } else {
      this.commentBtn = "评论";
    }
  }
};
</script>
<style scoped>
.toolBar {
  clear: both;
}
.btn-group{
  display: inline;
}
.voteBtn {
  line-height: 30px;
  padding: 0 12px;
  font-size: 14px;
  color: #2d84cc;
  background: #ebf3fb;
  border-color: #ebf3fb;
}
.voteBtn:hover {
  background-color: #e4ebf3;
  border-color: #e4ebf3;
}
.voteIcon {
  vertical-align: text-bottom;
}
.voteBtn.is-active {
  color: #eef3f7;
  background: #2d84cc;
  border-color: #2d84cc;
}
.voteNum {
  margin-left: 8px;
}
.actionBtn {
  display: inline-block;
  font-size: 14px;
  color: #8590a6;
  text-align: center;
  cursor: pointer;
}
.actionIcon {
  fill: #8590a6;
  width: 18px;
  height: 18px;
  margin-right: 4px;
  vertical-align: text-bottom;
}
.actionBtn:hover {
  color: #7a8599;
}
.writeIcon{
  fill: #2d84cc;
  vertical-align: text-bottom;
  height:16px;
  width:14px;
}
.writeBtn{
  color:#2d84cc;
}
.commentCard {
  border: 1px solid #e7eaf2;
  -webkit-box-shadow: 0 1px 3px 0 rgba(0, 33, 77, 0.05);
  box-shadow: 0 1px 3px 0 rgba(0, 33, 77, 0.05);
  background: #fff;
  margin-top: 12px;
  border-radius: 4px;
}
/* 隐藏 modal footer */
.ivu-modal-footer{
  display: none;
}
.right{
  float:right;
}
</style>

