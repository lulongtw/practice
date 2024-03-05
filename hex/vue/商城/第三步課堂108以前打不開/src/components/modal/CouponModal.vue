<script setup>
import axios from "axios";
import {noCatch} from "@/assets/functions";
import {ref} from "vue";


let data = ref({})
let headAPI = import.meta.env.VITE_headAPI;
let myAPI = import.meta.env.VITE_myAPI;
let url = `${headAPI}/api${myAPI}/admin/coupon`;
let checkBox = ref(false)

function addNewCoupon(){
  data.value.is_enabled = checkBox.value
  console.log(data.value)
  // noCatch(axios.post(url)
  //     .then(res=>{  

  //     })
  //   )
}
</script>

<template>

<div class="modal fade" id="CouponModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="staticBackdropLabel">Modal title</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        
  <div class="couponWrap">

<div class="title">
  <input v-model="data.title" type="text">
</div>

<div class="percent">
  <input v-model="data.percent" type="text">
</div>

<div class="due">
  <input v-model="data.due_date" type="text">
</div>

<div class="code">
  <input v-model="data.code" type="text">
</div>

<div class="couponenabled">
  <input type="checkbox" v-model="checkBox" :true-value="1" :false-value="0" >
</div>

</div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button @click="addNewCoupon()" type="button" class="btn btn-primary">Understood</button>
      </div>
    </div>
  </div>
</div>

</template>

<style>




</style>