<script setup>
import database from "../store/firebase.js";
import { ref, set, get, push } from "firebase/database";
import { ref as vueRef } from "vue";

let user = vueRef("");
let text = vueRef("");
let talkRef = ref(database, "talk");

async function send() {
  let newTalkRef = push(talkRef);
  set(newTalkRef, {
    user: user.value,
    text: text.value,
    time: getDate(),
    idx: await getIdx(user.value),
  });
}

async function getIdx(userName) {
  let snapshot = await get(talkRef);
  let data = snapshot.val();
  for (let key in data) {
    if (data[key].user == userName) {
      return data[key].idx;
    }
  }
  return await getNewIdx();
}

//沒事不要亂用.then  用await多好看
//下面那個註解起來是烙賽的
async function getNewIdx() {
  let countRef = ref(database, "count");
  let snapshot = await get(countRef);
  let count = snapshot.val();
  set(countRef, count + 9);
  return count;
}


//因為用了.then  找不到相同的user要執行await getNewIdx
//但無法放在.then迴圈裡面
// 只能放在.then{}外面
// 但是放在.then{}外面就會異步  抓到undefinded
// 所以想說getNewIdx不用await  直接.then但這樣野性不通

// async function getIdx(userName) {
//   get(talkRef)
//     .then((snapshot) => {
//       let data = snapshot.val();
//       for (let key in data) {
//         if (data[key].user == userName) {
//           return data[key].idx;
//         }
//       }
//     })
//     .then(async function () {
//       let countRef = ref(database, "count");
//       let ans = await get(countRef);
//       set(countRef, ans.val() + 9);
//       return ans.val();
//     });
// }

function getDate() {
  let date = new Date();
  return {
    hrs: date.getHours(),
    mins: date.getMinutes(),
    secs: date.getSeconds(),
  };
}
</script>

<template>
  <div class="input-group mb-3">
    <input
      v-model="user"
      type="text"
      class="form-control"
      placeholder=""
      aria-label="Example text with button addon"
      aria-describedby="button-addon1"
    />
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
      @click="send"
      class="btn btn-outline-secondary"
      type="button"
      id="button-addon2"
    >
      Button
    </button>
  </div>
</template>
