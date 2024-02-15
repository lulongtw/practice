<script setup>
  import axios from "axios";
  import {useRouter} from "vue-router";
  import {onMounted} from "vue";

  let router = useRouter();


  function logOut(){
    let headAPI = import.meta.env.VITE_headAPI;
    axios.post(headAPI+"/logout")
    .then(res=>{
      router.push("/")
    }).catch(res=>{
      console.log("shit",res)
    })
  }

  onMounted(()=>{
    let headAPI = import.meta.env.VITE_headAPI;
    let myAPI = import.meta.env.VITE_myAPI;
    let url = `${headAPI}/api${myAPI}/admin/products?page=:page`
    axios.get(url)
    .then(res=>{
      //這邊是確認只有在登入狀態才能進入這個API
      //如果在登入後  在Index畫面時  進入console application 把cookies刪掉  就無法進入
      console.log(res)
    })

  })

</script>

<template>
  this is index
  <a @click.prevent="logOut()">log out</a>

</template>