<template>
  <div>
    <TopBar></TopBar>
    <div class="layout">
        <div class="container">
            <SubMenuBar></SubMenuBar>
            <div class="feed-flow">
                <AnswerListCard avatar="h" name="ccc" qlink="" feed-title="热门内容,来自: 历史" question="历史上外交时有哪些尴尬场面？" answer="南海仲裁案之后，2016年7月16日，在美国国务院记者会上，凤凰卫视记者王冰汝向美国国务院发言人马克·托纳提问：“新加坡国立大学国际法中心在网站上刊登了地图和地名词典，其中一份地图，它的来源是美国政府，而且这张地图上写的是太平岛，而不是太平礁，这跟南海仲裁案“仲裁”结果不..."></AnswerListCard>
                <AnswerListCard qlink="" question="Mac 上的每个菜单命令，都能自定义快捷键吗?" cover-img="https://ss0.baidu.com/73F1bjeh1BF3odCf/it/u=3420588888,2752900295&fm=85&s=03809E4D4422EB430E34E03103008043" answer = "通常情况下，一个应用在 Mac 菜单栏显示的菜单命令，可以囊括了这个应用的大部分功能。同时也会为常用的菜单设置快捷键，比如最常见的「新建」功能，默认都是 Command + N。 为什么要自定义快捷键,许多开发者有自己的习惯,或..."></AnswerListCard>
                <AnswerListCard feed-title="你可能感兴趣: 生活"></AnswerListCard>
            </div>
        </div>
        <div class="sidebar">
            <SideBar></SideBar>
        </div>
    </div>
  </div>
</template>

<script>
  const TopBar = resolve => require(['@/components/topBar'], resolve)
  const SubMenuBar = resolve => require(['@/components/subMenuBar'], resolve)
  const AnswerListCard = resolve => require(['@/components/answerListCard'], resolve)
  const SideBar = resolve => require(['@/components/sideBar'], resolve)

  export default {
    name: 'IdxPage',
    components: {TopBar,SubMenuBar,AnswerListCard,SideBar}
  }
</script>

<style scoped>
    .layout{
        padding-top: 60px;
    }
    .container{
        float: left;
        min-width: 200px;
        width: 50%;
        margin-left: 14%;
        margin-top: 10px;
    }
    .sidebar{
        float: right;
        margin-right: 14%;
        margin-top: 10px;
        width: 20%;
    }
</style>
