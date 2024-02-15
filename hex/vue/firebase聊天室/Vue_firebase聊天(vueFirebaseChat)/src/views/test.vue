<script setup>
import { ref, reactive, computed, onMounted } from "vue";
import { chatRoomRef, get, set, push, onValue } from "../fbconfig.js";

let who = ref("");
let newText = ref("");
let data = reactive({});
let img = ref(`https://picsum.photos/70?random=${3}`);
let count = ref(1);

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
    add();
  }
}

function add() {
  let newChatRoomRef = push(chatRoomRef);
  if (newText.value && who.value) {
    set(newChatRoomRef, {
      name: who.value,
      content: newText.value,
      idx: search(who.value),
      time: getTime(),
    });
    get(chatRoomRef).then((snapshot) => {
      Object.assign(data, snapshot.val());
      newText.value = "";
    });
  } else {
   // console.log("要輸入");
    return;
  }
}

function search(name) {
  console.log("???")
  for (let item of Object.values(data)) {
    console.log(item.name)
    if (name === item.name) {
      return item.idx;
    }
  }
  return count.value++;
}

onMounted(() => {
  window.addEventListener("keydown", handleKeyDown);
  get(chatRoomRef).then((snapshot) => {
    Object.assign(data, snapshot.val());
  });

  onValue(chatRoomRef, (snapshot) => {
    Object.assign(data, snapshot.val());
  });
});
function checkSide(name) {
  return name == who.value ? "me" : "other";
}


const reversedData = computed(() => {
  return Object.values(data).reverse();
});
</script>

<template>
  <div class="wrap">
    com1輸入姓名
    <input type="text" v-model="who" />
    {{ who }}對話框
    <div class="input-group mb-3" style="width: 300px">
      <input
        type="text"
        v-model="newText"
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
