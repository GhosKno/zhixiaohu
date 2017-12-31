<template>
<div class="author-info">
    <Poptip trigger="hover" placement="right" width="400">
        <Avatar shape="square"  :src="authorAvatar"  />
        <div class="api" slot="content">
            
        </div>
    </Poptip>
    <div class="author-name">
        {{authorName}}
    </div>
    <div class="author-badge-text">
        , {{authorBadge}}
    </div>
</div>
</template>
<script>
export default {
  name: 'authorInfo',
  props:{
      authorAvatar: {
          default: '~assets/avatar.jpg',
      },
      authorName: {
          default: "MakicLin"
      },
      authorBadge: {
          default: ""
      }
  }
}
</script>
<style scoped>
.author-name{
    margin-left: 5px;
    display: inline;
    font-weight: 700;
    font-size: 15px;
}
.author-badge-text{
    display: inline;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    font-size: 14px;
}
</style>
