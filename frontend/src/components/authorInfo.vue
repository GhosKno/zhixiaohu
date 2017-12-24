<template>
<div class="author-info">
    <Poptip trigger="hover" placement="right" width="400">
        <Avatar shape="square"  src="https://cdn.sspai.com/attachment/origin/2016/03/11/315901.jpg?imageMogr2/quality/95/thumbnail/!60x60r/gravity/Center/crop/60x60"  />
        <div class="api" slot="content">
            <Avatar shape="square"  src="https://cdn.sspai.com/attachment/origin/2016/03/11/315901.jpg?imageMogr2/quality/95/thumbnail/!60x60r/gravity/Center/crop/60x60"  />
        </div>
    </Poptip>
    <div class="author-name">
        MakicLin
    </div>
    <div class="author-badge-text">
        ,平面设计，锥纸手机
    </div>
</div>
</template>
<script>
export default {
  name: 'authorInfo',
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
