<script setup>
import {RouterLink,RouterView} from "vue-router";
//引進這兩個標籤   
//routerlink決定誰要出線  用to決定
//routerview決定要出現在哪裡  用name決定
//也可以使用:to="{name:'名字'}"導覽
</script>
<template>
  <RouterLink :to="{name:'comOne'}">tocom1</RouterLink>
  <RouterLink to="/com2">tocom2</RouterLink>
  <hr>
  <div class="box">
    <RouterView name="view1"></RouterView>
  </div>

  <div>pika pika</div>
  <div class="box">
    <RouterView name='view2' v-slot="{Component}">
      <KeepAlive>
        <component :is="Component"></component>
      </KeepAlive>
    </RouterView>
  </div>


</template>
<style scoped>
  .box{
    border:1px solid black
  }
</style>