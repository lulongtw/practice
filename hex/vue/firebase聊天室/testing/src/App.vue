<script setup>
  import database from "@/firebase.js";
  import {ref as Fref,get,set,push,onValue} from "firebase/database";
  import {ref } from "vue"

  let testRef = Fref(database,"test");//取得路徑
  

  let text = ref("");
  let data = ref("")

  function send(){
    let newRef = push(testRef);//發送資料
    set(newRef,text.value)
  }

  onValue(testRef,(ss)=>{//監控資料
    let ans = ss.val();
    data.value = ans
  })




</script>
<template>
  <input type="text" v-model="text" @keyup.enter="send()">
  <div v-for="item in data">
      {{item}}
  </div>
</template>