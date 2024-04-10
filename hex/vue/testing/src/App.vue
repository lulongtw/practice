<script setup></script>

<template>
  <router-link to="/com1">com1</router-link>
  <router-link to="/com2">com2</router-link>
  <hr>

    <router-view  v-slot="{Component}">
      <keep-alive>
      <component :is="Component"></component>
      </keep-alive>
    </router-view>

</template>
<style>
  .qq{
    color:red
  }
</style>