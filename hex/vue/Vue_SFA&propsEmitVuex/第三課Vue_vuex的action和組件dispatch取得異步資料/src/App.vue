<script setup>
/*
  要先安裝vuex和axios

  這節課重點是在sfa格式下 使用vuex引入外部異步資料 使用在子組件上

  先講整個城市如何運作

  首先組件onMounted之後，觸發store.dispatch("ajax函式名")
  dispatch會讓store裡的actios的ajax函式啟動
  啟動獲得外部資料後
  再給store.commit觸發mutations
  叫store的mutation的函式來更改資料

  此時store的資料更改完成
  一樣需要透過watch監聽目標資料是否更新 


  再來說程式構造

  會使用到新同學actions和dispatch
  actions是createStore裡的一個屬性，裡面放一個等待被dispatch觸發函式A
  這個函式A內容是取得異步資料，並commit 叫store觸發另一個mutation函式B

  那個被觸發的mutations函式B就是拿來改動store.state的資料的

  至於action裡面的函式A要怎麼被觸發
  就在某個組件的onMounted hooker裡發送
  也就是由組件告訴store要抓資料了
  這時store就會觸發action裡的函式Ａ
  函式A又會觸發mutations的函式B
  函式B就會乖乖地改資料

  好，現在store資料改好了
  組件怎麼知道資料改好了
  當然是靠watch
  跟props一樣＠＠
  好像只有emit不需watch 因為他是監聽 會有專人去觸發
  
  */

import store from "./vuex.js";
import { onMounted, watch, ref } from "vue";


let text = ref("");

let fromStoreText = ref("");

let fromStoreData = ref("")
onMounted(() => {
  store.dispatch("fetchData");
  fromStoreText.value = store.state.text;
  fromStoreData.value = store.state.data
  //console.log(store.state.data)
  //不能在這邊直接印資料  會有時候有有時候沒有 庫巴  媽的酷斃了幹
  //反正要復職要在watch裡面復職，onMounted是叫store 去ajax
});

watch(
  () => store.state.data,
  (newVal) => {
   let ans = newVal;
   fromStoreData.value = ans.data.results[0].name.first
  }
);

function sendToStore(e) {
  text.value = e.target.value;
  store.commit("updtText", text.value);
}


watch(
  () => store.state.text,
  (newVal) => {
    fromStoreText.value = newVal;
  }
);

</script>
<template>
  <input type="text" v-model="text" @change="sendToStore" />
  <hr />
  {{ fromStoreText }}
  <hr>
  {{fromStoreData}}
</template>
