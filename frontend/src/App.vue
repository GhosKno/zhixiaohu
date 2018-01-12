<template>
  <div>
    <err-page :err="err" v-if="hasErr"></err-page>
    <section v-else>
      <TopBar class="top-bar"></TopBar>
      <transition name="router-fade" mode="out-in">
        <keep-alive>
          <router-view v-if="$route.meta.keepAlive" @err="handleErr"></router-view>
        </keep-alive>
      </transition>
      <transition name="router-fade" mode="out-in">
        <router-view v-if="!$route.meta.keepAlive" @err="handleErr"></router-view>
      </transition>
    </section>
    <svg-icon></svg-icon>
  </div>
</template>

<script>
import ErrPage from "@/views/errors/err";
import svgIcon from "@/components/svg";
import TopBar from "@/components/topBar";
export default {
  name: "app",
  components: {
    svgIcon,
    TopBar,
    ErrPage,
  },
  data(){
    return {
      err: {},
      hasErr: false
    }
  },
  methods: {
    handleErr:function(err){
      this.hasErr=true
      this.err=err
    }
  },
  watch:{
    '$route' (to,from){
      this.hasErr = false;
    }
  }
};
</script>
