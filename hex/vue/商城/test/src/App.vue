<script setup>
  import {ref,provide,watch} from "vue";
  import axios from "axios";
  //取得在login ok時做好的cookie
//在每次向伺服器送請求時加上cookie
  import store from "@/store/vuex.js";
  import Loading from 'vue-loading-overlay';
  import 'vue-loading-overlay/dist/css/index.css';

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

  let data = ref([]);
  provide("addToStack",(item)=>{
    data.value.push(item)
    setTimeout(()=>{
      data.value.splice(0,1)
    },3000)
  });
  let checkLoading = ref(store.state.isLoading)

  watch(data.value,
    ()=>{
      //不能watch data.value控制setTimeout
      //因為splice時也會觸發watch 會很邏輯 = = 
      //   setTimeout(()=>{
      //   if (data.value.length>0){
      //     console.log(data.value.length)
      //     data.value.splice(0,1);
      //   }
      // },5000)
    
    }
  )

  watch(()=>store.state.isLoading,
    ()=>{
      console.log(store.state.isLoading)
      checkLoading.value = store.state.isLoading
    }
 
  )
  function delThis(idx){
    data.value.splice(idx,1)
  }
  


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
    <loading v-model:active="checkLoading"/>
    <div class="squareWrap">
      <div class="square" v-for="(item,idx) in data" @click="delThis(idx)">
        {{item}}
      </div>
    </div>
    <router-view></router-view>
  </div>

</template>

<style scoped>
  .squareWrap{
    position:fixed;
    top:50px;right:50px;
    z-index:9999999
  }
  .square{
    margin-top: 10px;
    padding:30px;
    background-color: pink;

  }
</style>
