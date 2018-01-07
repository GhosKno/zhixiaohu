<template>
<div>
    <div class="topbar">
        <div class="title">
            {{numOfComment}} 条评论
        </div>
        <Select v-model="model1" style="float: right;width:100px" placeholder="默认排序">
          <Option v-for="item in answerSort" :value="item.value" :key="item.value">{{ item.label }}</Option>
        </Select>
    </div>
    <div class="list">
        <div class="item" 
            v-for="cm of comments" 
            v-bind:key="cm.id">
            <div class="meta">
                <Poptip trigger="hover" placement="right" width="400">
                    <Avatar class="avatar" shape="square" size="small"  />
                    <div class="api" slot="content">
                        
                    </div>
                </Poptip>
                <span class="name">{{cm.author}}</span>
                <span class="time">{{cm.time}}</span>
            </div>
            <div class="content">
                {{cm.text}}
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
    <input class="commentInput" :class="{'is-active': showCommentBtn}" v-model="commentVal" type="text" placeholder="写下你的评论..." required @focus="showCommentBtn = true" @blur="showCommentBtn = false">
    <Button type="primary" class="commentBtn" :class="{ 'is-visible': showCommentBtn }" :disabled="commentVal==''">评论</Button>
    </div>
</div>
</template>
<script>
export default {
  name: "commentList",
  props: {
    numOfComment: {}
  },
  data() {
    return {
      comments: [
        { id: 0, author: "失豆", time: "2 天前", text: "心疼 好可怕", zan: 12 },
        { id: 1, author: "橘子超人", time: "1 天前", text: "呵呵", zan: 0 },
        { id: 2, author: "想乖乖写代码的喵", time: "1 天前", text: "超吓人的啊", zan: 2 }
      ],
      showCommentBtn: false,
      commentVal: '',
      answerSort: [
          {
              value: 'default',
              label: '默认排序'
          },
          {
              value: 'time',
              label: '按时间排序'
          }
      ],
    };
  },
  methods: {
    getComments() {
      const submit = () => {
        this.$http.post("/api/users/register/", this.regForm).then(res => {
          if (res.body.success) {
            this.$Message.success("注册成功");
            Vue.http.headers.common["X-CSRF-TOKEN"] = this.$cookie.get(
              "csrftoken"
            );
            this.setCookie(true, res.body.data.id, res.body.data.nickname);
            this.$store.commit("LOGIN");
            this.$store.commit("USER", {
              id: res.body.data.id,
              name: res.body.data.nickname
            });
            this.$router.push({ name: "home" });
          } else {
            this.$Message.error(res.data.msg);
          }
        });
      };
      this.$refs["regForm"].validate(valid => {
        if (valid) submit();
      });
    }
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

.commentInput {
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
  transition: width 0.2s;
  -moz-transition: width 0.2s; /* Firefox 4 */
  -webkit-transition: width 0.2s; /* Safari 和 Chrome */
  -o-transition: width 0.2s; /* Opera */
}

.commentInput.is-active{
  width: 90%;
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
  margin-left:7px;
  position: absolute;
  transform: scale(0);
  -webkit-transform: scale(0);
  transition: transform .2s ease,
    -webkit-transform .2s ease;
}
.commentBtn.is-visible {
  transform: scale(1);
  -webkit-transform: scale(1);
}
.footer{
    padding: 12px 16px;
    background: #fff;
    border-top: 1px solid #ebeef5;
}
</style>
