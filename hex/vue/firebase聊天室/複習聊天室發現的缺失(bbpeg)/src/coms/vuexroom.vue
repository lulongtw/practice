<script setup>
  import store from "../store/vuex.js";
  import {watch,ref} from "vue";

  //要watch的值必須一開始就給復職
  //如果這段式data = ref([])
  //那麼watch會沒屁用
  let data = ref(store.state.data);
  
  watch(()=>store.state.data,
        ()=>data.value = store.state.data
  )
  function which(userName){
    return store.state.data[0].user==userName?"":"other"
  }

</script>

<template>
  <div class="room">

    <div v-for="item in data" :class="['chat',which(item.user)]">
      <div class="text">
        {{item.user}} 說: {{item.text}}
      </div>
      <div class="pic">
        <img :src="'https://picsum.photos/id/'+item.idx+'/50'" alt="">
      </div>
    </div>

  </div>
</template>