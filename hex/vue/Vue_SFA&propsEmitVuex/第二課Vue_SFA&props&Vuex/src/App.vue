<script setup>
  import A from "./a.vue";
  import B from "./b.vue";
  import {ref} from "vue";

  let digit = 69
</script>

<template>
  <!-- 描述子組件時傳入props 屬性名就是props的變數名  後面的值是父組件的變數實體 -->
  <A :ans="digit"></A>
  <B></B>
</template>

