<script setup>
  import {ref,onMounted,watch} from "vue";
  import store from "@/store/store.js";
  
  let user = ref("");
  let speak = ref("");
  let emits = defineEmits(['sendInput'])
  watch(()=>user.value,
    ()=>{
      emits('sendInput',user.value)
    }
  )

  async function send(){
    let toSend = {
      name:user.value,
      cntn:speak.value,
      count:await getIdx(user.value)
    }
    store.dispatch("setData",toSend);

  }

  async function getIdx(user){
    let data = store.state.data;
    let rightItem =  Object.values(data).find((item)=>{
      if (item.name==user){
        return item
      }
    });
    return (rightItem?rightItem.count:await getNewIdx())
  }

  async function getNewIdx(){
    await store.dispatch('setNewCount');
    await store.dispatch('getCount');
    return store.state.count
  }
</script>

<template>
  <div class="InputComWrap">
    <div class="input-group mb-3">
  <input v-model="user" type="text" class="form-control" placeholder="Recipient's username" aria-label="Recipient's username" aria-describedby="button-addon2">
</div>
<div class="input-group mb-3">
  <input v-model="speak" type="text" class="form-control" placeholder="Recipient's username" aria-label="Recipient's username" aria-describedby="button-addon2">
  <button @click="send()" class="btn btn-outline-secondary" type="button" id="button-addon2">Button</button>
</div>
  </div>

</template>

<style scoped>
  @import "@/assets/InputCom.css"
</style>