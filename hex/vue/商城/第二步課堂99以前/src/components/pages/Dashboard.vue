<script setup>
  import {useRouter} from "vue-router";

  let router = useRouter();
  


</script>

<template>
this is Dashboard
<br>
<a @click.prevent="router.push('/login')">click to login</a>

</template>

<style>

</style>