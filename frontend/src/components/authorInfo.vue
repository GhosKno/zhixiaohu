<template>
<div class="info">
    <Poptip trigger="hover" placement="right" width="400">
        <Avatar class="avatar" shape="square" size="small"  :src="authorAvatar"  />
        <div class="api" slot="content">
            
        </div>
    </Poptip>
    <div class="name">
        {{authorName}}
    </div>
    <div class="badge-text">
        , {{authorBadge}}
    </div>
</div>
</template>
<script>
export default {
  name: 'authorInfo',
  props:{
      authorAvatar: {
          default: ('/static/avatar.jpg'),
      },
      authorName: {
          default: "Coldwings"
      },
      authorBadge: {
          default: "已婚人士/专业数星星团队成员/编程狂热者/不只是Python/并行框架/DL爱好者"
      },
  }
}
</script>
<style scoped>
.name{
    margin-left: 5px;
    display: inline;
    font-weight: 700;
    font-size: 15px;
    line-height: 24px;
}
.badge-text{
    display: inline;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    font-size: 14px;
    line-height: 24px;
}
.avatar{
    vertical-align: top;
}
</style>
