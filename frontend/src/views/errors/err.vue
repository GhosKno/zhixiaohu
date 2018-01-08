<template>
  <div class="error">
<h1 class="header">
    <a href="/">
    <Logo color="#2f2f2f" class="logo"></Logo>
    </a>
    - {{errCode}}
</h1>
<div class="content">
    <p>
    <strong>发送错误了:{{errText}}</strong>
    </p>
    <p>也许是服务器出故障了，请稍后访问ಥ_ಥ</p>
    <hr>
    <p>
    <a href="/">返回首页</a>
    <span>或者</span>
    <a href="javascript:history.go(-1)" id="js-history-back">返回上页</a>
    </p>
</div>
</div>
</template>
<script>
const Logo = resolve => require(['@/components/logo.vue'], resolve)

export default {
  components: {Logo},
  props: {
      errCode:{},
      errText:{}
  }
}
</script>

<style scoped>
.logo{
    display: inline-block;
}
.error{
    margin: 169px auto 0;
    width: 404px;
}
.error .header {
    overflow: hidden;
    line-height: 1.2;
    margin: 0 0 .33em .33em;
}
.error .content {
    padding: 2em 1.25em;
    border: 1px solid #babbbc;
    border-radius: 5px;
    background: #fff;
    text-align: center;
}
.error strong {
    font-size: 1.1em;
    color: #000;
}
.error hr {
    margin: 1.3em 0;
}
.error p {
    margin: 0 0 1.7em;
    color: #999;
}
</style>

