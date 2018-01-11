<template>
  <div class="answer-card">
      <div class="info">
        <Avatar class="avatar" shape="square" size="large"  :src="author.avatar" />
        <div class="author-text">
            <div class="name">
                {{author.nickname}}
            </div>
            <div class="badge-text">
                {{author.discription}}
            </div>
        </div>
      </div>
      <common-editor
          ref="quillEditor"
          placeholder="在这里写下你的回答"
          :height="200"
        ></common-editor>
    <Button type="primary" class="postBtn" @click="postAnswer">提交回答</Button>
  </div>
</template>
<script>
import commonEditor from "@/components/commonEditor";
import api from "@/utils/api";

export default {
  name: "AnswerEditor",
  components: {
    commonEditor
  },
  data() {
    return {
      author: {}
    };
  },
  methods: {
    getProfile() {
      api.getProfile(this.$store.state.userid).then(
        res => {
          if (res.body.success) {
            this.author = res.body.data;
          } else {
            this.$Message.error(res.body.msg);
          }
        },
        err => {
          this.$Message.error(err.status + " " + err.statusText);
        }
      );
    },
    postAnswer: function() {
      if (this.$refs["quillEditor"].isEmpty()) {
        this.$Message.error("请填写回答");
      } else {
        this.$emit("post", this.$refs["quillEditor"].getHtmlContent());
      }
    }
  },
  created() {
    this.getProfile();
  }
};
</script>
<style scoped>
.answer-card {
  padding: 5px 15px;
}
.info {
  margin: 10px 0;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
}
.author-text {
  margin-left: 5px;
}
.name {
  font-weight: 700;
  font-size: 15px;
  line-height: 24px;
}
.badge-text {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  font-size: 14px;
  line-height: 24px;
}
.postBtn {
  float: right;
  margin: 5px;
}
</style>
