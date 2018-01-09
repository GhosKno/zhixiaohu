<template>
  <div>
	  <TopBar class="top-bar"></TopBar>
		<Scroll
			:on-reach-bottom="handleReachBottom"
			:height="900"
		>
				<div class="container">
					<div class="main">
						<SubMenuBar></SubMenuBar>
					 	<div class="feed-flow">
							<AnswerListCard
								v-for="(item, index) in answerList"
                :key="index"
                :answer="item">
							</AnswerListCard>
						</div>			
					</div>
					<SideBar class="sidebar"></SideBar>
				</div>	
		</Scroll>
  </div>
</template>

<script>
const SubMenuBar = resolve => require(["@/components/subMenuBar"], resolve);
const AnswerListCard = resolve =>
  require(["@/components/answerListCard"], resolve);
const SideBar = resolve => require(["@/components/sideBar"], resolve);
const TopBar = resolve => require(["@/components/topBar"], resolve);

import cookieManage from "@/mixins/cookieManage";
import initInfo from "@/mixins/initInfo";
export default {
  name: "IdxPage",
  mixins: [cookieManage, initInfo],
  components: { SubMenuBar, TopBar, AnswerListCard, SideBar },
  data() {
    return {
      windowHeight: "",
      answerList: {
          type: Array,
      }
    };
  },
  methods: {
    fetchAnswerList() {
      this.$http.get(`/api/answers/`)
          .then(res => {
            if(res.body.success==true) {
             
              this.answerList=res.body.data.results
              console.log(this.answerList)
            } else {
              this.$Message.error(res.body.msg);
            }
          }, function(response){
            // 响应错误回调 
             this.err=true
             this.errCode=response.status
             this.errText=response.statusText
          });
    },
    handleReachBottom() {
      return new Promise(resolve => {
        setTimeout(() => {
          this.answerList.push(...this.answerList);
          resolve();
        }, 2000);
      });
    }
  },
  created() {
    this.fetchAnswerList();
    if (this.initInfo()) {
      this.$router.push({ name: "home" });
    }
  }
};
</script>

<style scoped>
.container {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: start;
  -ms-flex-align: start;
  align-items: flex-start;
  position: relative;
  width: 1000px;
  margin-top: 10px;
  margin: 10px auto;
}
.main {
  width: 679px;
}
.sidebar {
  width: 296px;
  padding: 0 16px;
}
</style>
