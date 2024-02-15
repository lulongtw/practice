<script setup>
  import store from "../store/vuex.js";
  import {ref} from "vue";
  let user = ref("");
  let text = ref("");
  function send(){
    store.commit("updtData",{
      user:user.value,
      text:text.value,
      idx:getIdx(user.value)
    });
  }
  function getIdx(userName){
    let data = store.state.data;
    for (let item of data){
      if (item.user==userName){
        return item.idx
      }
    }
    return getNewIdx()
  }
  function getNewIdx(){
    let count = store.state.count;
    store.commit("updtCount",count+9);
    return count
  }

</script>

<template>

  <div class="input-group mb-3">
     <input v-model="user" type="text" class="form-control" placeholder="" aria-label="Example text with button addon" aria-describedby="button-addon1">
  </div>

  <div class="input-group mb-3">
    <input v-model="text" type="text" class="form-control" placeholder="Recipient's username" aria-label="Recipient's username" aria-describedby="button-addon2">
    <button @click="send" class="btn btn-outline-secondary" type="button" id="button-addon2">Button</button>
  </div>
  
</template>