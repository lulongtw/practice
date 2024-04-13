<script setup>
  import {useRouter} from "vue-router";
  import {ref} from "vue";
  let lst = ref(['surfeit','subvert','discomfit']);
  let router = useRouter();

  function goTo(item,idx){
    router.push({
      name:'com2',
      params:{id:item},
      query:{idx:idx}
    })
  }
</script>
<template>
  <router-link to="/com1">com1</router-link>
  <div @click="goTo(item,idx)" v-for="(item,idx) in lst">{{item}}</div>
  <hr>
  <!-- <router-view>
    <keep-alive v-slot="{Component}">
      <component :is="Component"></component>
    </keep-alive>
  </router-view> -->
  <router-view></router-view>
</template>
<style>

</style>