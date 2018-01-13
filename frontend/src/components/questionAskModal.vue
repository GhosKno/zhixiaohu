<template>
  <div class="question-modal-content">
    <Modal
      v-model="showQuestionForm"
      class-name="vertical-center-modal"
    >
      <div slot="header" style="color:#0f88eb;text-align:center">
        <p style="height: 30px;line-height: 30px;font-size: 23px;">写下你的问题</p>
        <p style="font-weight:normal;">描述精确的问题更易得到解答</p>
      </div>
      <div class="question-body">
        <Input
          class="question-input"
          v-model="questionForm.title" 
          type="textarea" 
          :autosize="{minRows: 3,maxRows: 6}" 
          placeholder="问题标题"
        />
        <Select
          class="question-input"
          v-model="selectTopics"
          filterable
          remote
          multiple
          :remote-method="filterRemoteTopic"
          :loading="topicLoading"
          placeholder="添加话题"
        >
          <Option
            v-for="(option, index) in topicOption"
            :key="index"
            :value="option.id"
          >
          {{option.label}}
          </Option>
        </Select>
        <span class="editor-label">问题描述（可选）：</span>
        <CommonEditor
          ref="quillEditor"
          placeholder="问题背景、条件等详细信息"
          :height="150"
          :imgUpload="false"
        ></CommonEditor>
      </div>
      <div slot="footer" style="text-align:center;">
        <Button 
          type="primary" 
          size="large" 
          style="width:200px;"
          @click="submitQuestion()"
        >提交问题</Button>
      </div>
    </Modal>
  </div>
</template>

<script>
import CommonEditor from "@/components/commonEditor";
import api from "@/utils/api";

export default {
  name: "questionAskModal",
  props: {},
  data() {
    return {
      selectTopics: [],
      questionForm: {
        title: "",
        topics: [],
        detail: ""
      },
      showQuestionForm: false,
      topicLoading: false,
      topicOption: []
    };
  },
  computed: {
    editor() {
      return this.$refs.quillEditor.quill;
    }
  },
  methods: {
    open() {
      this.showQuestionForm = true;
    },
    submitQuestion() {
      this.questionForm.detail = this.$refs["quillEditor"].getHtmlContent();
      this.questionForm.topics = this.selectTopics;
      // if (this.$refs.quillEditor.isEmpty()){
      //   this.$Message.error("给问题加上描述吧~");
      //   return
      // }
      api.postQuestion(this.questionForm).then(
        res => {
          if (res.body.success) {
            this.$Message.success("添加问题成功");
            this.$router.push({path: '/question/'+res.body.data.id});
            this.showQuestionForm = false;
          } else {
            this.$Message.info(res.body.msg);
          }
        },
        err => {
          this.$Message.error(err.status+': '+err.statusText);
        }
      );
    },
    filterRemoteTopic(query) {
      if (query !== "") {
        this.topicLoading = true;
        api.searchTopics(query).then(res => {
          this.topicOption = res.body.data.results;
          this.topicLoading = false;
        });
      } else {
        this.topicOption = [];
      }
    }
  },
  components: {
    CommonEditor
  }
};
</script>

<style lang="less">
@import "quill/dist/quill.core.css";
@import "quill/dist/quill.snow.css";
.question-body {
  .question-input {
    margin-bottom: 20px;
  }
  .editor-label {
    color: #ccc;
    margin-bottom: 10px;
    display: inline-block;
  }
  .quill-editor {
    height: 150px;
    .ql-container {
      height: 100px;
    }
  }
}
.vertical-center-modal {
  display: flex;
  align-items: center;
  justify-content: center;

  .ivu-modal {
    top: 0;
  }
}
</style>

