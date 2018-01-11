<template>
  <div>
    <div id="quillEditor" :style="{'height': `${height}px`}">
    </div>
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
    // props: ['placeholder','height'],
    components: {quillEditor},
    props: {
      imgUpload: {
        type: Boolean,
        default: true
      },
      placeholder: {
        type: String,
        default: '让我们来谈笑风生'
      },
      height: {
        default: 150
      }
    },
    data(){
      return {
        quillEditorRoot: {},
        /**** */
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
              ['clean']
            ],
            imageImport: true
          },
          strict: false,
          theme: 'snow'
        },
        addRange: {},
      }
    },
    methods: {
      editorChange({editor, html, text}) {
        this.htmlContent = html
      },
      getHtmlContent() {
        return this.quillEditorRoot.container.firstChild.innerHTML
      },
      isEmpty() {
        var text = this.quillEditorRoot.getText()
        var s1 = text.replace(/[\r\n]/g, '').replace(/[ ]/g, '');
        return (s1 == '') ? true : false;
      },
      beforeUpload(file) {
        return this.upload(file)
      },
      upload(file) {
        const suffix = file.name.split('.')
        const ext = suffix.splice(suffix.length-1,1)[0]
          return this.$http.get('/api/images').then(res => {
            this.uploadData = {
              key: res.body.data.name,
              token: res.body.data.token
            }
        })
      },
      upScuccess(e, file, fileList) {
        let url = ''
        url = STATICDOMAIN + e.key
        if (url != null && url.length > 0) {
          let value = url + '-zhixiaohu'
          for(var i = 0;i<=100;i++) {
            this.addRange = this.quillEditorRoot.getSelection()
            if(this.addRange) {
              break
            }
          }
          value = value.indexOf('http') !== -1 ? value : 'http:' + value
          if(!this.quillEditorRoot.getSelection()){
            this.$Message.error(`图片插入失败`)
            return
          }
          this.quillEditorRoot.focus()
          var range = this.quillEditorRoot.getSelection()
          let index = 0
          if (range) {
            index = range.index
          }
          this.quillEditorRoot.insertEmbed(index, 'image', value, Quill.sources.API)
          this.quillEditorRoot.formatText(index, index + 1, 'width', 400 + 'px');
        } else {
          this.$Message.error(`图片插入失败`)
        }
        this.$refs['upload'].clearFiles()
      }
    },
    created() {
      if(this.imgUpload) {
        this.editorOption.modules.toolbar.push(['image'])
      }
    },
    mounted() {
      this.quillEditorRoot = new Quill('#quillEditor', this.editorOption)
      this.quillEditorRoot.getModule("toolbar").addHandler("image", async (image) => {
        this.addRange = this.quillEditorRoot.getSelection()
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
#quillEditor {
  height: 200px;
}
</style>
