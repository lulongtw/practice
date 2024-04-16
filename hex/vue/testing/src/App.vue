<script setup>
import axios from 'axios';

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
  axios.defaults.headers.common.authorization = toSendCookie;
</script>
<template>
<router-view></router-view>
    
  
</template>
<style scoped>

</style>