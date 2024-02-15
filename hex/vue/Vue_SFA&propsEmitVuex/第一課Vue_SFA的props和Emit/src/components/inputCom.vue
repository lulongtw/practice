<script setup>
import { ref, watch } from "vue";

let infofromDad = ref("等待dad props")
//建立props物件接受props
let props = defineProps({
  fromDad: String//子組件使用props.fromDad使用父組件傳來的值
});
//props需要watch監聽父組件的值是否變動
watch(()=>props.fromDad,
      ()=>{infofromDad.value = props.fromDad})
      //  也可這樣寫
      // (newVal)=>{infofromDad.value = newVal})

let text = ref("給爸爸的話")
//要用emit要先建立emit案號
let emit = defineEmits(["sendToDad"])

function toDad(){
  //發送emit事件讓父組件監聽到
  emit("sendToDad",text.value)//注意要有.value  不然會瘋狂連動 如果一定要沒有.value的話 text一開始就不能ref()

}
</script>
<template>
  {{ infofromDad }}
  <br>
  <input type="text" v-model="text">
  <button @click="toDad">按我</button>
</template>