<script setup>
  import {ref,onMounted,watch,computed} from 'vue';
  import store from "@/store.js";


  let data = ref(store.state.data);
  let currentContent = ref("");
  let currentName = ref("");
  let nameHolder = ref('誰');
  let contentHolder = ref("說什麼");

  // let revData = computed(()=>{
  //   let newData = {};
  //   Object.keys(data.value).reverse().forEach(item=>{
  //     newData[item] = data.value[item]
  //   })
  //   return newData
  // })
  
  watch(()=>store.state.data,
    (newVal)=>{
      data.value = newVal;
    }
  )

  onMounted(async ()=>{
    store.dispatch("onValueData");
    store.dispatch("onValueCount");
    await store.dispatch('addViewer')

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
    let count = store.state.count +160;
    await store.dispatch('setNewCount',count);
    return count
  }

  async function send(){
    if (!currentName.value){
      nameHolder.value = "要說你是誰";}
    else if (!currentContent.value){
      contentHolder.value = "你沒說你想說什麼"
    }
    else{
      nameHolder.value = "誰";
      contentHolder.value = "說什麼"
      let time = new Date();
      store.dispatch('sent',{
      'name':currentName.value,
      'cnt':currentContent.value,
      'time':`${time.getMonth()+1}-${time.getDate()}-${time.getHours()}`,
      'count':await getCount()
    })
      currentContent.value = ""
    }
    
  }
</script>
<template>
  <div class="wrap">
    <div class="cntWrap">
  <div :style="{backgroundColor: `rgb(${item.count%255}, 0, 0, 0.15)`}" 
    :class="['cnt',item.name==currentName?'now':'']" v-for="item in data">
  
    <div><span>{{item.name}}</span> 說:<div>{{item.cnt}}</div></div>
    <div class="date">{{item.time}}</div>
  </div>
</div>
    <div class="input-group mb-3">
      
  <textarea  @keyup.enter="send" v-model="currentName" type="text" class="form-control" :placeholder="nameHolder" aria-label="Example text with button addon" aria-describedby="button-addon1"></textarea>
</div>

<div class="input-group mb-3">
  <textarea v-model="currentContent" type="text" class="form-control" :placeholder="contentHolder" aria-label="Recipient's username" aria-describedby="button-addon2"></textarea>
  <button  @click="send" class="btn btn-outline-secondary" type="button" id="button-addon2">send</button>
</div>


  </div>

</template>
<style scoped>
  .wrap{
    width:min(900px,80%);
    margin:20px auto;
  }
  .cntWrap{
    margin-bottom: 20px;
    padding:15px;
    border:1px solid rgb(187, 187, 187);
    border-radius: 10px;
    position: relative;
    display: flex;
    flex-wrap: wrap;

  }

  .cnt{
    padding:10px;
    margin-bottom:20px;
    gap:30px;
    line-height:27px;
    white-space:pre-wrap;
    border-radius:10px;
    width:90%;

  }
  span{
    font-weight: 800;
  }
  .now{
    position: relative;
    left:calc(10%);
  }
  .date{
    text-align: end;
  }
</style>