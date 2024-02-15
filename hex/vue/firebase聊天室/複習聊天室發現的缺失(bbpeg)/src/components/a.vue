<script setup>
  import database from '../store/firebase.js';
  import {ref,push,set,get,onValue} from "firebase/database";
  import {ref as vueRef,onMounted, useTransitionState} from "vue";

  let talkRef = ref(database,"talk");
  let user = vueRef("");
  let text = vueRef("")


  onMounted(async()=>{
    // get(talkRef).then((snapshot)=>{
    //   console.log(snapshot.val())
    // })

    // let newTalkRef = push(talkRef);
    // set(newTalkRef,{
    //   user:1
    // })

    // onValue(talkRef,(snapshot)=>{
    //   console.log(snapshot.val())
    // })
  })

  async function send(){
    let newTalkRef = push(talkRef);
    let newData = {
      user:user.value,
      text:text.value,
      idx:await getIdx(user.value)
    }
    console.log(newData)
    set(newTalkRef,newData)

    
  }
  async function getIdx(userName){
    let snapshot = await get(talkRef);
    let data = snapshot.val();
    for (let key in data){
      if (data[key].user==userName){
        return data[key].idx
      }
    }
    return await getNewIdx()
  }
  async function getNewIdx(){
    let countRef = ref(database,"count");
    let snapshot = await get(countRef);
    set(countRef,snapshot.val()+9);
    console.log(snapshot.val())
    return snapshot.val()
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