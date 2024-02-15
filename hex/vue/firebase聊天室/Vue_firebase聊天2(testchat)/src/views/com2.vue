<script setup>
  import {msgRef,countRef} from "../firebase.config.js";
  import {push,get,set,onValue} from "firebase/database";
  import {ref,reactive,computed,onMounted} from "vue"

  let name = ref("");
  let content = ref("");
  let data = reactive({});

  

  async function add(){
    if (name.value&&content.value){
      let newMsgRef = push(msgRef)
      set(newMsgRef,{
        name:name.value,
        content:content.value,
        idx:await getIdx(name.value)
      })
    }
  }

  function getIdx(name){
    for (let key of Object.values(data)){
      if (key.name==name){
        return key.idx
      }
    }
    return getNewIdx()
  }
  async function getNewIdx(){
    let snapshot = await get(countRef);
    let ans = snapshot.val().number+20;
    await set(countRef,{number:ans});
    return ans
  }

  function whitchSide(nm){
    return nm==name.value?"me":"other"
  }
  onMounted(()=>{
    get(msgRef).then((snapshot)=>{
      Object.assign(data,snapshot.val())
    });
    onValue(msgRef,(snapshot)=>{
      Object.assign(data,snapshot.val())
    });
    
  })
  
  let reversedData = computed(()=>{
    return Object.values(data).reverse()
  })
 


</script>

<template>
  <div class="wrap">
    com2
    <div class="input-group flex-nowrap">
      <input
        v-model="name"
        type="text"
        class="name form-control"
        placeholder="Username"
        aria-label="Username"
        aria-describedby="addon-wrapping"
      />
    </div>
    <div class="input-group mb-3">
      <input
        v-model="content"
        type="text"
        class="form-control"
        placeholder="Recipient's username"
        aria-label="Recipient's username"
        aria-describedby="button-addon2"
      />
      <button
        @click="add"
        class="btn btn-outline-secondary"
        type="button"
        id="button-addon2"
      >
        Button
      </button>
    </div>
    <div class="main">
      <div v-for="key in reversedData" :class="['dialoage',whitchSide(key.name)]">
        <!-- <img :src="'https://picsum.photos/70?random='+key.idx"> -->
        <img :src="'https://picsum.photos/id/'+key.idx+'/70'"/>
        <div class="textwrap">{{key.name}} 說 : {{key.content}}</div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>