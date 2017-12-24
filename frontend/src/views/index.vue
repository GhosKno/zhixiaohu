<template>
  <div>
    <TopBar></TopBar>
    <div class="layout">
        <div class="container">
            <SubMenuBar></SubMenuBar>
            <div class="feed-flow">
                <AnswerListCard></AnswerListCard>
                <AnswerListCard></AnswerListCard>
                <AnswerListCard></AnswerListCard>
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
        min-width: 960px;
        width: 100vw;
        height: 100vh;
        background: #f5f7f9;
    }
    .container{
        float: left;
        width: 600px;
        margin-left: 160px;
        margin-top: 10px;
    }
    
    .card{
        margin-bottom: 10px;
        background: #fff;
        overflow: hidden;
        border-radius: 2px;
        -webkit-box-shadow: 0 1px 3px rgba(0,0,0,.1);
        box-shadow: 0 1px 3px rgba(0,0,0,.1);
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
    }
    .sidebar{
        float: right;
        margin-right: 170px;
        margin-top: 10px;
        width: 320px;
    }
    .feed-flow .card{
        padding: 10px;
    }
    
</style>
