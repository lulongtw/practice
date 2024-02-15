<script setup>
  import {RouterLink,RouterView} from "vue-router";


</script>

<template>
  <RouterLink to="/">com1</RouterLink>
  <RouterLink to="/com2">com2</RouterLink>
  <hr>
  <RouterView name="view1" v-slot="{Component}">
    <KeepAlive>
      <component :is="Component"></component>
    </KeepAlive>

  </RouterView>
</template>
<style scoped>
  .active{
    font-size:100px;
  }
</style>