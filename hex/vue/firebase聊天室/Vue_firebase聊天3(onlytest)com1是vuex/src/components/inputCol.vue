<script setup>
  import {ref,onMounted} from "vue";
  import store from "../store.js"

  let name=ref("");
  let text=ref("");


 function add(){
    if (name.value&&text.value){
      let newData = {
        name:name.value,
        text:text.value,
        idx:getIdx(name.value),
        time:getTime()
      }
      store.commit("updt",newData)
    }

    text.value=""
  }


function getIdx(nm){
  let data = store.state.data
  for (let i=0;i<data.length;i++){
    if (data[i].name==nm){
      return data[i].idx
    }
  }
  return getNewIdx()
}

function getNewIdx(){
  let ans = store.state.count;
  ans+=9;
  store.commit("updtCount",ans);
  return ans
}

function getTime(){
  let time = new Date();
  let hr = time.getHours();
  let min = time.getMinutes();
  let sec = time.getSeconds();
  return {hr:hr,min:min,sec:sec}
}

onMounted(()=>{
  window.onkeydown = (e)=>{
  if (e.key=="Enter"){
    add()
  }
}
})

</script>

<template>
      <div class="col-auto">
      <label class="visually-hidden" for="autoSizingInputGroup">Username</label>
      <div class="input-group">
        <div class="input-group-text">@</div>
        <input
          v-model="name"
          type="text"
          class="form-control"
          id="autoSizingInputGroup"
          placeholder="Username"
        />
      </div>
    </div>

    <div class="input-group mb-3">
      <input
        v-model="text"
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
</template>

<style scoped></style>