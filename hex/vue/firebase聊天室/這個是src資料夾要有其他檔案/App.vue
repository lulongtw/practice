<script setup>
  import InputCom from "@/components/InputCom.vue";
  import ContentCom from "@/components/ContentCom.vue";
  import {onMounted,ref} from "vue";
  import store from "@/store/store.js"
  // console.log(store.state.count)
  onMounted(async()=>{
    store.dispatch("onValueData");
    store.dispatch("onValueCount")
    await store.dispatch('getData');
    await store.dispatch('getCount')
    
  });
  let currentUser = ref("")
  function sentToContent(newVal){
    currentUser.value = newVal;
  }
</script>
<template>
  <div class="wrap">
    <InputCom @sendInput="sentToContent"></InputCom>
  <ContentCom :fromDad="currentUser"></ContentCom>
  </div>


</template>
<style>
  .wrap{
    width:min(80%,900px);
    margin:30px auto;
  }
</style>