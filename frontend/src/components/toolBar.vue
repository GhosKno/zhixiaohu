<template>
  <div class="toolBar">
    
   <div class="btn-group" v-if="forQuestion">
      <Button v-if="newIsWatch" @click="cancelWatchQuestion()">取消关注</Button>
      <Button type="primary" @click="watchQuestion()" v-else>关注问题</Button>
      <Button type="ghost" class="writeBtn" @click="$emit('writeAnswer')"><svg viewBox="0 0 12 12" class="writeIcon" width="14" height="16" aria-hidden="true"><g data-reactid="108"><path d="M.423 10.32L0 12l1.667-.474 1.55-.44-2.4-2.33-.394 1.564zM10.153.233c-.327-.318-.85-.31-1.17.018l-.793.817 2.49 2.414.792-.814c.318-.328.312-.852-.017-1.17l-1.3-1.263zM3.84 10.536L1.35 8.122l6.265-6.46 2.49 2.414-6.265 6.46z" fill-rule="evenodd"></path></g></svg>
        写回答
      </Button>
   </div>
   <div class="btn-group" v-else>
      <Button class="voteBtn" :class="{'is-active': newHasApprove}" :disabled="isOwner" @click="newHasApprove?postCancelApprove():postApprove()"><Icon type="arrow-up-b" class="voteIcon" size=16></Icon>
        <span class="voteNum">{{newApprove}}</span>
      </Button>
      <Button class="voteBtn" :class="{'is-active': newHasAgainst,'is-disappear': isOwner} " @click="newHasAgainst?postCancelAgainst():postAgainst()"><Icon type="arrow-down-b" class="voteIcon" size=16></Icon></Button>
   </div>
      <Button type="text" class="actionBtn" @click="toggleComment"><svg class="actionIcon" fill="currentColor" viewBox="0 0 24 24" width="1.2em" height="1.2em"><path d="M10.241 19.313a.97.97 0 0 0-.77.2 7.908 7.908 0 0 1-3.772 1.482.409.409 0 0 1-.38-.637 5.825 5.825 0 0 0 1.11-2.237.605.605 0 0 0-.227-.59A7.935 7.935 0 0 1 3 11.25C3 6.7 7.03 3 12 3s9 3.7 9 8.25-4.373 9.108-10.759 8.063z" fill-rule="evenodd"></path></svg>
        {{commentBtn}}
      </Button>
      <Dropdown trigger="click" :transfer="true" @on-click="share">
        <Button type="text" class="actionBtn">
          <svg class="actionIcon" viewBox="0 0 24 24"><path d="M2.931 7.89c-1.067.24-1.275 1.669-.318 2.207l5.277 2.908 8.168-4.776c.25-.127.477.198.273.39L9.05 14.66l.927 5.953c.18 1.084 1.593 1.376 2.182.456l9.644-15.242c.584-.892-.212-2.029-1.234-1.796L2.93 7.89z" fill-rule="evenodd"></path></svg>
          分享
        </Button>
        <DropdownMenu slot="list">
            <DropdownItem name="copy" class="copyBtn" :data-clipboard-text="copyText" >
              <svg class="copyLinkIcon" viewBox="0 0 24 24"><path d="M6.77 17.23c-.905-.904-.94-2.333-.08-3.193l3.059-3.06-1.192-1.19-3.059 3.058c-1.489 1.489-1.427 3.954.138 5.519s4.03 1.627 5.519.138l3.059-3.059-1.192-1.192-3.059 3.06c-.86.86-2.289.824-3.193-.08zm3.016-8.673l1.192 1.192 3.059-3.06c.86-.86 2.289-.824 3.193.08.905.905.94 2.334.08 3.194l-3.059 3.06 1.192 1.19 3.059-3.058c1.489-1.489 1.427-3.954-.138-5.519s-4.03-1.627-5.519-.138L9.786 8.557zm-1.023 6.68c.33.33.863.343 1.177.029l5.34-5.34c.314-.314.3-.846-.03-1.176-.33-.33-.862-.344-1.176-.03l-5.34 5.34c-.314.314-.3.846.03 1.177z" fill-rule="evenodd"></path></svg>
               复制链接
            </DropdownItem>
            <DropdownItem name="weibo" >
              <svg viewBox="0 0 22 18" class="weiboIcon" aria-hidden="true">
              <g fill-rule="evenodd">
              <path d="M14.518.06s-.87.644.03 1.71c0 0 6.287-1.19 5.69 6.33 0 0 1.05 1.13 1.674-.31 0 .002 1.44-8.584-7.394-7.73zM4.883 13.17s.038 2.584 3.326 2.584c3.657 0 3.683-2.98 3.683-2.98S12.1 9.67 8.687 9.61c-3.863-.07-3.804 3.56-3.804 3.56zM7.41 14.21c-.668 0-1.214-.447-1.214-.998 0-.55.543-.998 1.215-.998.67 0 1.213.447 1.213.998 0 .55-.54.998-1.212.998z"></path>
              <path d="M4.317 4.52C-2.603 10.353.873 14.85.873 14.85c.57 1.01 3.382 3.1 8.596 3.1 5.21 0 9.314-3.628 9.314-6.44 0-2.813-2.918-2.714-2.918-2.714 1.04-1.554.19-2.65.19-2.65-1.684-2.118-5.404-.16-5.407-.158.772-1.717.11-2.797.11-2.797C8.932.66 4.317 4.52 4.317 4.52zm10.448 7.79s-.467 4.16-6.447 4.16c-5.745 0-5.82-3.322-5.842-3.712 0 0-.073-4.423 6.58-4.654 5.94-.204 5.71 4.207 5.71 4.207zM18.65 7.045s1.018-4.37-3.864-3.818c0 0-.628.58.09 1.346 0 0 2.602-.58 2.397 2.598 0 0 .715.885 1.376-.125z"></path>
              </g>
              </svg>
               新浪微博
            </DropdownItem>
            <DropdownItem name="weixin" >
              <svg viewBox="0 0 20 19" class="weixinIcon" aria-hidden="true"><g><path fill-rule="evenodd" d="M.224 18.667s4.24-1.825 4.788-2.056C13.03 20.14 20 14.715 20 8.9 20 3.984 15.523 0 10 0S0 3.984 0 8.898c0 1.86.64 3.585 1.737 5.013-.274.834-1.513 4.757-1.513 4.757zM6.167 8.96c.69 0 1.25-.57 1.25-1.27 0-.703-.56-1.272-1.25-1.272s-1.25.57-1.25 1.27c0 .703.56 1.272 1.25 1.272zm7.583 0c.69 0 1.25-.57 1.25-1.27 0-.703-.56-1.272-1.25-1.272s-1.25.57-1.25 1.27c0 .703.56 1.272 1.25 1.272z"></path></g>
              </svg>
               微信好友
            </DropdownItem>
        </DropdownMenu>
    </Dropdown>
      <span v-if="!forQuestion">
        <Button type="text" class="actionBtn" @click="addFavorite()">
          <svg class="actionIcon" viewBox="0 0 24 24" ><path d="M5.515 19.64l.918-5.355-3.89-3.792c-.926-.902-.639-1.784.64-1.97L8.56 7.74l2.404-4.871c.572-1.16 1.5-1.16 2.072 0L15.44 7.74l5.377.782c1.28.186 1.566 1.068.64 1.97l-3.89 3.793.918 5.354c.219 1.274-.532 1.82-1.676 1.218L12 18.33l-4.808 2.528c-1.145.602-1.896.056-1.677-1.218z" fill-rule="evenodd"></path></svg>
          收藏
        </Button>
        <Button type="text" class="actionBtn">
          <Dropdown trigger="click">
              <svg class="actionIcon" viewBox="0 0 24 24"><path d="M5 14a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm7 0a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm7 0a2 2 0 1 1 0-4 2 2 0 0 1 0 4z" fill-rule="evenodd"></path></svg>
              <DropdownMenu slot="list" v-if="isOwner">
                  <DropdownItem >删除</DropdownItem>
                  <DropdownItem>修改</DropdownItem>
              </DropdownMenu>
              <DropdownMenu slot="list" v-else>
                  <DropdownItem>举报</DropdownItem>
                  <DropdownItem>没有帮助</DropdownItem>
              </DropdownMenu>
          </Dropdown>
          <Poptip title="提示标题" content="提示内容">
          </Poptip>
        </Button>
      </span>
      <Button type="text" class="actionBtn right" v-if="showFoldBtn" @click="toggleFold">
          <span v-if="fold">展开全文 <Icon type="chevron-down"></Icon></span>
          <span v-else>收起 <Icon type="chevron-up"></Icon></span>
      </Button>

