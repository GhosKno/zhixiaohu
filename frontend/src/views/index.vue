<template>
  <div>
		<Scroll :on-reach-bottom="handleReachBottom" :height="windowHeight">
		  <div class="container">
				<div class="main">
          <SubMenuBar></SubMenuBar>
          <div class="section">
            <AnswerListCard
              v-for="(item, index) in answerList"
              :key="index"
              :answer="item">
            </AnswerListCard>
            <div style="color: #9eaad1;text-align: center;" v-if="emptyList">
              <div style="font-size: 70px;">щ(ﾟДﾟщ)!||<br/> 空无一物</div>
              _(:з」∠)_快去写点回答吧
            </div>
            <Spin size="large" fix v-if="loading"></Spin>
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

import cookieManage from "@/mixins/cookieManage";
import initInfo from "@/mixins/initInfo";
import api from "@/utils/api";

export default {
  name: "home",
  mixins: [cookieManage, initInfo],
  components: { SubMenuBar, AnswerListCard, SideBar },
  data() {
    return {
      windowHeight: 900,
      answerList: {},
      nextUrl: "",
      emptyList: false,
      loading: true
    };
  },
  methods: {
    fetchAnswerList() {
      api.getAnswers().then(
        res => {
          if (res.body.success == true) {
            this.answerList = res.body.data.results;
            this.nextUrl = res.body.data.next;
          } else {
            this.$Message.error(res.body.msg);
          }
          this.loading = false;
        },
        res => {
          this.$Message.error(res.status + " " + res.statusText);
          this.loading = false;
        }
      );
    },
    handleReachBottom() {
      return new Promise(resolve => {
        if (this.nextUrl == null || this.nextUrl.length == 0) {
          this.$Message.info("没有更多的内容了");
          return resolve();
        }
        this.$http.get(this.transUrl(this.nextUrl)).then(res => {
          this.nextUrl = res.body.data.next;
          setTimeout(() => {
            this.answerList.push(...res.body.data.results);
            resolve();
          }, 1000);
        });
      });
    }
  },
  created() {
    this.fetchAnswerList();
  },
  watch: {
    loading() {
      if (!this.answerList.length) {
        this.emptyList = true;
      }
      if (this.answerList.length < 3) {
        this.windowHeight = window.innerHeight - 60;
      }
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
