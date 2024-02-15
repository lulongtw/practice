<script setup>
import { ref, reactive, computed, onMounted } from "vue";
import { chatRoomRef, get, set, push, onValue } from "../fbconfig.js";

let who2 = ref("");
let newText2 = ref("");
let data = ref({});
let count = ref(69);

function getTime() {
  let currentDate = new Date();
  let hour = currentDate.getHours();
  let minute = currentDate.getMinutes();
  let second = currentDate.getSeconds();
  return {
    hour:hour,
    minute:minute,
    second:second
  };
}


function handleKeyDown(e) {
  if (e.key === "Enter") {
   
      add()
    
  }
}
function add() {
  let newChatRoomRef = push(chatRoomRef);
  if (newText2.value && who2.value) {
    set(newChatRoomRef, {
      name: who2.value,
      content: newText2.value,
      idx: search(who2.value),
      time: getTime(),
    });

      newText2.value = "";

  } else {
    //console.log(newText.value, who.value);
    console.log("要輸入");
  }
}

function search(name) {
  for (let item of Object.values(data.value)) {
    if (name === item.name) {
      return item.idx;
    }
  }
  return count.value++;
}

onMounted(() => {
  window.addEventListener("keydown", handleKeyDown);
  get(chatRoomRef).then((snapshot) => {
    data.value = snapshot.val();
  });

  onValue(chatRoomRef, (snapshot) => {
    data.value = snapshot.val();
  });


});
function checkSide(name) {
  return name == who2.value ? "me" : "other";
}



const reversedData = computed(() => {
  return Object.values(data.value).reverse();
});
</script>

<template>
  <div class="wrap">
    com2輸入姓名
    <input type="text" v-model="who2" />
    {{ who2 }}對話框
    <div class="input-group mb-3" style="width: 300px">
      <input
        type="text"
        v-model="newText2"
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
    <div class="content">
      <div class="column" v-for="(item, key) in reversedData">
        <div :class="['msg', checkSide(item.name)]">
          <img :src="'https://picsum.photos/70?random=' + item.idx" />
          <div class="contentwrap">
            <div class="text">{{item.name}}說:{{item.content}}</div>
            <div class="time">at {{item.time.hour}}-{{item.time.minute}}-{{item.time.second}}</div>            
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
