<script setup>
  import axios from 'axios';
import {ref,onMounted,inject,watch} from "vue";
import {headAPI,myAPI,getData,getDot} from "@/functions.js";
import {useRoute} from "vue-router";
import {Form,Field,ErrorMessage} from "vee-validate";

import * as yup from "yup";

let route = useRoute();
let data = ref("");
let toggleLoading = inject('toggleLoading');
let showStatus = inject('showStatus');
let id
onMounted(async()=>{
  id = route.params.id;
  await getSinglePayData()
})

async function getSinglePayData(){
  toggleLoading()
    let url = `${headAPI}/api${myAPI}/order/${id}`;
    let res = await(getData(url,'get'));
    if (res.data.success){
      data.value = res.data.order;
      console.log(data.value)
    }
    toggleLoading()
}
async function gogo(){
  toggleLoading()
  let url = `${headAPI}/api${myAPI}/pay/${id}`;
  let method = 'post';
  let res = await getData(url,method);
  if (res.data.success){
    let timeStamp = new Date().getTime()
    showStatus({content:res.data.message,stamp:timeStamp})

  }
  toggleLoading()
  await getSinglePayData()
}
</script>

<template>
  <table>
    <thead>
      <tr>
        <th>品茗</th>
        <th>數量</th>
        <th>單價</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(item,idx) in data.products">
        <td>{{item.product.title}}</td>
        <td>{{item.qty}}{{item.product.unit}}</td>
        <td>{{item.product.price}}</td>
      </tr>

        <tr class="qq">
        <td></td>
        <td></td>
        <td>總價{{data.total}}</td>
      </tr>



    </tbody>
  </table>
  
  <table v-if="data.user">
    <tr>
      <td>email</td>
      <td>{{data.user.email}}</td>
    </tr>
    <tr>
      <td>姓名</td>
      <td>{{data.user.name}}{{data.user.userName}}</td>
    </tr>
    <tr>
      <td>收件人電話</td>
      <td>{{data.user.tel}}</td>
    </tr>
    <tr>
      <td>收件地址</td>
      <td>{{data.user.address}}</td>
    </tr>
    <tr>
      <td>付款狀態</td>
      <td>{{data.is_paid?'服完了':'notok'}}</td>
    </tr>
  </table>
  <button @click="gogo" v-if="!data.is_paid">按我付款</button>

</template>
<style>
  .qq{
    text-align: right;
  }
  table{
    width:min(80%,600px);
    margin:30px auto;

  }
  tr{
    border-top:1px solid gray;
  }
  td,th{
    padding:20px 10px;
  }
  th{
    text-align: center;
  }
  th:first-of-type{
    text-align: left;
  }
  table:nth-of-type(1)>tbody td:first-of-type{
    width:50%;

  }
  table:nth-of-type(1)>tbody td:nth-of-type(2){
    text-align: center;
    width:20%;

  }
  table:nth-of-type(1)>tbody td:nth-of-type(3){
    width:20%;
    text-align: center;
  }
  table:nth-of-type(2) td:first-of-type{
    width:30%;
  }
</style>