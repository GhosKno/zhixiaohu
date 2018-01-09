<template>
<div class="sideBar">
  <div class="navList card">
        <a class="nav" href="javascript:void(0);">
            <svg class="sideBarIcon" viewBox="0 0 24 24" ><path d="M5.515 19.64l.918-5.355-3.89-3.792c-.926-.902-.639-1.784.64-1.97L8.56 7.74l2.404-4.871c.572-1.16 1.5-1.16 2.072 0L15.44 7.74l5.377.782c1.28.186 1.566 1.068.64 1.97l-3.89 3.793.918 5.354c.219 1.274-.532 1.82-1.676 1.218L12 18.33l-4.808 2.528c-1.145.602-1.896.056-1.677-1.218z" fill-rule="evenodd"></path></svg>
            <div class="nav-text" @click="$router.push({path: `/profile/${$store.state.userid}`})">我的收藏</div>
        </a>
        <a class="nav" href="javascript:void(0);">
            <svg class="sideBarIcon" viewBox="0 0 24 24"><path d="M4 10V8a1 1 0 1 1 2 0v2h2a1 1 0 0 1 0 2H6v2a1 1 0 0 1-2 0v-2H2a1 1 0 0 1 0-2h2zm10.455 2c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4zm-7 6c0-2.66 4.845-4 7.272-4C17.155 14 22 15.34 22 18v1.375c0 .345-.28.625-.625.625H8.08a.625.625 0 0 1-.625-.625V18z" fill-rule="evenodd" data-reactid="1247"></path></svg>
            <div class="nav-text">我的邀请</div>
        </a>
  </div>
<footer class="footer">
    <a class="footer-item" target="_blank" href="/">小看山</a>
    <span class="footer-dot"></span>
    <a class="footer-item" target="_blank" href="/">知小乎指南</a>
    <span class="footer-dot"></span>
    <a class="footer-item" target="_blank" href="/">知小乎协议</a>
    <br>
    <a class="footer-item" target="_blank" href="/">侵权举报</a>
    <span class="footer-dot"></span>
    <a class="footer-item" target="_blank" href="http://www.12377.cn">网上有害信息举报专区</a>
    <br>
    <span class="footer-item">违法和不良信息举报：010-82716601</span>
    <br>
    <a class="footer-item" target="_blank" href="/">联系我们</a><span> 
        © 2018 知小乎</span></footer>
</div>
</template>
<script>
export default {
  name: "sideBar"
};
</script>
<style scoped>
.sideBar li {
  padding: 10px 20px;
}
.nav{
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
}
.nav:hover {
    background: #f4f8fb;
}
.navList{
    width: 100%;
    padding: 8px 0;
}
.nav-text{
    -webkit-box-flex: 1;
    font-weight: 500;
    -ms-flex: 1;
    flex: 1;
    margin: 0 10px;
    text-align: left;
}
.sideBarIcon{
    width: 18px;
    height: 18px;
    fill: #9fadc7;
    vertical-align: text-bottom;
}
.footer{
    padding: 10px 0 10px 5px;
    font-size: 13px;
    line-height: 2;
    color: #8590a6;
}
.footer a{
    color: inherit;
    text-decoration: none;
}
.footer-dot:after {
    margin: 0 5px;
    content: "\B7";
}
</style>

