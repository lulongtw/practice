<script setup>
  import axios from "axios";
  import {watch,ref,onMounted} from "vue";

  import {noCatch} from "@/assets/functions";
  
  let data = ref([]);

  onMounted(async ()=>{
    let headAPI = import.meta.env.VITE_headAPI;
    let myAPI = import.meta.env.VITE_myAPI;
    let url = `${headAPI}/api${myAPI}/admin/orders?page=:page`;
    noCatch(axios.get(url)
      .then(res=>{
        console.log(res)
      })
    )
  })
</script>

<template>
  orderlist

</template>

<style>

</style>