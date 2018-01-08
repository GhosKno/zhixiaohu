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
								:avatar="item.avatar"
								:name="item.name"
                :pk="item.pk"
								:feed-title="item.feedTitle" 
								:coverImg="item.coverImg"
								:question="item.question" 
								:answer="item.answer"
							>
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
      answerList: [
        {
          authorName: "ccc",
          pk: "3",
          feedTitle: "热门内容,来自: 历史",
          question: "这个",
          coverImg: "https://avatars3.githubusercontent.com/u/9395718?s=460&v=4",
          answer:
            "泻药.这个答案是一个示例答案.这个示例答案很长很长很长很长很长很长很长很长很长很长很长很长很长dd很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很od"
        },
        {
          authorName: "kiki",
          pk: "4",
          feedTitle: "热门内容,来自: 编程",
          question: "作为一名程序员，我这属于什么水平？",
          answer:
            "南海仲裁案之后，2016年7月16日，在美国国务院记者会上，凤凰卫视记者王冰汝向美国国务院发言人马克·托纳提问：“新加坡国立大学国际法中心在网站上刊登了地图和地名词典，其中一份地图，它的来源是美国政府，而且这张地图上写的是太平岛，而不是太平礁，这跟南海仲裁案“仲裁”结果不很舒服卡仕"
        },
        {
          authorName: "kiki",
          pk: "4",
          feedTitle: "热门内容,来自: 编程",
          question: "作为一名程序员，我这属于什么水平？",
          answer:
            "南海仲裁案之后，2016年7月16日，在美国国务院记者会上，凤凰卫视记者王冰汝向美国国务院发言人马克·托纳提问：“新加坡国立大学国际法中心在网站上刊登了地图和地名词典，其中一份地图，它的来源是美国政府，而且这张地图上写的是太平岛，而不是太平礁，这跟南海仲裁案“仲裁”结果不..."
        },
        {
          authorName: "kiki",
          pk: "4",
          feedTitle: "热门内容,来自: 编程",
          question: "作为一名程序员，我这属于什么水平？",
          answer:
            "南海仲裁案之后，2016年7月16日，在美国国务院记者会上，凤凰卫视记者王冰汝向美国国务院发言人马克·托纳提问：“新加坡国立大学国际法中心在网站上刊登了地图和地名词典，其中一份地图，它的来源是美国政府，而且这张地图上写的是太平岛，而不是太平礁，这跟南海仲裁案“仲裁”结果不..."
        },
        {
          authorName: "kiki",
          pk: "4",
          feedTitle: "热门内容,来自: 编程",
		  question: "作为一名程序员，我这属于什么水平？",
		  coverImg: "https://avatars3.githubusercontent.com/u/9395718?s=460&v=4",
          answer:
            "南海仲裁案之后，2016年7月16日，在美国国务院记者会上，凤凰卫视记者王冰汝向美国国务院发言人马克·托纳提问：“新加坡国立大学国际法中心在网站上刊登了地图和地名词典，其中一份地图，它的来源是美国政府，而且这张地图上写的是太平岛，而不是太平礁，这跟南海仲裁案“仲裁”结果不..."
        },
        {
          authorName: "kiki",
          pk: "4",
          feedTitle: "热门内容,来自: 编程",
          question: "作为一名程序员，我这属于什么水平？",
          answer:
            "南海仲裁案之后，2016年7月16日，在美国国务院记者会上，凤凰卫视记者王冰汝向美国国务院发言人马克·托纳提问：“新加坡国立大学国际法中心在网站上刊登了地图和地名词典，其中一份地图，它的来源是美国政府，而且这张地图上写的是太平岛，而不是太平礁，这跟南海仲裁案“仲裁”结果不..."
        }
      ]
    };
  },
  methods: {
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
