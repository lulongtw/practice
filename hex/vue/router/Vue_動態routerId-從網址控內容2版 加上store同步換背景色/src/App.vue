<script setup>
  import {ref} from "vue";

  let lst = ref(['dick','penis','asshole']);
</script>

<template>
    <router-link to="/com1">com1</router-link>
    <router-link v-for="(item,idx) in lst"
      :to="{name:'/com2',params:{id:item},query:{dataSet:idx}}"

    ><div>{{item}}</div></router-link>
    <hr>
    <router-view v-slot="{Component}">
      <keep-alive>
        <component :is="Component"></component>
      </keep-alive>
    </router-view>
</template>

<style scopted>

</style>