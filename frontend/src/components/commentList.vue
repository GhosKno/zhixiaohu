<template>
<div>
    <div class="header">
        <div class="title">
            {{numOfComment}} 条评论
        </div>
        <Select style="float: right;width:100px" placeholder="默认排序">
          <Option v-for="item in commentSort" :value="item.value" :key="item.value">{{ item.label }}</Option>
        </Select>
    </div>
    <div class="list">
      <div class="item" 
          v-for="(cm,index) of comments" 
          v-bind:key="cm.id">
          <div class="meta" v-if="cm.userSummary">
            <a class="user-info" @click="$router.push({path: '/profile/'+cm.userSummary.id})">
              <Avatar class="avatar" shape="square" size="small"
                :src="cm.userSummary.avatar"/>
              <span class="name">{{cm.userSummary.nickname}}</span>
            </a>
              <span class="time">{{timeago(cm.add_time)}}({{(curPage-1)*10+index+1}} 楼)</span>
          </div>
          <div class="content">
              {{cm.detail}}
          </div>
          <div class="tool">
              <Button type="text" class="zan" @click="$Message.success('已赞~')">
                <svg class="zanIcon">
                  <use xlink:href="#zan"></use>
                </svg>
                <!-- TODO: add zan for comments -->
                  {{cm.zan?cm.zan:"赞"}}
              </Button>
          </div>
      </div>
      <Page size="small" class="pagination" :total="numOfComment" @on-change="fetchComments"></Page>
    </div>
    <div class="footer">
      <div class="commentEditor" :class="{'is-active': showCommentBtn}" >
        <input type="text" class="commentInput" 
          v-model="commentForm.detail" 
          placeholder="写下你的评论..." required 
          @focus="showCommentBtn = true" 
          @blur="hideCommentBtn()"
          @keyup.enter="postComment()"/>
          
        <Button type="primary" class="commentBtn" 
          :class="{ 'is-visible': showCommentBtn }" 
          :disabled="commentForm.detail==''"
          @click="postComment()">评论</Button>
      </div>
    </div>
</div>
</template>
<script>
const UserPoptip = resolve => require(["@/components/userPoptip"], resolve);
import api from "@/utils/api";

export default {
  name: "commentList",
  components: { UserPoptip },
  props: {
    pk: {},
    numOfComment: 0
  },
  data() {
    return {
      comments: [],
      showCommentBtn: false,
      commentForm: {
        answer: this.pk,
        detail: ""
      },
      curPage: 1,
      commentSort: [
        {
          value: "default",
          label: "默认排序"
        },
        {
          value: "time",
          label: "按时间排序"
        }
      ]
    };
  },
  methods: {
    fetchComments(page = 0) {
      if(page)this.curPage=page
      api.getComments(this.pk, page).then(
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
    postComment() {
      api.postComment(this.commentForm).then(
        res => {
          if (res.body.success == true) {
            this.$Message.success("评论成功");
            this.comments.push(res.body.data);
            this.commentForm.detail = "";
          } else {
            this.$Message.error(res.body.msg);
          }
        },
        res => {
          this.$Message.error(response.status + " " + response.statusText);
        }
      );
    },
    hideCommentBtn() {
      if (this.commentForm.detail === "") {
        setTimeout(() => {
          this.showCommentBtn = false;
        }, 100);
      }
    }
  },
  mounted() {
    if (!this.forQuestion) this.fetchComments();
  }
};
</script>

<style lang="less" scoped>
.header {
  background: #fff;
  border-bottom: 1px solid #f0f2f7;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  height: 50px;
  padding: 0 20px;
  .title {
    display: inline-block;
    font-size: 15px;
    font-weight: 600;
    font-synthesis: style;
    color: #1e1e1e;
  }
}
.list {
  .item {
    position: relative;
    flex-shrink: 0;
    padding: 12px 16px 10px;
    font-size: 15px;
    &:after {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      display: block;
      margin: 0 20px;
      border-bottom: 1px solid #f0f2f7;
      content: "";
    }

    .content {
      margin-bottom: 6px;
      line-height: 25px;
      word-break: break-word;
    }
    .meta {
      margin-bottom: 5px;
      a.user-info {
        color: #1e1e1e;
      }
      .time {
        float: right;
        font-size: 14px;
        color: #8590a6;
      }
      .name {
        padding-left: 5px;
        line-height: 24px;
      }
    }
    .zan {
      display: inline-block;
      font-size: 14px;
      line-height: 32px;
      color: #8590a6;
      padding: 0;
      border: none;
      border-radius: 0;
      &:hover .zanIcon {
        color: #7a8599;
        fill: #7a8599;
      }
      .zanIcon {
        fill: #95a1ba;
        height: 16px;
        width: 13px;
        vertical-align: text-bottom;
      }
    }
  }
  .pagination {
    margin: 10px;
  }
}
.footer {
  padding: 12px 16px;
  background: #fff;
  border-top: 1px solid #ebeef5;

  .commentEditor {
    position: relative;
    -webkit-transition: padding-right 0.3s ease;
    transition: padding-right 0.3s ease;
    &.is-active {
      padding-right: 94px;
    }
    .commentInput {
      position: relative;
      display: -webkit-box;
      display: -ms-flexbox;
      display: flex;
      width: 100%;
      height: 34px;
      padding: 0 10px;
      font-size: 14px;
      border: 1px solid #e7eaf1;
      border-radius: 3px;
      -webkit-box-sizing: border-box;
      box-sizing: border-box;
      background: #f7f8fa;
      outline: none;
      transition: all 0.2s;
      -moz-transition: all 0.2s; /* Firefox 4 */
      -webkit-transition: all 0.2s; /* Safari 和 Chrome */
      -o-transition: all 0.2s; /* Opera */
      &.is-active {
        background: #fff;
        border: 1px solid #9fadc7;
      }
      &::placeholder {
        color: #9fadc7;
        font-weight: 500;
      }
    }
    .commentBtn {
      position: absolute;
      right: 16px;
      bottom: 2px;
      transform: scale(0);
      -webkit-transform: scale(0);
      transition: all 0.2s ease;
      -moz-transition: all 0.2s; /* Firefox 4 */
      -webkit-transition: all 0.2s; /* Safari 和 Chrome */
      -o-transition: all 0.2s; /* Opera */
      &.is-visible {
        transform: scale(1);
        -webkit-transform: scale(1);
      }
    }
  }
}
</style>
