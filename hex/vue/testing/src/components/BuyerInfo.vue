<script setup>
import axios from 'axios';
import {ref,onMounted,inject,watch} from "vue";
import {headAPI,myAPI,getData,getDot} from "@/functions.js";
import {useRouter} from "vue-router";

let cartInfo = ref([]);

onMounted(async()=>{
  let url = `${headAPI}/api${myAPI}/cart`;
  let method = 'get';
  let res = await getData(url,method);
  if (res.data.success){
    console.log(res)
    cartInfo.value = res.data.data
  }
})



</script>
<template>

</template>