<script setup>
  import axios from "axios";
  import {useRouter} from "vue-router";
  import {onMounted,ref} from "vue"; 

  import {noCatch} from "@/assets/functions"

  let router = useRouter();
  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;

  function logOut(){
    let url = headAPI+"/logout";
    noCatch(axios.post(url))
    .then(res=>{
      if(res.data.success){
        router.push("/fsaf")
      }
    })
  }

  onMounted(()=>{
    let url = `${headAPI}/api${myAPI}/admin/products?page=:page`;
    noCatch(axios.get(url))
    .then(res=>{
         //如果在登入後  在Index畫面時  進入console application 把cookies刪掉  就無法進入
      console.log(res)
    })
  })
</script>

<template>
  this is product

</template>