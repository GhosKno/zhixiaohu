<template>
  <div>
    <div class="layout">
        <Menu mode="horizontal" :theme="navTheme" active-name="1"> 
            <div class="layout-logo">知小乎</div>
            <div class="layout-nav">
            <MenuItem name="1">
                <Icon type="ios-people"></Icon>
                广场
            </MenuItem>
            <MenuItem name="2">
                <Icon type="fireball"></Icon>
                热点
            </MenuItem>
            <MenuItem name="3">
                <Icon type="leaf"></Icon>
                最新
            </MenuItem>
            <MenuItem name="4">
                <Icon type="university"></Icon>
                提问
            </MenuItem>
            </div>
         </Menu>
        <div class="layout-content">
          <div class="layout-content-main">Content</div>
        </div>
    </div>
  </div>
</template>

<script>
	import cookieManage from '@/mixins/cookieManage'
	import initInfo from '@/mixins/initInfo'
  export default {
		name: 'IdxPage',
		mixins: [cookieManage, initInfo],
    data () {
        return {
            navTheme: 'light'
        }
		},
		methods: {
		},
		components: {
		},
		created () {
			console.log(this.initInfo())
		}
  }
</script>

<style scoped>
    .layout{
        float: left;
        width: 100vw;
        height: 100vh;
        border: 1px solid #d7dde4;
        background: #f5f7f9;
    }
    .layout-logo{
        width: 100px;
        height: 35px;
        border-radius: 3px;
        float: left;
        position: relative;
        top: 0;
        left: 60px;
        font-size: 30px;
    }
    .layout-nav{
        width: 420px;
        margin: 0 auto;
    }

    .layout-content{
        margin: 15px;
        overflow: hidden;
        background: #fff;
        border-radius: 4px;
    }
    .layout-content-main{
        padding: 10px;
    }
</style>
