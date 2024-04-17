<script setup>
import axios from 'axios';
import {ref,provide,computed} from "vue";
import States from "@/components/Status.vue";
import Page from "@/components/Pages.vue";

  //console.log(document.cookie);
  let cookies = document.cookie;
  let lst = cookies.split("; ")
  let toSendCookie ;
  lst.forEach(item=>{
    let temp = item.split("=");
    if (temp[0]=="renewToken"){
      toSendCookie = temp[1];
     // console.log(toSendCookie)
      return
    }
  })

  let isLoading = ref(false);
  provide('toggleLoading',()=>{
    isLoading.value = !isLoading.value
  })
  let statesLst = ref([])
  provide('showStatus',(newVal)=>{
    //console.log(statesLst.value.length,statesLst.value)
   // console.log(newVal)
    statesLst.value.push(newVal);
    
    //console.log(statesLst.value.length,statesLst.value)
  });


  axios.defaults.headers.common.authorization = toSendCookie;
</script>
<template>
  <div>
    <loading v-model:active="isLoading"/>
    <States :fromDad="statesLst"></States>
    <router-view></router-view>
  </div>

    
  
</template>
<style scoped>

</style>