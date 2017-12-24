<template>
  <div class="topic-sidebar">
    <div class="header">热门话题</div>
    <div class="topic-card-content">
      <Card class="topic-card" v-for="(el,index) in topicList" :key="index">
          <a class="label" slot="title">
            {{el.label}}
          </a>
          <span class="watchers" slot="extra">
            {{el.watchers}}人关注
          </span>
        <div class="topic-introduc">
          {{el.introduction.slice(0,20)}}...
        </div>
      </Card>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'topicSidebar',
    data () {
      return {
        topicList: [
          {label: '神器', introduction: '2018 年应届硕士毕业生如何拿到知名互联网公司深度学习 offer？', watchers: 5},
          {label: '神器', introduction: '2018 年应届硕士毕业生如何拿到知名互联网公司深度学习 offer？', watchers: 5},
          {label: '神器', introduction: '2018 年应届硕士毕业生如何拿到知名互联网公司深度学习 offer？', watchers: 5},
          {label: '神器', introduction: '2018 年应届硕士毕业生如何拿到知名互联网公司深度学习 offer？', watchers: 5},
        ]
      }
    }
  }
</script>

<style lang="less" scoped>
.topic-sidebar {
  .header {
    font-size: 2em;
    font-weight: 500;
  }
  .topic-card-content {
    .topic-card {
      margin: 10px 0;
      .label {
        font-size:1.2em;
      }
      .watchers{
        font-size: 0.9em;
        color: #ccc;
      }
    }
  }
}
</style>

