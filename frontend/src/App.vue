<template>
  <div class="home">
    <TopBar></TopBar>
    <transition name="router-fade" mode="out-in">
      <keep-alive>
        <router-view v-if="$route.meta.keepAlive"></router-view>
      </keep-alive>
    </transition>
    <transition name="router-fade" mode="out-in">
      <router-view v-if="!$route.meta.keepAlive"></router-view>
    </transition>
  </div>
</template>

<script>
const TopBar = resolve => require(['@/components/topBar'], resolve)
export default {
  name: 'app',
  components: {TopBar}
}
</script>