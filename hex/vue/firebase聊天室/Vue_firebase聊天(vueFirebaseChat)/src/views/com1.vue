<script setup>
import { ref, reactive, computed, onMounted } from "vue";
import { chatRoomRef, get, set, push, onValue } from "../fbconfig.js";

/*
com1跟com2長的一樣= =  其實router跟多人聊天室好像沒啥太大關係
只是com1 com2可以多個keepalive設定而已
還有count來連動隨機頭像的號碼，但是可以透過直接設在資料庫裡面處理，就不用兩邊都射count了

先把router和firebase處理好  再來搞view組件

view組件
首先把組件的畫面都打樣板出來
就是做對話css 重點是要怎麼決定圖在左邊還是是右邊
用bind來引入函式決定


然後是add函式
資料庫寫入web端輸入的資料  這很簡單
但我無法處理當沒有輸入名字訊息時 會有功能是提醒使用者要輸入名字和訊息
蛋兩個組件會同時監聽keydown enter 即使目前routes不是自己  也會監聽到= = 到底
因為當我輸入完訊息送出後  訊息欄就會變空白  然後我切換到另一個view組件繼續聊天
當我按下enter時 那個沒在用的view組件也會同時監聽到enter  因為該訊息欄是空白 就會console出沒輸入訊息
我是想在執行keydown之前 加個if 如果當前path==目前組件的話  才執行  但我找不到當前path怎麼用


然後就是onMount部分，
在有關使用遠端資料刷新頁面，
一定要把相關程式放在onMount 
不然鐵定抓不到
例如get,set,onvalue等等


Object.values
取得響應式狀態的js使用狀態@@
看下面search部分  無法直接使用data.item
我也不知道為啥我也不知道為啥我也不知道為啥我也不知道為啥我也不知道為啥我也不知道為啥我也不知道為啥


還有reactive
com2的data適用ref() com1用reactive()
差別是reactive是監聽內部
所以如果直接整體 data = snapshot.val()
會當作沒有發生
要Object.assign(data,snapshot.val())才會監聽到
而com2ref有用
我也不知道為什麼= =我也不知道為什麼= =我也不知道為什麼= =我也不知道為什麼= =我也不知道為什麼= =我也不知道為什麼= =

*/ 

let who = ref("");
let newText = ref("");
let data = reactive({});
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
      add()
    
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
    newText.value = "";
  } else {
      console.log("要輸入");
    
  }
}

function search(name) {
  for (let item of Object.values(data)) {
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
