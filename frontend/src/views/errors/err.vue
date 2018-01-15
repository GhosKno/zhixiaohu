<template>
  <div class="error">
<h1 class="header">
    <a href="/">
    <svg class="logo">
        <use xlink:href="#logo"></use>
    </svg>
    <svg-icon></svg-icon>
    </a>
    - {{err.code}}
</h1>
<div class="content">
    <p>
    <strong>{{err.text}}</strong>
    </p>
    <p>{{err.info}}</p>
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

import svgIcon from "@/components/svg";
export default {
  props: {
    err: {
      default: function() {
        return {
          code: 404,
          text: "你似乎来到了没有知识存在的荒原...",
          info: "请检查操作,但也可能是服务器出故障了ಥ_ಥ"
        }
      }
    },
  },
  components: {
    svgIcon
  },
};
</script>

<style scoped>
.logo {
  width: 120px;
  height: 43px;
  vertical-align: text-bottom;
  display: inline-block;
}
.error {
  margin: 169px auto 0;
  width: 404px;
}
.error .header {
  overflow: hidden;
  line-height: 1.2;
  margin: 0 0 0.33em 0.33em;
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

