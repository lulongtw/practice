<script setup>
  import {ref,onMounted,watch,computed} from 'vue';
  import store from "@/store.js";


  let data = ref(store.state.data);
  let currentContent = ref("");
  let currentName = ref("");
  let revData = computed(()=>{
    let newData = {};
    Object.keys(data.value).reverse().forEach(item=>{
      newData[item] = data.value[item]
    })
    return newData
  })
  
  watch(()=>store.state.data,
    (newVal)=>{
      data.value = newVal;
    }
  )

  onMounted(()=>{
    store.dispatch("onValueData");
    store.dispatch("onValueCount")
  })
    
  function check(name){
    return name==currentName.value?true:false
  }

  async function getCount(){
    let lst = Object.values(data.value);
    let count
    if (lst.some(item=>{
      count = item.count
      return item.name==currentName.value
    })){
      return count 
    }
    return await getNewCount()
  }
  async function getNewCount(){
    let count = store.state.count +9;
    await store.dispatch('setNewCount',count);
    return count
  }

  async function send(){
    store.dispatch('sent',{
      'name':currentName.value,
      'cnt':currentContent.value,
      'count':await getCount()
    })
  }
</script>
<template>
  <div class="wrap">
    <div class="input-group mb-3">
  
  <input v-model="currentName" type="text" class="form-control" placeholder="誰" aria-label="Example text with button addon" aria-describedby="button-addon1">
</div>

<div class="input-group mb-3">
  <input v-model="currentContent" type="text" class="form-control" placeholder="說什麼" aria-label="Recipient's username" aria-describedby="button-addon2">
  <button @click="send" class="btn btn-outline-secondary" type="button" id="button-addon2">send</button>
</div>

<div class="cntWrap">
  <div :class="['cnt',{'other':check(item.name)}]" v-for="item in revData">
    <img :src="`https://picsum.photos/id/${item.count}/60/60`" alt="">
    <div>{{item.name}} 說: {{item.cnt}}</div>
  </div>
</div>
  </div>

</template>
<style scoped>
  .wrap{
    width:min(900px,80%);
    margin:20px auto;
  }
  .cntWrap{
    margin-top: 20px;
    padding:10px;
    border:1px solid rgb(187, 187, 187);
    border-radius: 10px;
  }
  .cnt{
    padding:10px;
    border-bottom:1px solid  rgb(187, 187, 187);
    margin-bottom:20px;
    display:flex;
    align-items: center;
    justify-content: space-between;
    gap:30px;
  }
  .other{
    flex-direction: row-reverse;
  }
</style>