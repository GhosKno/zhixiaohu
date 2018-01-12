<template>
    <div>
        <Button class="topbar" @click="$router.push({path:'/question/'+$route.params.q_id})">
            共 {{numOfAnswer}} 个回答，查看其它回答
        </Button>
        <div class="answer card">
        <AnswerCard
         v-id="answer.id"
         :answer="answer"
         :fold="false"
        ></AnswerCard>
        <Spin size="large" fix v-if="loading"></Spin>
        </div>
    </div>
</template>

<script>
const AnswerCard = resolve => require(["@/components/answerCard"], resolve);
import api from "@/utils/api";

export default {
  name: "AnswerPage",
  components: {
    AnswerCard
  },
  data() {
    return {
      answer: {},
      loading: true,
    };
  },
  props: {
    numOfAnswer: 0,
    newAnswer: {}
  },
  methods: {
    fetchAnswer: function() {
      api.getAnswer(this.$route.params.a_id).then(
        res => {
          if (res.body.success == true) {
            if(res.body.data.question.id!=this.$route.params.q_id){
              this.$emit("err");
            }
            this.answer = res.body.data;
            this.loading = false;
          } else {
            this.$emit("err");
          }
        },
        err => {
          this.$emit("err", { code: err.status, text: err.statusText });
        }
      );
    }
  },
  mounted() {
    this.fetchAnswer();
  },
  watch:{
    '$route' (to, from){
      this.fetchAnswer();
    }
  }

};
</script>

<style lang="less" scoped>
.topbar {
  width: 100%;
  font-size: 16px;
}
.answer {
  padding: 0 10px;
  margin: 20px auto;
}
</style>


