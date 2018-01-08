<template>
  <div>
    <quill-editor
      ref="quillEditor"
      :options="editorOption"
      style="height: 180px; margin-bottom: 10px"
      v-model="editorContent"
      @change="editorChange"
    >
    </quill-editor>
    <Upload 
      action="//up-z1.qiniu.com"
      :before-upload="beforeUpload"
      :data="uploadData"
      :on-success="upScuccess"
      ref="upload"
      style="display: none;">
        <Button 
          type="ghost" 
          icon="ios-cloud-upload-outline"
          id="uploadInput"
        >Upload files</Button>
    </Upload>
  </div>
</template>
<script>
  const STATICDOMAIN = 'http://p26te03wf.bkt.clouddn.com/'
  import { quillEditor } from 'vue-quill-editor'
  import Quill from 'quill'
  import { ImageImport } from './modules/ImageImport.js'
  Quill.register('modules/imageImport', ImageImport)

  export default {
    name: 'commonEditor',
    props: ['placeholder'],
    components: {quillEditor},
    data(){
      return {
        editorContent: '', //文章内容
        htmlContent: '',  //html内容
        uploadData:{},
        editorOption: {
          placeholder: this.placeholder,
          modules: {
            toolbar: [
              ['bold','italic','underline', 'strike'],
              [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
              [{ 'color': [] }, { 'background': [] }],
              [{ 'size': ['small', false, 'large', 'huge'] }],
              ['image'],
              ['clean']
            ],
            imageImport: true
          },
          strict: false,
        },
        addRange: {},
      }
    },
    methods: {
      editorChange({editor, html, text}) {
        this.htmlContent = html
      },
      getHtmlContent() {
        return this.htmlContent
      },
      beforeUpload(file) {
        return this.upload(file)
      },
      upload(file) {
        const suffix = file.name.split('.')
        const ext = suffix.splice(suffix.length-1,1)[0]
          return this.$http.get('/api/images').then(res => {
            this.uploadData = {
              // key: `image/${suffix.join('.')}_${new Date().getTime()}.${ext}`,
              // token: res.data
              key: res.body.data.name,
              token: res.body.data.token
            }
        })
      },
      upScuccess(e, file, fileList) {
        let url = ''
        url = STATICDOMAIN + e.key
        // url = 'http://ock1p2k5t.bkt.clouddn.com/canvas-star%E4%B8%8B%E8%BD%BD%20%281%29.png'
        if (url != null && url.length > 0) { // 将文件上传后的URL地址插入到编辑器文本中
          let value = url
          for(var i = 0;i<=100;i++) {
            this.addRange = this.$refs.quillEditor.quill.getSelection()
            if(this.addRange) {
              break
            }
          }
          value = value.indexOf('http') !== -1 ? value : 'http:' + value
          this.$refs.quillEditor.quill.insertEmbed(this.addRange && this.addRange.hasOwnProperty('index') ? this.addRange.index : 0, 'image', value, Quill.sources.USER)
        } else {
          this.$message.error(`图片插入失败`)
        }
        this.$refs['upload'].clearFiles()
      }
    },
    created: function () {
    },
    mounted() {
      this.$refs.quillEditor.quill.getModule("toolbar").addHandler("image", async (image) => {
        this.addRange = this.$refs.quillEditor.quill.getSelection()
        if (image) {
          let fileInput = document.getElementById('uploadInput')
          fileInput.click()
        }
      })
    }
  }
</script>
<style scoped>
@import 'quill/dist/quill.core.css';                                                                                                                 
@import 'quill/dist/quill.snow.css';
</style>
