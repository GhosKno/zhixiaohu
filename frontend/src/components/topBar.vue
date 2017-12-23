<template>
    <Menu mode="horizontal" :theme="theme1" active-name="1" class="menu">
    <div class="logo">
        <svg width="180" height="60">
        <text x="21.84" y="43.658" fill="#3b89e4" font-family="Wawati SC" font-size="42.667">
            知小乎
        </text>
        <path fill="#fff" d="M49 25.994a24.8 24.8 0 0 1 7.117.494c2.321.66 3.63 2.611 2.542 1.977.817.476 1.059.179 2.033 0s1.747-3.051 0-3.46a31.906 31.906 0 0 0-7.626-1.483c-3.221-.063-3.926.431-4.066 2.472z"/>
        <path fill="#fff" d="M49.508 25.994s8.835-.239 9.659 1.483 2.542-.494 2.542-.494a1.5 1.5 0 0 1-1.525 1.483c-1.532.085-4.414-1.393-5.592-1.483s-5.084-.494-5.084-.494v-.495z"/>
        <path fill="red" fill-rule="evenodd" d="M50.017 24.017s2.9-4.579 11.184-3.955c7.657.577 5.507 4.347 5.592 4.943s-2.975 7.46-4.575 8.4a23.6 23.6 0 0 0 .508-4.943 2.625 2.625 0 0 0-2.034-1.977c-.857-.34-2.912-2.049-4.067-1.977s-4.691-1.408-6.608-.491z"/>
        <path fill="#fff" d="M62.569 32.1s-2.107-.833-1.122 1.236 3 .582 2.8 0a4.012 4.012 0 0 0-1.678-1.236z"/>
        <path fill="#ebebeb" d="M63.235 32.42s.489 2.468-1.525 1.483c.224.687 1.649 1.8 2.542.494s-1.017-1.977-1.017-1.977z"/>
        <path fill="#eb2a2a" fill-rule="evenodd" d="M61.71 26.983s2.089-2.025 2.542-2.472c.012 1.62-.655 6.232-1.525 7.415-.949-.211 1.422-4.277-1.017-4.943z"/>
        </svg>
    </div>  
    <Nav>
    <MenuItem name="1">
        广场
    </MenuItem>
    <MenuItem name="2">
        热点
    </MenuItem>
    <MenuItem name="3">
        话题
    </MenuItem>
    </Nav>

    <div class="search">
        <input maxlength="50" type="text" placeholder="搜索你感兴趣的问题...">
        <Button type="text" class="searchBtn"><Icon type="search" size=16></Icon></Button>
    </div>
    <div class="rightBtns">
        <Button type="ghost" class="loginBtn">登录</Button>
        <Button type="info" class="joinBtn">加入知小乎</Button>
        </div>
</Menu>
</template>

<script>
export default {
    name: 'topBar',
    data () {
        return {
            theme1: 'light'
        }
    },
}
</script>

<style scoped>
.menu{
        display: flex;
    }
    .ivu-menu-item{
        font-size: 15px;
        font-weight: 600;
    }
    .logo{
        margin-left: 140px;
    }
    .search{
        margin-left: 20px;
    }
    .search input {
        background: transparent;
        border: 0;
        border-bottom: 1px solid #414648;
        background-size: auto 16px;
        line-height: 20px;
        padding-bottom: 10px;
        padding-right: 25px;
        font-family: "open sans";
        font-weight: 300;
        font-size: 14px;
        width: 200px;
        -webkit-transition: border .2s;
        outline:none;
        transition: 0.2s;
        -moz-transition: 0.2s; /* Firefox 4 */
        -webkit-transition: 0.2s; /* Safari 和 Chrome */
        -o-transition: 0.2s; /* Opera */
    }
    .search input:hover,.search input:focus{
        width: 250px;
        border-bottom: 2px solid #0096d1;
    }
    .search input:focus + .searchBtn{
        color: rgb(4, 139, 230);
    }
    .searchBtn{
        margin-left: -40px;
        transition: 0.5s;
        -moz-transition: 0.5s; /* Firefox 4 */
        -webkit-transition: 0.5s; /* Safari 和 Chrome */
        -o-transition: 0.5s; /* Opera */
    }
    .rightBtns{
        position: absolute;
        right: 80px;
    }
    @media screen and (max-width: 1060px){
        .logo{
            margin-left: 10px;
        }
        .rightBtns{
            right:10px;
        }
    }
</style>
