<template>
<div class="card">
    <div class="feed-title">
        来自话题: 学习
    </div>
    <AuthorInfo></AuthorInfo>
    <div class="question">
        Mac 上的每个菜单命令，都能自定义快捷键吗?
    </div>
    <div class="content">
        通常情况下，一个应用在 Mac 菜单栏显示的菜单命令，可以囊括了这个应用的大部分功能。同时也会为常用的菜单设置快捷键，比如最常见的「新建」功能，默认都是 Command + N。 为什么要自定义快捷键...
        
        <Button type="text" class="read-all">阅读全文 <Icon type="chevron-down"></Icon></Button>
        <ToolBar></ToolBar>
    </div>
</div>
</template>
<script>
const AuthorInfo = resolve => require(['@/components/authorInfo'], resolve)
const ToolBar = resolve => require(['@/components/toolBar'], resolve)
export default {
  name: 'answerListCard',
  components: {AuthorInfo,ToolBar},
}
</script>

<style scoped>
.feed-title{
    color: #8590a6;
    line-height: 1;
    font-weight: 500;
    font-size: 14px;
    margin-top: 5px;
    margin-bottom: 14px;
}
.question{
    color: #000;
    margin: 5px;
    font-size: 18px;
    font-weight: 700;
}
.content{
    color: #4a4a4a;
    font-size: 14px;
    line-height: 1.625;
    margin: 5px;
}
.read-all{
    padding: 0;
    margin-left: 4px;
    color: #175199;
}
</style>
