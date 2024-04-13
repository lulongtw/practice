<script setup>
  import {ref} from 'vue';

  let lst = ref(["雞", "豬", "牛", "狗", "熊"])

  let com1 = ref([]);

  let com2 = ref(false)
  let com3 = ref(false)
  let com4 = ref(false);

  let com5 = ref(true);
  let com6 = ref(null);
  let com7 = ref("nono");
  let com8 = ref([]);

  let com9 = ref("");
  let com10 = ref("")
</script>

<template>
  <div v-for="item in lst">
    <input type="checkbox" v-model="com1" :value="item">{{item}}
  </div>
  <div v-for="item in com1">{{item}}</div>

  <hr>

  <input type="checkbox" v-model="com2">
  <input type="checkbox" v-model="com3">
  <input type="checkbox" v-model="com4">
  {{[com2,com3,com4]}}

  <hr>

  <input type="checkbox" v-model="com5" true-value="q" false-value="j">
  {{com5}}

  <hr>

  <div v-for="item in lst">
    <input type="radio" v-model="com6" :value="item">{{item}}
  </div>
  {{com6}}

  <hr>

  <select v-model="com7" name="" id="">
    <option  disabled selected>nono</option>
    <option v-for="item in lst" :value="item">{{item}}</option>
  </select>
  {{com7}}

  <hr>

  <select v-model="com8" name="" id="" multiple>
    <option v-for="item in lst" :value="item">{{item}}</option>
  </select>
  {{com8}}

  <hr>

  <input type="text" v-model.lazy="com9">{{com9}}
  <input type="text" v-model.numver="com10">{{com10}}

</template>

<style>
  select{
    width:100px;
  }
</style>