<template>
  <div>
    <quill-editor
      ref="newEditor"
      :options="newOption"
      style="height: 200px; margin-bottom: 10px"
      v-model="editorContent"
      @change="editorChange">
    </quill-editor>
    <form 
      action="" 
      method="post" 
      enctype="multipart/form-data" 
      id="uploadFormMulti"
    >
      <input 
        style="display: none" 
        :id="uniqueId" 
        type="file" 
        name="avator" 
        multiple 
        accept="image/jpg,image/jpeg,image/png,image/gif" 
        @change="uploadImg('uploadFormMulti')">
    </form>
  </div>
</template>
<script>
  import { quillEditor } from 'vue-quill-editor'
  import Quill from 'quill'
  import { ImageImport } from './modules/ImageImport.js'
  Quill.register('modules/imageImport', ImageImport)

  export default {
    name: 'commonEditor',
    props: ['text', 'editorId','uploadImgUrl','placeholder'],
    components: {quillEditor},
    data(){
      return {
        editorContent: '',
        htmlContent: '',
        uniqueId: '',
        imgPercent: 0,
        imageLoading: false,
        newOption: {
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
        addImgRange: 0,
      }
    },
    methods: {
      editorChange({editor, html, text}) {
        this.htmlContent = html
      },
      getHtmlContent() {
        return this.htmlContent
      },
      async uploadImg(id) {
        this.imageLoading = true
        let formData = new FormData(document.getElementById(id)[0])
        try {
          const url = await this.uploadImgReq(formData)
          if (url != null && url.length > 0) {
            let value = url
            let index = this.addImgRange.hasOwnProperty('index') ? this.addImgRange.index : 0 // 获取插入时的位置索引，如果获取失败，则插入到最前面
            this.$refs.newEditor.quill.insertEmbed(index , 'image', value, Quill.sources.USER)
            let img = new Image()
            img.src = value
            img.onload = () => {
              this.$refs.newEditor.quill.formatText(index, index + 1, 'width', 400 + 'px');
            }
          } else {
          }
          document.getElementById(this.uniqueId).value=''
        } catch ({message: msg}) {
          document.getElementById(this.uniqueId).value=''
        }
        this.imageLoading = false
      },
      async uploadImgReq (formData) {
        // todo upload image
        return new Promise((resolve, reject) => {
          if (true) {
            resolve("http://ock1p2k5t.bkt.clouddn.com/canvas-star%E4%B8%8B%E8%BD%BD%20%281%29.png")
          } else {
            reject({message: '图片上传失败'})
          }
        })
      },
    },
    created: function () {
      this.imgPercent = 0
      this.editorContent = this.text
      this.uniqueId = this.editorId?this.editorId:'inputImg'
    },
    watch:{
      text: function () {
        this.editorContent = this.text
      }
    },
    mounted() {
      this.$refs.newEditor.quill.getModule("toolbar").addHandler("image", async (image) => {
        this.addImgRange = this.$refs.newEditor.quill.getSelection()
        if (image) {
          let fileInput = document.getElementById(this.uniqueId)
          fileInput.click()
        }
      })
    }
  }
</script>
<style scoped>

</style>
