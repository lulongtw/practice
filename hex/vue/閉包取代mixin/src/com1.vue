<script setup>

  import {num,add,useNum} from "@/function.js"
  let {num2,add2} = useNum();
</script>

<template>
  <hr>
  this is com1
  <div @click="add">{{num}}</div>
  <div @click="add2">{{num2}}</div>


</template>