<Modal v-model="showComment" v-if="forQuestion">
  <CommentList :commentCount="commentCount" :pk="pk" :comments="comments">
  </CommentList>
</Modal>
<div class="commentCard" v-else v-show="showComment">
  <CommentList :commentCount="commentCount" :pk="pk" :comments="comments">
  </CommentList>
  <div slot="footer"></div>
</div>
  </div>
</template>
<script>
const CommentList = resolve => require(["@/components/commentList"], resolve);
import Clipboard from 'clipboard';
export default {
  name: "toolBar",
  components: { CommentList },
  data() {
    return {
      showComment: false,
      commentBtn: "评论",
      comments: [],
      newHasApprove: {
        type: Boolean
      },
      newHasAgainst: {
        type: Boolean
      },
      newApprove: {
        type: Number,
        default: 0
      },
      newIsWatch: {
        type: Boolean
      },
      copyText: document.title + window.location.href,
    };
  },
  props: {
    hasApprove: {
      type: Boolean
    },
    hasAgainst: {
      type: Boolean
    },
    approve: {
      type: Number,
      default: 0
    },
    forQuestion: {
      type: Boolean,
      default: false
    },
    fold: {
      type: Boolean,
      default: true
    },
    showFoldBtn: {
      default: true
    },
    commentCount: {},
    pk: {},
    isWatch: {
      type: Boolean,
      default: false
    },
    isOwner: {}
  },
  methods: {
    toggleComment: function() {
      if (this.showComment) {
        if (this.commentCount > 0) {
          this.commentBtn = this.commentCount + " 条评论";
        } else {
          this.commentBtn = "评论";
        }
      } else if (!this.question) {
        this.commentBtn = "收起评论";
      }
      this.showComment = !this.showComment;
    },
    toggleFold() {
      this.$emit("toggleFold");
    },
    watchQuestion() {
      this.$emit("watch");
      this.$http.get(`/api/questions/${this.pk}/watch/`).then(res => {
        if (res.body.success == true) {
          this.newIsWatch = true;
        } else {
          this.$Message.error(res.body.msg);
        }
      },
      function(response) {
        this.$Message.error(response.status + " " + response.statusText);
      });
    },
    cancelWatchQuestion() {
      this.$emit("cancelWatch");
      this.$http.get(`/api/questions/${this.pk}/cancel_watch/`).then(res => {
        if (res.body.success == true) {
          this.newIsWatch = false;
        } else {
          this.$Message.error(res.body.msg);
        }
      },
      function(response) {
        this.$Message.error(response.status + " " + response.statusText);
      });
    },
    getComments() {
      this.$http.get(`/api/answers/${this.pk}/get_comments/`).then(res => {
        if (res.body.success == true) {
          this.comments = res.body.data.results;
        } else {
          this.$Message.error(res.body.msg);
        }
      },
      function(response) {
        this.$Message.error(response.status + " " + response.statusText);
      });
    },
    postApprove() {
      if (this.newHasAgainst) this.postCancelAgainst();
      this.$http.get(`/api/answers/${this.pk}/agree/`).then(res => {
        if (res.body.success == true) {
          this.newApprove++;
          this.newHasApprove = true;
        } else {
          this.$Message.error(res.body.msg);
        }
      },
      function(response) {
        this.$Message.error(response.status + " " + response.statusText);
      });
    },
    postCancelApprove() {
      this.$http.get(`/api/answers/${this.pk}/cancel_agree/`).then(res => {
        if (res.body.success == true) {
          this.newApprove--;
          this.newHasApprove = false;
        } else {
          this.$Message.error(res.body.msg);
        }
      },
      function(response) {
        this.$Message.error(response.status + " " + response.statusText);
      });
    },
    postAgainst() {
      if (this.newHasApprove) this.postCancelApprove();
      this.$http.get(`/api/answers/${this.pk}/disagree/`).then(res => {
        if (res.body.success == true) {
          this.newHasAgainst = true;
        } else {
          this.$Message.error(res.body.msg);
        }
      },
      function(response) {
        this.$Message.error(response.status + " " + response.statusText);
      });
    },
    postCancelAgainst() {
      this.$http.get(`/api/answers/${this.pk}/cancel_disagree/`).then(res => {
        if (res.body.success == true) {
          this.newHasAgainst = false;
        } else {
          this.$Message.error(res.body.msg);
        }
      },
      function(response) {
        this.$Message.error(response.status + " " + response.statusText);
      });
    },
    addFavorite() {
      this.$http.get(`/api/answers/${this.pk}/favorite/`).then(res => {
        if (res.body.success == true) {
          this.$Message.success("收藏成功");
        } else {
          this.$Message.error(res.body.msg);
        }
      },
      function(response) {
        this.$Message.error(response.status + " " + response.statusText);
      });
    },
    share(name){
      if(name=='copy'){
        const clipboard = new Clipboard('.copyBtn');
        clipboard.on('success', e => {
          this.$Message.success("复制成功,分享给你的好友吧")
        });
      }else if(name=='weibo'){
        window.location = "http://service.weibo.com/share/share.php?appkey=&title="+
        document.title
        +"&url="+this.$router.path
        +"&searchPic=false&style=simple";
      }else if(name=='weixin'){
        this.$Message.info("点击复制链接,分享给你的微信好友吧")
      }
    } 
  },
  created() {
    this.newHasAgainst = this.hasAgainst;
    this.newHasApprove = this.hasApprove;
    this.newApprove = this.approve;
    this.newIsWatch = this.isWatch;
    if (!this.forQuestion) this.getComments();
    if (this.commentCount > 0) {
      this.commentBtn = this.commentCount + " 条评论";
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
.btn-group {
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
.voteBtn.is-disappear {
  display: none;
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

.writeIcon {
  fill: #2d84cc;
  vertical-align: text-bottom;
  height: 16px;
  width: 14px;
}
.writeBtn {
  color: #2d84cc;
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
.ivu-modal-footer {
  display: none;
}
.right {
  float: right;
}
.weiboIcon {
  fill: rgb(249, 110, 118);
  height: 16px;
  width: 16px;
  vertical-align: text-bottom;
}
.copyLinkIcon {
  fill: #9fadc7;
  height: 16px;
  width: 16px;
  vertical-align: text-bottom;
}
.weixinIcon {
  fill: rgb(125, 210, 57);
  height: 16px;
  width: 16px;
  vertical-align: text-bottom;
}
.ivu-dropdown-item {
  line-height: 30px;
  font-size: 14px!important;
  color: #262626;
}
.ivu-dropdown-item:hover {
 color: #7a8599;
 background: #f4f8fb;
}
</style>

