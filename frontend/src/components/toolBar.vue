<template>
  <div class="toolBar">
    <div class="btn-group" v-if="forQuestion">
        <Button v-if="newIsWatch" @click="cancelWatchQuestion()">取消关注</Button>
        <Button type="primary" @click="watchQuestion()" v-else>关注问题</Button>
        <Button type="ghost" class="writeBtn" @click="$emit('writeAnswer')">
          <svg class="writeIcon">
              <use xlink:href="#pen"></use>
          </svg>
          写回答
        </Button>
    </div>
    <!--点赞-->
    <div class="btn-group" v-else>
        <Button class="voteBtn" :class="{'is-active': newHasZan}" :disabled="isOwner" @click="newHasZan?cancelZan():Zan()">
          <Icon type="arrow-up-b" class="voteIcon" size=16></Icon>
          <span class="voteNum">{{newZanNum}}</span>
        </Button>
        <Button class="voteBtn" :class="{'is-active': newHasCai,'is-disappear': isOwner} " @click="newHasCai?CancelCai():Cai()">
        <Icon type="arrow-down-b" class="voteIcon" size=16></Icon></Button>
    </div>
    <Button type="text" class="actionBtn" v-if="!forQuestion" @click="toggleComment">
      <svg class="actionIcon">
          <use xlink:href="#comment"></use>
      </svg>
      {{commentBtn}}
    </Button>
    <Dropdown trigger="click" :transfer="true" @on-click="handleShare">
      <Button type="text" class="actionBtn">
        <svg class="actionIcon">
          <use xlink:href="#share"></use>
        </svg>
        分享
      </Button>
      <DropdownMenu slot="list">
          <DropdownItem name="copy" :id="'copyBtn'+_uid" :data-clipboard-text="copyText" >
            <svg class="copyLinkIcon">
              <use xlink:href="#link"></use>
            </svg>
              复制链接
          </DropdownItem>
          <DropdownItem name="weibo" >
            <svg class="weiboIcon">
              <use xlink:href="#weibo"></use>
            </svg>
              新浪微博
          </DropdownItem>
          <DropdownItem name="weixin" >
            <svg class="weixinIcon">
              <use xlink:href="#weixin"></use>
            </svg>
              微信好友
          </DropdownItem>
      </DropdownMenu>
    </Dropdown>
      <span v-if="!forQuestion">
        <Button type="text" class="actionBtn" @click="newHasStar?CancelStar():Star()">
          <svg class="actionIcon starIcon" :class="{'is-active':newHasStar}">
            <use xlink:href="#star"></use>
          </svg> {{newHasStar?'取消收藏':'收藏'}}
        </Button>
        <Button type="text" class="actionBtn">
          <Dropdown trigger="click" :transfer="true" @on-click="handleMore">
              <svg class="actionIcon">
                <use xlink:href="#more"></use>
              </svg>
              <DropdownMenu slot="list" v-if="isOwner">
                <DropdownItem name="delete">删除</DropdownItem>
                <DropdownItem name="edit">修改</DropdownItem>
              </DropdownMenu>
              <DropdownMenu slot="list" v-else>
                  <DropdownItem name="report">举报</DropdownItem>
                  <DropdownItem name="noHelp">没有帮助</DropdownItem>
              </DropdownMenu>
          </Dropdown>
        </Button>
      </span>
      <Button type="text" class="actionBtn right" v-if="showFoldBtn" @click="toggleFold">
          <span v-if="fold">展开全文 <Icon type="chevron-down"></Icon></span>
          <span v-else>收起 <Icon type="chevron-up"></Icon></span>
      </Button>
<!-- 
<Modal v-model="showComment" v-if="forQuestion">
  <CommentList :commentCount="commentCount" :pk="pk" :comments="comments">
  </CommentList>
</Modal> -->
<div class="commentCard" v-show="showComment">
  <CommentList :commentCount="commentCount" :pk="pk" :comments="comments">
  </CommentList>
  <div slot="footer"></div>
</div>
  </div>
</template>
<script>
const CommentList = resolve => require(["@/components/commentList"], resolve);
import Clipboard from "clipboard";
import api from "@/utils/api";

