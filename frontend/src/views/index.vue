<template>
  <div>
	  <TopBar class="top-bar"></TopBar>
		<Scroll
			:on-reach-bottom="handleReachBottom"
			:height="windowHeight"
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
      },
      nextUrl: ''
    };
  },
  methods: {
    fetchAnswerList() {
      this.$http.get(`/api/answers/`)
          .then(res => {
            if(res.body.success==true) {
              this.answerList=res.body.data.results
              this.nextUrl = res.body.data.next
            } else {
              this.$Message.error(res.body.msg);
            }
          }, function(response){
            this.$Message.error(response.status + " " + response.statusText);
          });
    },
    handleReachBottom() {
      return new Promise(resolve => {
        if(this.nextUrl == null || this.nextUrl.length == 0) {
          this.$Message.info('没有更多的内容了')
          return resolve()
        }
        this.$http.get(this.transUrl(this.nextUrl))
          .then(res => {
            this.nextUrl = res.body.data.next
            setTimeout(() => {
              this.answerList.push(...(res.body.data.results));
              resolve();
            }, 1000);
          })
      });
    }
  },
  mounted () {
    this.windowHeight = Math.max(document.body.clientHeight, 900)
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
