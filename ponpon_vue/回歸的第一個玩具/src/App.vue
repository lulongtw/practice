<script setup>
import {ref} from "vue";
  let word1 = "下雨"
  let word2 = "晴天"
  let weather = ref(true)
</script>
<template>
  <input type="checkbox" v-model="weather">
  <div v-html="weather?word1:word2" :class="weather?'class1':'class2'"></div>
</template>

<style scoped>
  .class1{
    color:red
  }
  .class2{
    color:blue
  }
</style>