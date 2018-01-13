<template>
<div>
    <div class="topbar card">
        <div class="title">
            {{numOfAnswer}} 个回答
        </div>
        <Select style="float: right;width:100px" placeholder="默认排序">
            <Option v-for="item in answerSort" :value="item.value" :key="item.value">{{ item.label }}</Option>
        </Select>
    </div>
    <div class="main card">
    <AnswerCard
    class="answer"
    v-for="(item, index) in answerList"
    :key="index"
    :answer="item"
    @closeWriteAnswer="$emit('closeWriteAnswer')"
    :showQuestion="false">
    </AnswerCard>
    <Spin size="large" fix v-if="loading"></Spin>
    </div>
    <div style="text-align:center;font-size: 38px;color:#9eaad1;" v-if="!answerList.length">还没有任何回答 /(ㄒoㄒ)/~~</div>
</div>
</template>

<script>

const AnswerCard = resolve => require(["@/components/answerCard"], resolve);
import api from "@/utils/api";

export default {
  name: "AllAnswer",
  components: {
    AnswerCard,
  },
  data() {
    return {
      answerSort: [
        {
          value: "default",
          label: "默认排序"
        },
        {
          value: "time",
          label: "按时间排序"
        }
      ],
      loading: true,
      answerList: Array,
    };
  },
  props: {
      numOfAnswer: 0,
  },
  methods: {
    fetchAnswer: function() {
      api.getAnswersByQuestion(this.$route.params.q_id).then(
        res => {
          if (res.body.success == true) {
            this.answerList = res.body.data.results;
            this.loading = false;
          } else {
            this.$Message.error(res.body.msg);
            this.loading = false;
          }
          this.loading = false;
        },
        err => {
          this.$emit("err", { code: err.status, text: err.statusText });
          this.loading = false;
        }
      );
    }
  },
  mounted() {
    this.fetchAnswer();
  }
};
</script>

<style lang="less" scoped>
.topbar {
  background: #fff;
  border-bottom: 1px solid #f0f2f7;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  height: 50px;
  padding: 0 20px;
  .title {
    display: inline-block;
    font-size: 15px;
    font-weight: 600;
    font-synthesis: style;
    color: #1e1e1e;
  }
}
.main {
  padding: 0 16px;
  margin: 0 auto;
}

.answer {
  position: relative;
  padding: 5px 10px;
  margin-top: 10px;
  width: 688px;
}
.answer + .answer:after {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  margin: 0 20px;
  display: block;
  border-bottom: 1px solid #f0f2f7;
  content: "";
}
</style>
