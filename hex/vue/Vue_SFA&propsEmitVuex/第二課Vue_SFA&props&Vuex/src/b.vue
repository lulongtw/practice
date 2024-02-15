<script setup>
 import store from "./store.js"
 import {ref,watch} from "vue"

 let ans = ref(store.state.msg)



 watch(() => store.state.msg, 
       () =>{ans.value = store.state.msg})
       //也可以這樣寫
      // (newValue) => {ans.value = newValue;})

  /*
  watch(參數1,參數2)

  參數1是一個函式  ()=>監視的值
  參數2也他媽是函式 (監視到的新值,舊值)=>{看你要幹嘛}

  參數1為什麼是一個函式  跟getter有關@@
  */ 
 
</script>


<template>{{ans}}</template>

