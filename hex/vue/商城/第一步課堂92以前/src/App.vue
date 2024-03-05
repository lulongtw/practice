<script setup>
  import axios from "axios"
  //取得在login ok時做好的cookie
//在每次向伺服器送請求時加上cookie
  let cookies = document.cookie;
  cookies = cookies.split("; ");
  //console.log(cookies)
  cookies = cookies.map(item=>{
    return item.split("=")
  })
  
  let beforeShootingToken
  cookies.forEach(item=>{
    if (item[0]=="beforeShootingToken"){
      beforeShootingToken = item[1];
    }
  })
  axios.defaults.headers.common.authorization = beforeShootingToken
</script>

  <!--
  這邊架構是
  開始畫面是login 登入成功進到product
  producy是dashboard的routes children
  看到product需驗證登入
  看到dashboard哺需要
  

  進入index.vue之前 router.beforeEach會進行檢查
  因為index是一個在routes裡面的物件具有meta:{requiredAuth:true}的組件
  因為有這項屬性 router可以透過程式碼進行檢查
  檢查行為在main.js
-->

<template>
  <div class="AppWrap">
    <router-view></router-view>
  </div>

</template>
