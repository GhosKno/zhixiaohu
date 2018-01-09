<template>
<div>
    <div class="topbar">
        <div class="title">
            {{comments.length}} 条评论
        </div>
        <Select style="float: right;width:100px" placeholder="默认排序">
          <Option v-for="item in answerSort" :value="item.value" :key="item.value">{{ item.label }}</Option>
        </Select>
    </div>
    <div class="list">
        <div class="item" 
            v-for="cm of comments" 
            v-bind:key="cm.id">
            <div class="meta">
                <Poptip trigger="hover" placement="right" width="400">
                    <Avatar class="avatar" shape="square" size="small"  :src="cm.userSummary.avatar"/>
                    <div class="api" slot="content">
                        <user-poptip ref="userPoptip" :id="author.id"></user-poptip>
                    </div>
                </Poptip>
                <span class="name">{{cm.userSummary.nickname}}</span>
                <span class="time">{{timeago(cm.add_time)}}</span>
            </div>
            <div class="content">
                {{cm.detail}}
            </div>
            <div class="tool">
                <Button type="text" class="zan">
                    <svg viewBox="0 0 20 18" aria-hidden="true" class="zanIcon"><g><path d="M.718 7.024c-.718 0-.718.63-.718.63l.996 9.693c0 .703.718.65.718.65h1.45c.916 0 .847-.65.847-.65V7.793c-.09-.88-.853-.79-.846-.79l-2.446.02zm11.727-.05S13.2 5.396 13.6 2.89C13.765.03 11.55-.6 10.565.53c-1.014 1.232 0 2.056-4.45 5.83C5.336 6.965 5 8.01 5 8.997v6.998c-.016 1.104.49 2 1.99 2h7.586c2.097 0 2.86-1.416 2.86-1.416s2.178-5.402 2.346-5.91c1.047-3.516-1.95-3.704-1.95-3.704l-5.387.007z"></path></g></svg>
                {{cm.zan?cm.zan:"赞"}}
                </Button>
            </div>
        </div>
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
import timeago from "@/utils/time";
export default {
  name: "commentList",
  props: {
    comments: {
      type: Array
    },
    pk: {}
  },
  data() {
    return {
      showCommentBtn: false,
      commentForm: {
        answer: this.pk,
        detail: ""
      },
      answerSort: [
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
    postComment() {
      this.$http.post(`/api/comments/`, this.commentForm)
      .then(res => {
        if (res.body.success == true) {
          console.log(res.body);
          this.$Message.success("评论成功");
          this.comments.push(res.body.data)
        } else {
          this.$Message.error(res.body.msg);
        }
      }, function(response) {
        this.$Message.error(response.status + " " + response.statusText);
      });
    },
    hideCommentBtn() {
      if (this.commentForm.detail===""){
        setTimeout(() => {
          this.showCommentBtn = false
        }, 100);
      }
    }
  },
  mounted() {
  }
};
</script>

<style scoped>
.topbar {
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
}
.topbar .title {
  display: inline-block;
  font-size: 15px;
  font-weight: 600;
  font-synthesis: style;
  color: #1e1e1e;
}
.item {
  position: relative;
  flex-shrink: 0;
  padding: 12px 16px 10px;
  font-size: 15px;
}
.item:after {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  display: block;
  margin: 0 20px;
  border-bottom: 1px solid #f0f2f7;
  content: "";
}
.zan {
  display: inline-block;
  font-size: 14px;
  line-height: 32px;
  color: #8590a6;
  padding: 0;
  border: none;
  border-radius: 0;
}
.zan:hover .zanIcon {
  color: #7a8599;
  fill: #7a8599;
}
.zanIcon {
  fill: #95a1ba;
  height: 16px;
  width: 13px;
  vertical-align: text-bottom;
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
.content {
  margin-bottom: 6px;
  line-height: 25px;
  word-break: break-word;
}
.meta {
  margin-bottom: 5px;
}
.commentEditor{
  position: relative;
    -webkit-transition: padding-right .3s ease;
    transition: padding-right .3s ease;
}
.commentEditor.is-active {
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
}

.commentInput.is-active {
  background: #fff;
  border: 1px solid #9fadc7;
}

.commentInput::-webkit-input-placeholder {
  color: #9fadc7;
  font-weight: 500;
}

.commentInput:-ms-input-placeholder {
  color: #9fadc7;
  font-weight: 500;
}
.commentInput::placeholder {
  color: #9fadc7;
  font-weight: 500;
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
}
.commentBtn.is-visible {
  transform: scale(1);
  -webkit-transform: scale(1);
}
.footer {
  padding: 12px 16px;
  background: #fff;
  border-top: 1px solid #ebeef5;
}
</style>
