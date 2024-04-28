<script setup>
  import {ref,watch,computed,onMounted,inject,provide} from "vue";
  import store from "@/store/store.js";
  import {useRouter} from "vue-router";
  import {Modal} from "bootstrap";
  import {showModal,hideModal,getData} from "@/functions.js";
  import * as yup from "yup"

  
</script>

<template>
  <div class="cartLst">
    qqq
  </div>

</template>
<style scoped>
  .cartLst{
    width:150px;
    position:absolute;
    top:50px;
    right:0px;
    padding:10px;
    border:1px solid black;
    background-color: rgba(155, 155, 155, 0.602);
  }
</style>