<script setup>
  import axios from "axios";
  import {reactive,provide,ref,watch} from "vue";

  import Nono from "./components/sideComs/Nono.vue"
  import {getCookie} from "./assets/functions"
  let greenToken = getCookie("greenToken");

  let responseLst = reactive([]);
  provide("updtResponseLst",(newVal)=>{
    responseLst.push(newVal)
  })

  axios.defaults.headers.common.Authorization = greenToken
  
</script>

<template>


    <Nono :res="responseLst"></Nono>
    <router-view></router-view>



</template>

<style>

</style>