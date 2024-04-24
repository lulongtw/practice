<script setup>
  import {watch,ref} from "vue";
  import store from "@/store/store.js";
  import Loading from 'vue-loading-overlay';
  import 'vue-loading-overlay/dist/css/index.css';

  watch(()=>store.state.isLoading,
    (newVal)=>{
      isLoading.value = newVal
    }
  )
  let isLoading = ref(false)

</script>

<template>
  <div>
    <loading v-model:active="isLoading"/>
    <router-view></router-view>
  </div>


</template>
<style scoped>


</style>