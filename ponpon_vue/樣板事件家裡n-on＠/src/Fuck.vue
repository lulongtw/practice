<script setup>
  let num = 1
  let func1 = function(){
    num++
    console.log(num)
  }
  let func2 = function(){
    console.log("prevent")
  }
  let func3 = function(){
    console.log("once")
  }  
</script>
<template>
  <div v-on:click="func1">1</div>
  <a href="http://www.google.com" @click.prevent="func2">2</a>
  <div @click.once="func3">3</div>
</template>
<style scoped>

</style>