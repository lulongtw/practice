<script setup>
  import {ref,watch,computed,onMounted,onActivated,inject,provide} from "vue";
  import store from "@/store/store.js";
  import {useRouter} from "vue-router";
  import {Modal} from "bootstrap";
  import {showModal,hideModal,getData} from "@/functions.js";
  import {Form,Field,ErrorMessage} from "vee-validate";
  import * as yup from "yup";

  import router from "@/router";
 
 
  onMounted(()=>{
    setTimeout(()=>{
      router.push("/checkOut/useCouponPage")
    },0)
  })

</script>

<template>
  <div class="wrap">
    <div class="title">肥狗旺旺結帳</div>
    <div class="stepWrap">
      <div @click="go" class="step">1.套用優惠券</div>
      <div class="step">2.建立買家訂單</div>
      <div class="step">3.付錢</div>
    </div>
    <RouterView></RouterView>

    <!-- <div class="inputWrap">
      <ValiForm></ValiForm>
    </div> -->
  </div>
</template>
<style scoped>
  *{
    text-align:center;
  }
  .title{
    font-size:20px;
    color:grey;
  }
  .stepWrap{
    display:flex;
    gap:10px;
    justify-content: center;
  }
  .step{
    background-color: green;
    padding:5px 15px;
  }

  


  

</style>