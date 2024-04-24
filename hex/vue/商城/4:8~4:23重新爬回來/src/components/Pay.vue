 <script setup>
import axios from 'axios';
import {ref,onMounted,inject,watch} from "vue";
import {headAPI,myAPI,getData,getDot} from "@/functions.js";
import {useRouter} from "vue-router";
import {Form,Field,ErrorMessage} from "vee-validate";
import * as yup from "yup";
import Pages from './Pages.vue';

let data = ref({});
let toggleLoading = inject('toggleLoading');
let showStatus = inject('showStatus');
let pagination = ref({})

onMounted(async()=>{
  await getOrdersData()
})

async function getOrdersData(){
  toggleLoading()
  let url = `${headAPI}/api${myAPI}/orders?page=1`;
  let method = 'get';

  let res = await getData(url,method);
  console.log(res)
  if (res.data.success){
    data.value = res.data.orders;
    pagination.value = res.data.pagination;
  }
  toggleLoading()
}

async function checkOut(item){  
  toggleLoading()
  let url = `${headAPI}/api${myAPI}/pay/${item.id}`;
  let method = 'post';
  let res = await getData(url,method);
  if (res.data.success){
    let timeStamp = new Date().getTime()
    showStatus({content:res.data.message,stamp:timeStamp})

  }
  toggleLoading()
  await  getOrdersData()
}


</script>
 
<template>
  <table>
    <tbody>
      <tr v-for="(item,idx) in data">
        <td>{{new Date(item.create_at*1000).toISOString().split('T')[0]}}</td>
        <td>{{item.user.name}}{{item.user.userName}}</td>
        <td>{{item.is_paid?'付錢了':'還沒付'}}</td>
        <td>{{item.total}}</td>
        <td v-if="!item.is_paid" @click="checkOut(item)"><button type="button" class="btn btn-success">去付錢</button></td>
        <td v-else><button type="button" class="btn btn-danger" disabled>富完了</button></td>
      </tr>
    </tbody>
  </table>

</template>

<style scoped>
  table{
    width:min(80%,600px);
    border-collapse: collapse;
    margin:30px auto;
    text-align: center;
  }
  td{
    border:1px solid black;
  }
</style>