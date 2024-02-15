<script setup>
import store from '../store.js';
import { watch, ref } from 'vue';

let data = ref(store.state.data)

watch(() => store.state.data, (newValue) => {
  data.value = newValue
})

function checkSide(name){

 return name===data.value[0].name?"me":"other"
}


</script>

<template>
  <div class="cntnwrap">
    <div v-for="obj in data" :class="['text',checkSide(obj.name)]">
      <img :src="'https://picsum.photos/id/' + obj.idx + '/70'">
      <div class="textwrap">
        <div>{{ obj.name }} 說: {{ obj.text }}</div>
        <!-- 不能寫data[obj].name 
        因為在v-for裡面 obj已經是物件了 而不是序列的索引
        因為v-for="(value,key) in data" 懂?? -->
        <div>at{{obj.time.hr}}-{{obj.time.min}}-{{obj.time.sec}}</div>
      </div>
    </div>
  </div>


</template>

<style scoped></style>