<template>
<div class="sideBar">
  <div class="navList card">
        <a class="nav" @click="$router.push({path: `/profile/${$store.state.userid}#favorite`})">
            <svg class="sideBarIcon">
                <use xlink:href="#star"></use>
            </svg>
            <div class="nav-text"> 我的收藏</div>
        </a>
        <a class="nav" @click="$Notice.info({desc:'没有人邀请你（此功能待开发..(๑•ᴗ•๑)'})">
            <svg class="sideBarIcon">
                <use xlink:href="#invite"></use>
            </svg>
            <div class="nav-text"> 我的邀请</div>
        </a>
  </div>
<footer class="footer">
    <a class="footer-item" href="/">小看山</a>
    <span class="footer-dot"></span>
    <a class="footer-item" href="/">知小乎指南</a>
    <span class="footer-dot"></span>
    <a class="footer-item" href="/">知小乎协议</a>
    <br>
    <a class="footer-item" href="/">侵权举报</a>
    <span class="footer-dot"></span>
    <a class="footer-item" href="http://www.12377.cn">网上有害信息举报专区</a>
    <br>
    <span class="footer-item">违法和不良信息举报：010-82716601</span>
    <br>
    <a class="footer-item" href="/">联系我们</a><span> 
        © 2018 知小乎</span></footer>
</div>
</template>
<script>
export default {
  name: "sideBar"
};
</script>
<style lang="less" scoped>
.navList {
  width: 100%;
  padding: 8px 0;
  .nav {
    color: #8590a6;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    padding: 0 15px;
    height: 40px;
    overflow: hidden;
    &:hover {
      background: #f4f8fb;
    }

    .sideBarIcon {
      width: 18px;
      height: 18px;
      fill: #9fadc7;
      vertical-align: text-bottom;
    }
    .nav-text {
      -webkit-box-flex: 1;
      font-weight: 500;
      -ms-flex: 1;
      flex: 1;
      margin: 0 10px;
      text-align: left;
    }
  }
}
.footer {
  padding: 10px 0 10px 5px;
  font-size: 13px;
  line-height: 2;
  color: #8590a6;
  a {
    color: inherit;
    text-decoration: none;
  }
  .footer-dot:after {
    margin: 0 5px;
    content: "\B7";
  }
}
</style>

