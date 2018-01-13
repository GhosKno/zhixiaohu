<template>
<div>
    <div v-if="inEdit">
        <CommonEditor
            ref="quillEditor"
            :height="200"
            :html="text"
            class="editor"
            ></CommonEditor>
        <span class="time">上次编辑于 {{this.timeago(postTime)}}</span>
        <Button type="primary" class="edit-btn" @click="handleEditPost">确认修改</Button>
    </div>
    <div v-else>
        <div class="text" ref="foldText" :class="{'is-fold':newFold}">
            <span v-html="text"></span>
        </div>
        <div class="time">发布于{{this.timeago(postTime)}}</div>
        <ToolBar class="tool-bar"
            :fold="newFold"
            :forQuestion="forQuestion" 
            :showFoldBtn="foldByDefault"
            :commentCount="commentCount"
            @toggleFold="newFold=!newFold;"
            @writeAnswer="$emit('writeAnswer')"
            @closeWriteAnswer="$emit('closeWriteAnswer')"
            @cancelWatch="$emit('cancelWatch')"
            @watch="$emit('watch')"
            @editAnswer="handleEditAnswer()"
            :zanNum="approve"
            :hasZan="hasApprove"
            :hasCai="hasAgainst"
            :hasStar="hasFavorite"
            :pk="pk"
            :isWatch="isWatch"
            :isOwner="isOwner"
            :copyText="copyText"></ToolBar>
    </div>
</div>
</template>
<script>
const ToolBar = resolve => require(["@/components/toolBar"], resolve);
const CommonEditor = resolve => require(["@/components/commonEditor"], resolve);
import api from "@/utils/api";

export default {
  name: "textWithToolBar",
  components: { ToolBar, CommonEditor },
  props: {
    text: {},
    forQuestion: Boolean,
    commentCount: Number,
    postTime: {},
    approve: Number,
    pk: {},
    isWatch: Boolean,
    hasApprove: Boolean,
    hasAgainst: Boolean,
    hasFavorite: Boolean,
    isOwner: Boolean,
    copyText: String,
    fold: {
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      fullAnswer: "",
      foldByDefault: false,
      inEdit: false,
      newFold: true
    };
  },
  methods: {
    // 高度小于85时，折叠无效，所以不折叠
    initDefaultFold: function() {
      var t = this.$refs.foldText;
      this.foldByDefault = t && t.scrollHeight > 85;
    },
    handleEditAnswer() {
      this.$emit("closeWriteAnswer");
      this.inEdit = true;
    },
    handleEditPost() {
      api.updateAnswer(this.pk, {'detail': this.$refs["quillEditor"].getHtmlContent()})
      .then(
          res=>{
              if(res.body.success){
                  this.$router.go(0);
              }else{
                  this.$Message.info(res.body.msg);
              }
          },
          err=>{
              this.$Message.error(err.status+': '+err.statusText)
          }

      )
    }
  },
  mounted() {
    setTimeout(() => {
      this.initDefaultFold();
    }, 500);
  },
  created() {
    this.newFold = this.fold;
  },
  watch: {
    fold() {
      this.newFold = this.fold;
    }
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
.is-fold {
  max-height: 70px;
  overflow: hidden;
}
.tool-bar {
  background: #fff;
  padding: 5px 0;
}
.time {
  margin-top: 10px;
  font-size: 14px;
  color: #8590a6;
}
.editor {
  margin: 10px 0;
}
.edit-btn {
  float: right;
  margin-bottom: 20px;
}
</style>
