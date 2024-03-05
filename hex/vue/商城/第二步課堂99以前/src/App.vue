<script setup>
import axios from "axios";
import {getCookie,a} from "@/assets/function.js";

let nextCookie = getCookie("nextToken");
//console.log(nextCookie)
axios.defaults.headers.common.Authorization = nextCookie;
</script>

<template>
  <router-view></router-view>

</template>

<style>
  
</style>