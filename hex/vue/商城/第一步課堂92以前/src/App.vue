<script setup>

import axios from "axios";

//取得在login ok時做好的cookie
//在每次向伺服器送請求時加上cookie
const newCookies = document.cookie.replace(/(?:(?:^|.*;\s*)newToken\s*=\s*([^;]*).*$)|^.*$/, '$1');
axios.defaults.headers.common.Authorization = newCookies;
</script>

<template>

<!--
  這邊的架構是
  app.vue只是放view的展示臺
  決定誰要出現的是一開始設置的"/"  以及  後續使用者的操作
  因為組件的出現決定於點擊與輸入
  一開始page為"/"的組件 dashboard 透過 view1出現
  dashboard只有負責將人導引至login page
  到login page後  login處理登入 如果登入成功 就導引至 index
  login也有使用localStorage存使用者設定
  在index只有處理log out功能
  以及log out之後導航至dashboard

  另外 再進入index.vue之前 router.beforeEach會進行檢查
  因為index是一個在routes裡面的物件具有meta:{requiredAuth:true}的組件
  因為有這項屬性 router可以透過程式碼進行檢查
  檢查行為在main.js
-->





  <router-view name="view1"></router-view>

</template>