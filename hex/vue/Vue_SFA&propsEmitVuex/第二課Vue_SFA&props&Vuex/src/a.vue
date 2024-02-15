<script setup>
import { ref } from "vue"
import store from "./store.js"

let props =  defineProps({
  ans: Number
})
console.log(props.ans)//這樣才可以用props
//如果父組件傳進來的props是ajax來的  
//就必須使用watch檢查props是否有更新
//但在最後渲染畫面時有可能發生
//在watch時有資料  但是無法渲染在畫面上的情形
//此時就必須
/*

     這種可以 <div>{{imm.name?.first}}</div>
    這種也可以<div v-if="imm.name">{{imm.name.first}}</div>
      <!-- 這行印不出來<div>{{imm.name.first}}</div> -->


意思是要先檢查傷一層有沒有東西在進行渲染= = 
*/ 

let text = ref("qqq")

function func() {
  store.commit("updt", text.value)
  console.log(store.state.msg)
}

</script>

<template>
  <input type='text' v-model="text" @keydown.enter="func" />
</template>