export default {
  name: "toolBar",
  components: { CommentList },
  data() {
    return {
      showComment: false,
      commentBtn: "评论",
      comments: [],
      newHasZan: Boolean,
      newHasCai: Boolean,
      newHasStar: Boolean,
      newZanNum: Number,
      newIsWatch: Boolean,
      clipboard:{}
    };
  },
  props: {
    hasZan: Boolean,
    hasCai: Boolean,
    hasStar: Boolean,
    zanNum: Number,
    forQuestion: {
      type: Boolean,
      default: false
    },
    fold: {
      type: Boolean,
      default: true
    },
    showFoldBtn: {
      type: Boolean,
      default: true
    },
    commentCount: Number,
    pk: {},
    isWatch: {
      type: Boolean,
      default: false
    },
    isOwner: {},
    copyText: {
      default: document.title + " " + window.location.href
    }
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
      api.watchQuestion(this.pk).then(
        res => {
          if (res.body.success == true) {
            this.newIsWatch = true;
          } else {
            this.$Message.error(res.body.msg);
          }
        },
        err => {
          this.$Message.error(err.status + " " + err.statusText);
        }
      );
    },
    cancelWatchQuestion() {
      this.$emit("cancelWatch");
      api.cancelWatchQuestion(this.pk).then(
        res => {
          if (res.body.success == true) {
            this.newIsWatch = false;
          } else {
            this.$Message.error(res.body.msg);
          }
        },
        err => {
          this.$Message.error(err.status + " " + err.statusText);
        }
      );
    },
    getComments() {
      api.getComments(this.pk).then(
        res => {
          if (res.body.success == true) {
            this.comments = res.body.data.results;
          } else {
            this.$Message.error(res.body.msg);
          }
        },
        err => {
          this.$Message.error(err.status + " " + err.statusText);
        }
      );
    },
    Zan() {
      if (this.newHasCai) this.CancelCai();
      api.zanAnswer(this.pk).then(
        res => {
          if (res.body.success == true) {
            this.newZanNum++;
            this.newHasZan = true;
          } else {
            this.$Message.error(res.body.msg);
          }
        },
        err => {
          this.$Message.error(err.status + " " + err.statusText);
        }
      );
    },
    cancelZan() {
      api.cancelZanAnswer(this.pk).then(
        res => {
          if (res.body.success == true) {
            this.newZanNum--;
            this.newHasZan = false;
          } else {
            this.$Message.error(res.body.msg);
          }
        },
        err => {
          this.$Message.error(err.status + " " + err.statusText);
        }
      );
    },
    Cai() {
      if (this.newHasZan) this.cancelZan();
      api.caiAnswer(this.pk).then(
        res => {
          if (res.body.success == true) {
            this.newHasCai = true;
          } else {
            this.$Message.error(res.body.msg);
          }
        },
        err => {
          this.$Message.error(err.status + " " + err.statusText);
        }
      );
    },
    CancelCai() {
      api.CancelCaiAnswer(this.pk).then(
        res => {
          if (res.body.success == true) {
            this.newHasCai = false;
          } else {
            this.$Message.error(res.body.msg);
          }
        },
        err => {
          this.$Message.error(err.status + " " + err.statusText);
        }
      );
    },
    Star() {
      api.starAnswer(this.pk).then(
        res => {
          if (res.body.success == true) {
            this.newHasStar = true;
          } else {
            this.$Message.error(res.body.msg);
          }
        },
        err => {
          this.$Message.error(err.status + " " + err.statusText);
        }
      );
    },
    CancelStar() {
      api.CancelStarAnswer(this.pk).then(
        res => {
          if (res.body.success == true) {
            this.newHasStar = false;
          } else {
            this.$Message.error(res.body.msg);
          }
        },
        err => {
          this.$Message.error(err.status + " " + err.statusText);
        }
      );
    },
    handleShare(name) {
      if (name == "weibo") {
        window.location =
          "http://service.weibo.com/share/share.php?appkey=&title=" +
          document.title +
          "&url=" +
          this.$router.path +
          "&searchPic=false&style=simple";
      } else if (name == "weixin") {
        this.$Message.info("点击复制链接,分享给你的微信好友吧");
      }
    },
    handleMore(name) {
      console.log(name)
      if (name == "delete") {
        this.$Notice.info({
                    title: "删除成功",
                    desc: "该回答将在 24h 后删除，取消请联系管理员"
                });
      } else if (name == "edit") {
        this.$Message.info("点击复制链接,分享给你的微信好友吧");
      } else if (name == "report") {
        this.$Message.success("举报成功");
      } else {
        this.$Message.info("谢谢反馈")
      }
    },
  },
  created() {
    this.clipboard = new Clipboard(`#copyBtn${this._uid}`);
    this.clipboard.on("success", e => {
      this.$Message.success("复制成功,分享给你的好友吧");
    });
    this.newHasCai = this.hasCai;
    this.newHasZan = this.hasZan;
    this.newHasStar = this.hasStar;
    this.newZanNum = this.zanNum;
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
<style lang="less" scoped>
@vote-color: #2d84cc;
.toolBar {
  clear: both;
  .btn-group {
    display: inline;
    .voteBtn {
      line-height: 30px;
      padding: 0 12px;
      font-size: 14px;
      color: @vote-color;
      background: #ebf3fb;
      border-color: #ebf3fb;
      &:hover {
        background-color: #e4ebf3;
        border-color: #e4ebf3;
      }
      &.is-active {
        color: #eef3f7;
        background: @vote-color;
        border-color: @vote-color;
      }
      &.is-disappear {
        display: none;
      }
      .voteIcon {
        vertical-align: text-bottom;
      }
      .voteNum {
        margin-left: 8px;
      }
    }
  }
  .actionBtn {
    display: inline-block;
    font-size: 14px;
    color: #8590a6;
    text-align: center;
    cursor: pointer;
    &:hover {
      color: #7a8599;
    }
    .actionIcon {
      fill: #8590a6;
      width: 18px;
      height: 18px;
      margin-right: 4px;
      vertical-align: text-bottom;
    }
    &.right {
      float: right;
    }
  }

  .writeIcon {
    fill: @vote-color;
    vertical-align: text-bottom;
    height: 16px;
    width: 14px;
  }
  .writeBtn {
    color: @vote-color;
  }

  .commentCard {
    border: 1px solid #e7eaf2;
    -webkit-box-shadow: 0 1px 3px 0 rgba(0, 33, 77, 0.05);
    box-shadow: 0 1px 3px 0 rgba(0, 33, 77, 0.05);
    background: #fff;
    margin-top: 12px;
    border-radius: 4px;
  }
  .starIcon.is-active {
    fill: #ffe600;
  }
}
/* 隐藏 modal footer */
.ivu-modal-footer {
  display: none;
}
.copyLinkIcon {
  fill: #9fadc7;
  height: 16px;
  width: 16px;
  vertical-align: text-bottom;
}
.weiboIcon {
  fill: rgb(249, 110, 118);
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
</style>

