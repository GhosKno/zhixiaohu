<template>
  <Dropdown trigger="custom" :visible="!showAskBtn" :transfer="true" placement="bottom-start" @on-click="handleSearchResult">    
    <div class="search" :class="{'is-active':showAskBtn}">
      <div class="wrapper">
        <input class="input" 
          maxlength="50" 
          type="text" 
            placeholder="搜索你想知道的问题..." required 
          v-model="searchData"
          @focus="showAskBtn = false" 
          @blur="showAskBtn = true"
          @keyup="handleSearch()"
          @keydown.enter="seeAll"
          ref="input">
        <Button type="text" class="searchBtn" @click="seeAll()"><Icon type="ios-search-strong" class="searchIcon" size=20 ></Icon></Button>  
      </div>
      <Button type="primary" class="askBtn" :class="{'is-active':showAskBtn}" @click="$emit('ask')">提问</Button>
    </div>
    <DropdownMenu  v-if="searchData" slot="list" style="width: 380px;max-height: 500px;" >
        <div class="divider" v-if="Questions.length">
          问题
        </div>
        <DropdownItem 
          v-for="(ques, index) in Questions"
          :key="'q'+index"
          :name="'q'+ques.id"
          style="line-height: 16px;"
          >
          <div class="search-res">
          <div class="question">{{ques.title}}</div>
          <span class="answer-count">{{ques.answer_count}} 个回答</span>
          </div>
        </DropdownItem>

        <div class="divider" v-if="Answers.length">
          回答
        </div>
        <DropdownItem 
          v-for="(ans, index) in Answers"
          :key="'a'+index"
          :name="'a'+ans.question.id+'/answer/'+ans.id"
          >
          <div class="search-res">
            <Avatar size="small" :src="ans.userSummary.avatar"></Avatar>
            <span class="name">{{ans.userSummary.nickname}}</span>
            在 <span class="question in">{{ans.question.title}}</span> 下的回答
            <div class="question-detail" v-html="getContent(ans.detail)"></div>
          </div>
        </DropdownItem>

        <div class="divider" v-if="Topics.length">
          话题
        </div>
        <DropdownItem 
          v-for="(topic, index) in Topics"      
          :key="'t'+index"
          :name="'t'+topic.id"
          >
          <div class="search-res">
          <span class="tag">{{topic.label}}</span>
          <span class="intro">{{topic.introduction}}</span>
          </div>
        </DropdownItem>

        <div class="divider" v-if="Profiles.length">
          用户
        </div>
        <DropdownItem 
          v-for="(user, index) in Profiles"      
          :key="'u'+index"
          :name="'u'+user.id"
          >
          <div class="search-res">
          <Avatar :src="user.avatar"></Avatar>
          <span class="name">{{user.nickname}}</span>
          <span class="intro">{{user.description}}</span>
          </div>
        </DropdownItem>
        <div class="dropDownInfo" v-if="searchData && !(Questions.length || Topics.length || Answers.length)">
          没有找到有关的内容
        </div>
        <DropdownItem class="dropDownInfo" name="seeAll" divided v-else>
          查看所有搜索结果
        </DropdownItem>
    </DropdownMenu>
  </Dropdown>
</template>
<script>
import api from "@/utils/api";
import common from "@/utils/common";

