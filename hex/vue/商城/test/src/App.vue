<script setup>
  import Loading from 'vue3-loading-overlay';
  // Import stylesheet
  import 'vue3-loading-overlay/dist/vue3-loading-overlay.css';
  import {computed,watch,ref} from "vue";

  import store from "@/store/vuex.js";

  let hintList = ref([]);
  
  let isLoading = computed(()=>{
    return store.state.isLoadingModule.isLoading
  })

  watch(()=>store.state.AllHints,
    ()=>{
      hintList.value = store.state.AllHints;
      //在watch裡面 用setTimteOut處理 watch的目標
      //結果會跟笨蛋想的不一樣
      //watch一樣會觀測到splice的結果 就會再次引發splice
      //所以splice行為要跟push型為放一起 也就是vuex內
      // setTimeout(()=>{
      //   store.commit("mutations_deleteHints")
      // },3000)
    },{deep:true}
  )

</script>

<template>
  <div class="hints">
    <div  class="square" v-for="(item,idx) in hintList">
      {{item}}
    </div>
  </div>

  <div>
    <loading :active="isLoading"></loading>
    <router-view></router-view>
  </div>

</template>

<style scoped>
  .hints{
    z-index:99999;
    position:fixed;
    top:30px;right:30px;
  }
  .square{
    padding:20px;
    background-color: rgb(248, 146, 146);
    margin-bottom:10px;
    border-radius: 10px;
    opacity: 0.95;
  }

</style>
