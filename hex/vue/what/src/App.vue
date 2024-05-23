<script setup>
import { ref } from "vue";

let lst = ref([]);
let ck1 = ref("");
let ck2 = ref('')
</script>

<template>
  <div :style="{color:'red',backgroundColor:'blue'}">dsad</div>
  <div :style="`color:red;background-color:blue`">dsadsaadd</div>
</template>

<style>
.a{
  color:red
}
.b{
  background-color: blue;
}
</style>
