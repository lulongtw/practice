<script setup>
  import {ref} from "vue";
  let props = defineProps(
    ["size","weight"]
  )
  let ck = ref(true)
  function bigger(){
    ck.value=!ck.value
  }
</script>

<template>
  <div @click="bigger">按我</div>
  <div :style="{fontSize:ck?'10px':props.size,fontWeight:ck?200:props.weight}">onevue</div>
</template>

<style scoped></style>