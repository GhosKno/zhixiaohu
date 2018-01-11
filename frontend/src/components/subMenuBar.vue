<template>
<div class="card sub-menu-bar">
    <Button type="text" class="sub-menu-btn" @click="$refs['questionModal'].open()">
        <svg class="icon" >
            <use xlink:href="#ask"></use>
        </svg>
        提问
    </Button>
    <Button type="text" class="sub-menu-btn">
        <svg class="icon" >
            <use xlink:href="#answer"></use>
        </svg>
        回答
    </Button>
    <Button type="text" class="sub-menu-btn">
        <svg class="icon" >
            <use xlink:href="#write"></use>
        </svg>
        写文章
    </Button>
    <Button type="text" class="sub-menu-btn btn-right">
        草稿
    </Button>
    <question-modal ref="questionModal"></question-modal>
</div>
</template>
<script>
import questionModal from '@/components/questionAskModal.vue'
export default {
  name: 'subMenuBar',
  data () {
    return {}
  },
  methods: {
	},
	components: {
		questionModal
	}
}
</script>

<style scoped>
    .sub-menu-bar{
        line-height: 58px;
    }
    .sub-menu-btn{
        font-size: 16px;
        width: 100px;
        height: 58px;
    }
    .btn-right{
        font-weight: 600;
        color:#8590a6;
        float: right;
    }
    .icon{
        vertical-align: text-bottom;
        margin-bottom: -5px;
        width: 24px;
        height: 24px;
    }
</style>
