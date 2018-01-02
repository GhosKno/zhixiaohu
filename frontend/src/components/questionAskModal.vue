<template>
  <div class="question-modal-content">
    <Modal
      v-model="showQuestionForm"
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
          placeholder="问题标题">
        </Input>
        <Select
          class="question-input"
          v-model="questionForm.topic"
          filterable
          remote
          :remote-method="filterRemoteTopic"
          :loading="topicLoading"
          placeholder="添加话题"
        >
          <Option
            v-for="(option, index) in topicOption"
            :key="index"
            :value="option.value"
          >
          {{option.label}}
          </Option>
        </Select>
        <span class="editor-label">问题描述（可选）：</span>
        <quill-editor
          :options="editorOption"
          ref="quillEditor"
          @blur="onEditorBlur($event)" 
          @focus="onEditorFocus($event)"
          @change="onEditorChange($event)"
          @ready="onEditorReady($event)"
        ></quill-editor>
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
import {quillEditor} from 'vue-quill-editor'
import Quill from 'quill'
export default {
  name: 'questionAskModal',
  props: {
  },
  data () {
    return {
      questionForm: {
        title: '',
        topic: '',
        content: ''
      },
      showQuestionForm: false,
      editorOption: {
        modules: {
          toolbar: [
            ['bold','italic','underline', 'strike'],
            [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
            [{ 'color': [] }, { 'background': [] }],
            [{ 'size': ['small', false, 'large', 'huge'] }],
            ['clean']
          ]
        },
        placeholder: '问题背景、条件等详细信息',
        theme: 'snow'
      },
      topicLoading: false,
      topicOption: [],
    }
  },
  computed: {
    editor() {
      return this.$refs.quillEditor.quill
    }
  },
  methods: {
    open () {
      this.showQuestionForm = true
    },
    onEditorChange({editor, html, text}) {
      this.questionForm.content=html;
      // console.log(html)
    },
    onEditorFocus() {
      return
    },
    onEditorReady() {
      return
    },
    onEditorBlur() {
      return
    },
    submitQuestion () {
      //TODO submit question
      console.log(this.questionForm.content)
    },
    filterRemoteTopic (query) {
      if (query !== '') {
        this.topicLoading = true;
        //TODO get remote topic Option
    } else {
      this.topicOption = [];
    }
  },
  },
  components: {
    quillEditor
  }
}
</script>

<style lang="less">
@import 'quill/dist/quill.core.css';
@import 'quill/dist/quill.snow.css';
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
</style>