export default {
  name: "searchBox",
  data() {
    return {
      showAskBtn: true,
      searchData: "",
      Questions: [],
      Answers: [],
      Topics: [],
      Profiles: []
    };
  },
  methods: {
    searchQuestion() {
      api.searchQuestion(this.searchData).then(
        res => {
          if (res.body.success) {
            this.Questions = res.body.data.results;
          } else {
            this.$Message.error(res.body.msg);
          }
        },
        err => {
          this.$Message.error(err.status + " " + err.statusText);
        }
      );
    },
    searchAnswer() {
      api.searchAnswers(this.searchData).then(
        res => {
          if (res.body.success) {
            this.Answers = res.body.data.results;
          } else {
            this.$Message.error(res.body.msg);
          }
        },
        err => {
          this.$Message.error(err.status + " " + err.statusText);
        }
      );
    },
    searchTopic() {
      api.searchTopics(this.searchData).then(
        res => {
          if (res.body.success) {
            this.Topics = res.body.data.results;
          } else {
            this.$Message.error(res.body.msg);
          }
        },
        err => {
          this.$Message.error(err.status + " " + err.statusText);
        }
      );
    },
    searchProfile() {
      api.searchProfile(this.searchData).then(
        res => {
          if (res.body.success) {
            this.Profiles = res.body.data.results;
          } else {
            this.$Message.error(res.body.msg);
          }
        },
        err => {
          this.$Message.error(err.status + " " + err.statusText);
        }
      );
    },
    handleSearch() {
      if (this.searchData != "") {
        this.searchQuestion();
        this.searchAnswer();
        this.searchTopic();
        this.searchProfile();
      }
    },
    handleSearchResult(id) {
      if (id.length == 1) return;
      if (id[0] == 'a') {
        this.$router.push({ path: "/question/" + id.slice(1) });
      } else if (id[0] == 'q') {
        this.$router.push({ path: "/question/" + id.slice(1) });
      } else if (id[0] == 't') {
        this.$router.push({ path: "/topic/" + id.slice(1) });
      } else if (id[0] == 'u') {
        this.$router.push({ path: "/profile/" + id.slice(1) });
      } else if (id == 'seeAll') {
        this.seeAll()
      }
    },
    seeAll(){
      this.$refs.input.blur()
      this.$router.push({ path: "/search/?query=" + this.searchData });
    },
    getContent(html) {
      return common.getContent(html);
    }
  }
};
</script>

<style lang="less" scoped>
.search {
  position: relative;
  -webkit-transition: all 0.2s;
  transition: all 0.2s;
  &.is-active {
    padding-right: 94px;
  }
  .wrapper {
    position: relative;
    .input {
      width: 300px;
      height: 34px;
      padding-left: 10px;
      padding-right: 50px;
      font-size: 14px;
      border: 1px solid #e7eaf1;
      border-radius: 3px;
      -webkit-box-sizing: border-box;
      box-sizing: border-box;
      background: #f7f8fa;
      border: none;
      outline: none;
      -webkit-transition: all 0.2s;
      transition: all 0.2s;
      &:focus {
        width: 380px;
        background: #fff;
        border: 1px solid #9fadc7;
      }
      &::placeholder {
        color: #9fadc7;
        font-weight: 500;
      }
    }
    .input:focus + .searchBtn .searchIcon {
      color: #0f88eb;
    }
    .input:valid + .searchBtn .searchIcon {
      color: #fff;
    }
    .input:valid + .searchBtn {
      background: #0f88eb;
      border-top-left-radius: 0;
      border-bottom-left-radius: 0;
      height: 100%;
    }
    .searchBtn {
      position: absolute;
      right: 0;
      top: 0;
    }
    .searchIcon {
      color: #8590a6;
    }
  }
  .askBtn {
    position: absolute;
    right: 15px;
    bottom: 0;
    opacity: 0;
    transform: scale(0);
    -webkit-transform: scale(0);
    transition: opacity 0.2s, transform 0.2s, -webkit-transform 0.2s;
    &.is-active {
      opacity: 1;
      transform: scale(1);
    }
  }
}
.divider {
  color: #8590a6;
  margin: 7px 16px;
  padding: 4px 0;
  border-bottom: 1px solid #f6f6f6;
}
.dropDownInfo {
  text-align: center;
  color: #666666;
}
.search-res {
  width: 100%;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  .name {
    font-weight: 500;
    font-size: 12px;
  }
  .question {
    width: 280px;
    display: inline-block;
    font-weight: 500;
    font-size: 14px;
    white-space: nowrap;
    text-overflow: ellipsis;
    -o-text-overflow: ellipsis;
    overflow: hidden;
    &.in {
      width: auto;
      max-width: 190px;
      vertical-align: top;
    }
  }
  .question-detail{
    width: 280px;
    white-space: nowrap;
    text-overflow: ellipsis;
    -o-text-overflow: ellipsis;
    overflow: hidden;
  }
  .answer-count {
    float: right;
    font-size: 12px;
    color: #8590a6;
  }
  .intro {
    font-size: 14px;
    color: #8590a6;
  }
  .tag {
    padding: 5px 10px;
    color: #3e7ac2;
    background: #eef4fa;
    border-radius: 100px;
  }
}
</style>
