<script setup>
import { get, set ,push, onValue} from "firebase/database";
import { testRef,countRef } from "../firebase.config.js";
import {onMounted, reactive,ref,computed} from "vue"

async function 給你看看() {
  //這函式式包裝用  這兩個get-console要拿出去外面用

  //await會等get再返回  雖然可以執行蛋會跳警告  因為沒有好兄弟async
  let snapshot = await get(testRef);
  console.log(snapshot.val());

  //.then會自動等
  get(testRef).then((snapshot) => {
    console.log(snapshot.val());
  });
}


function getTime(){
  let date = new Date();
  let hr = date.getHours();
  let min = date.getMinutes();
  let sec = date.getSeconds();
  return {hr:hr,min:min,sec:sec}
}

let name = ref("b")
let text = ref("雞掰")
let data = reactive({})

async function add(){
  if (name.value&&text.value){
    let newtestRef = push(testRef);
    set(newtestRef,{
      name:name.value,
      text:text.value,
      hr:getTime().hr,
      min:getTime().min,
      sec:getTime().sec,
      idx:await getIdx(name.value)
    })
  }
}
function getIdx(name){
  for (let key of Object.values(data)){
    if (name==key.name){
      return key.idx
    }
  }
  return getNewIdx()
}
async function getNewIdx(){
  let snapshot = await get(countRef);
  let ans = snapshot.val() +9;
  await set(countRef,ans);
  return ans
}
onMounted(()=>{
  get(testRef).then((snapshot)=>{
    Object.assign(data,snapshot.val());
  });
  onValue(testRef,(snapshot)=>{
    Object.assign(data,snapshot.val())
  })
});

let reversedData = computed(()=>{
  return Object.values(data).reverse();
})

function checkSide(keyname){
  return keyname==name.value?"me":"other"
}

</script>



<template>
  com2
  <div class="wrap">
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

    <div class="cntnwrap">
      <div v-for="key in reversedData" :class="['text',checkSide(key.name)]">
        <img :src="'https://picsum.photos/id/'+key.idx+'/70'">
        <div class="textwrap">
          <div>{{key.name}} 說: {{key.text}}</div>
          <div>at-{{key.hr}}時{{key.min}}分{{key.sec}}秒</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
