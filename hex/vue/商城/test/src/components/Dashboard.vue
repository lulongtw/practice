<script setup>
  import axios from "axios";
  import {useRouter} from "vue-router"

  import {noCatch} from "@/assets/functions";
  import HeaderNav from "./sideComs/HeaderNav.vue";
  import SideNav from "./sideComs/SideNav.vue"

  let router = useRouter();

  function logOut(){
    let headAPI = import.meta.env.VITE_headAPI;
    let url = headAPI + "/logout";
    noCatch(axios.post(url)
      .then(res=>{
        router.push("/")
      })
    )
  } 


</script>

<template>
  <HeaderNav></HeaderNav>
 <div class="container-fluid">
   <div class="row">
    <SideNav></SideNav>
     <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">  
      <router-view></router-view>  
     </main>
   </div>
 </div>
</template>

<style>

</style>