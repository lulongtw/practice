<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();
/*
useRouter 和 useRoute 不一樣

useRoute是組件取得router實例的方法
可取用當前router的params的id 也就是當前的路由
可透過query取用傳入的參數

useRouter是取代ROuterLink :to="" 的一個方法
可以直接觸發router轉換當前路由
方法有 push , back,  forward , go ,replace

push()
參數傳入  path
或是
routes的name，跳轉的path，傳入的參數
相當於<RouterLink to='xxx'>

back()
回上ㄧ頁

forward()
回下一頁

go(x)
往前x頁

replace(x)
由目前的頁面跳轉到x頁，目前頁面不會留在紀錄中
比方說順序是
1,2,replace 3 ,4,5
那麼2不會留在紀錄裡面 也就是說不會被back和forward追蹤到



*/

function fun1(n) {
  
  router.push({name:'com',params:{id:n},query: { idx: n }});
}


</script>

<template>

  <div v-for="item in 7" @click="fun1(item)">com{{item}}</div>
  <!-- <div @click="fun1(1)">com1</div>
  <div @click="fun1(2)">com2</div>
  <div @click="fun1(3)">com3</div>
  <div @click="fun1(4)">com4</div>
  <div @click="fun1(5)">com5</div> -->
  <div @click="router.back()">回上一頁</div>
  <div @click="router.forward()">回下一頁</div>
  <div @click="router.go(2)">前進兩頁</div>
  <div @click="router.replace({
    name:'com',params:{id:3},query:{idx:3}
  })">replace3</div>
  <hr>
  <RouterView name="view1"></RouterView>
</template>
