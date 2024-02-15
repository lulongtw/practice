<script setup>
  import {RouterView,RouterLink} from "vue-router";
</script>
  
<template>
  this is com4 <br>
  <RouterLink to="/com2">child1</RouterLink>
  <RouterLink to="/com2/child2">child2</RouterLink>
  <RouterLink to="/com2/child3">child3</RouterLink>
  <hr>
  <RouterView name="childView"></RouterView>
</template>
<style scoped></style>