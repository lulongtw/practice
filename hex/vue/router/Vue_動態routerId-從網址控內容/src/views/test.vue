<script setup>
import { useRoute } from 'vue-router';
import { ref, watch } from "vue"

// 使用 useRoute 获取当前路由实例
const route = useRoute();

// 你可以直接访问 route.params 来获取路由参数
//console.log(route.params.id);
let id = route.params.id;
let text = ref("dsad")
let url = `https://randomuser.me/api/?page=3&results=1&seed=${text.value}`;
let data = ref([])
let id1 = ref("")

fetch(url)
  .then((res) => res.json())
  .then((res1) => {
    data.value = res1.results
    console.log(data.value)
  })
  .catch(res => {
    console.log("shit")
  })

watch(() => id1.value,
  () => {
     url = `https://randomuser.me/api/?page=3&results=1&seed=${id1.value}`;
    fetch(url)
      .then((res) => res.json())
      .then((res1) => {
        data.value = res1.results
        console.log(data.value)
      })
      .catch(res => {
        console.log("shit")
      })
  }
)


</script>

<template>
  <input type="text" v-model="text" @change="id1 = text">
  <div v-for="item in data">
    {{ item.name.first }}
    <img :src="item.picture.medium" alt="">
  </div>
</template>
