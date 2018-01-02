<template>
<div class="comment-card">
    <div class="topbar">
        <div class="title">
            {{numOfComment}} 条评论
        </div>
    </div>
    <div class="list">
            <div class="item" 
            v-for="cm of comments" 
            v-bind:key="cm.id">
                <div class="meta">
                <Poptip trigger="hover" placement="right" width="400">
                    <Avatar class="avatar" shape="square" size="small"  />
                    <div class="api" slot="content">
                        
                    </div>
                </Poptip>
                <span class="name">{{cm.author}}</span>
                <span class="time">{{cm.time}}</span>
                </div>
                <div class="content">
                    {{cm.text}}
                </div>
                <div class="tool">
                    <Button type="text" class="zan">
                        <svg viewBox="0 0 20 18" aria-hidden="true" class="zanIcon"><g><path d="M.718 7.024c-.718 0-.718.63-.718.63l.996 9.693c0 .703.718.65.718.65h1.45c.916 0 .847-.65.847-.65V7.793c-.09-.88-.853-.79-.846-.79l-2.446.02zm11.727-.05S13.2 5.396 13.6 2.89C13.765.03 11.55-.6 10.565.53c-1.014 1.232 0 2.056-4.45 5.83C5.336 6.965 5 8.01 5 8.997v6.998c-.016 1.104.49 2 1.99 2h7.586c2.097 0 2.86-1.416 2.86-1.416s2.178-5.402 2.346-5.91c1.047-3.516-1.95-3.704-1.95-3.704l-5.387.007z"></path></g></svg>
                    {{cm.zan?cm.zan:"赞"}}
                    </Button>
                    
                </div>
            </div>
        </div>
</div>
</template>
<script>
export default {
  name: "commentList",
  props:{
      'numOfComment':{},
      
  },
  data() {
      return {
       comments: [
            {id:0, author: '失豆', time:'2 天前',text:'心疼 好可怕',zan:12},
            {id:1, author: '橘子超人', time:'1 天前', text:'呵呵',zan:0},
            {id:2, author: '想乖乖写代码的喵', time:'1 天前', text:'超吓人的啊',zan:2}
        ]
      }
    },
};
</script>

<style scoped>
.comment-card{
    border: 1px solid #e7eaf2;
    -webkit-box-shadow: 0 1px 3px 0 rgba(0,33,77,.05);
    box-shadow: 0 1px 3px 0 rgba(0,33,77,.05);
    background: #fff;
    margin-top: 12px;
    overflow: visible;
    border-radius: 4px;
}
.topbar{
    background: #fff;
    border-bottom: 1px solid #f0f2f7;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    justify-content: space-between;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    height: 50px;
    padding: 0 20px;
}
.topbar .title{
    display: inline-block;
    font-size: 15px;
    font-weight: 600;
    font-synthesis: style;
    color: #1e1e1e;
}
.item{
    position: relative;
    flex-shrink: 0;
    padding: 12px 16px 10px;
    font-size: 15px;
}
.item:after {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    display: block;
    margin: 0 20px;
    border-bottom: 1px solid #f0f2f7;
    content: "";
}
.zan{
    display: inline-block;
    font-size: 14px;
    line-height: 32px;
    color: #8590a6;
    padding: 0;
    border: none;
    border-radius: 0;
}
.zan:hover .zanIcon{
    color: #7a8599;
    fill: #7a8599;
}
.zanIcon{
    fill: #95a1ba;
    height: 16px; 
    width: 13px;
    vertical-align: text-bottom;
}
.time{
    float: right;
    font-size: 14px;
    color: #8590a6;
}
.name{
    padding-left: 5px;
    line-height: 24px;
}
.content{
    margin-bottom: 6px;
    line-height: 25px;
    word-break: break-word;
}
.meta{
    margin-bottom: 5px;
}
</style>
