<script setup>
  import {ref,onMounted,watch} from "vue";

  let text = ref("")
  let color = ref(null);
  let lst = ref([]);
  let lst2 = ['red','blue']
  let option = ref(lst2[0])

  function del(){
    text.value = ""
  }
  watch(()=>color.value,
    ()=>{console.log(color.value)})

    let hehe = ref(true)

</script>

<template>
  <input type="text" v-model="text">
  <div>{{text}}</div>
  <input @click="del" type="button" value="clear">
  <hr>
  red<input type="radio" v-model="color" value="red">
  <br>
  blue <input type="radio" v-model="color" value="blue">
  <br>
  <div :class="color">color</div>
  <hr>
  apple <input type="checkbox" value="apple" v-model="lst">
  <br>
  banana <input type="checkbox" value="banana" v-model="lst">
  <ul>
    <li v-for="item in lst">{{item}}</li>
  </ul>
  <input type="checkbox" v-model="hehe" >
  <div>{{hehe?'1':'2'}}</div>
  <select name="" id="" v-model="option">
    <option v-for="item in lst2" :value="item">{{item}}</option>
  </select>
  <div :class="option">啊啊</div>
</template>

<style scoped>
  .red{
    color:red
  }
  .blue{
    color:blue
  }

</style>