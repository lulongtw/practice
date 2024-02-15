<script setup>
  import {useRouter} from "vue-router";
  let router = useRouter();

</script>

<template>
  this is dashboard
  <br>
  <a @click.prevent="router.push('/login')">Login</a>
  <!-- <router-link to="/login">Login</router-link> -->
</template>