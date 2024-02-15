<script setup>
    import {RouterLink,RouterView} from "vue-router";
    import "./fbconfig.js"



</script>

<template>
    <RouterLink to="/">com1</RouterLink>
    <br>
    <router-link to="/com2">com2</router-link>
    <hr>

    <router-view v-slot="{ Component }">
  <keep-alive>
    <component :is="Component" />
  </keep-alive>
</router-view>
  
</template>

<style scoped></style>