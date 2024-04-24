<script setup>
import axios from 'axios';
import {ref,onMounted,inject,watch} from "vue";
import {headAPI,myAPI,getData,getDot} from "@/functions.js";
import {useRouter} from "vue-router";
import {Modal} from "bootstrap";
import couponModal from "@/modal/couponModal.vue";

let toggleLoading = inject('toggleLoading')
let showStatus = inject('showStatus')
let coupon = ref([]);
let currentPage = ref(1);
let pagination = ref({});
let toSonData = ref({});
let currentId = ref("");


onMounted(async()=>{
  await getCoupon()
})

async function getCoupon(){
  toggleLoading()
  let url = `${headAPI}/api${myAPI}/admin/coupons?page=${currentPage.value}`;
  let method = 'get';
  let res = await getData(url,method);
  if (res.data.success){
    coupon.value = res.data.coupons;
    coupon.value.forEach(item=>{
      let newDate = dealTime(item.due_date);
      item.due_date = newDate
    })
    pagination.value = res.data.pagination
  }
  toggleLoading()
}
function callModal(){
  let id = document.querySelector("#couponModal");
  let modalDOM = Modal.getOrCreateInstance(id);
  modalDOM.show()
}

function editCoupon(item){
  currentId.value = item.id;

}

function dealTime(time){
  let ans = new Date(time*1000).toISOString().split("T")[0]
  return ans

}
async function sendRequest(item){
  toggleLoading()
  let url = `${headAPI}/api${myAPI}/admin/coupon/${item.id}`;
  let method = 'put';
  item.due_date = new Date(item.due_date).getTime()/1000
  let toSend = {'data':item}
  let res = await getData(url,method,toSend);
  if (res.data.success){
    let timeStamp = new Date().getTime()
    showStatus({content:res.data.message,stamp:timeStamp})
    currentId.value=""
  }
  toggleLoading()
  await getCoupon()
}

async function delCoupon(item){
  toggleLoading()
  let url = `${headAPI}/api${myAPI}/admin/coupon/${item.id}`;
  let method = 'delete';
  let res = await getData(url,method);

  if (res.data.success){
    let timeStamp = new Date().getTime()
    showStatus({content:res.data.message,stamp:timeStamp})
  }
  toggleLoading();
  await getCoupon()
}


</script>
<template>
  <couponModal @toDad="getCoupon"></couponModal>
  <button @click="callModal" type="button" class="btn btn-warning">新增</button>
    <table>
      <thead>
        <th>名稱</th>
        <th>折扣</th>
        <th>到期日</th>
        <th>啟用狀態</th>
        <th>修改</th>
      </thead>
      <tbody>
        <tr v-for="(item,idx) in coupon">
            <td>
              <input v-if="item.id==currentId" type="text" v-model="item.title">
              <span v-else> {{item.title}}</span>
            </td>
            <td>
              <input  v-if="item.id==currentId" type="text" v-model="item.percent">
              <span v-else> {{item.percent}}</span>
            </td>
            <td>
              <input  v-if="item.id==currentId" type="date" v-model="item.due_date">
              <span v-else> {{item.due_date}}</span>
            </td>
            <td>
              <input  v-if="item.id==currentId" type="checkbox" v-model="item.is_enabled" true-value=1 false-value=0>
              <span v-else> {{item.is_enabled*1?'已啟用':"未啟用"}}</span>  
            </td>
            
            <td>
              <button v-if="item.id==currentId" @click="sendRequest(item)" type="button" class="btn btn-success"
                style="--bs-btn-padding-y: .25rem; --bs-btn-padding-x: .5rem; --bs-btn-font-size: .75rem;"
                >送出</button>
              <div v-else class="button">
                <button @click="editCoupon(item)" type="button" class="btn btn-success"
                style="--bs-btn-padding-y: .25rem; --bs-btn-padding-x: .5rem; --bs-btn-font-size: .75rem;"
                >編輯</button>
                <button @click="delCoupon(item)" type="button" class="btn btn-danger"
                style="--bs-btn-padding-y: .25rem; --bs-btn-padding-x: .5rem; --bs-btn-font-size: .75rem;"
                  >刪除</button>
              </div>
            </td>



        </tr>
      </tbody>
    </table>
</template>
<style scoped>
table{
  width:min(900px,95%);
  margin:10px auto;
  border-collapse: collapse;
  text-align:center;
}
  thead{
    border:1px solid black;
  }
  tr{
    border-bottom:1px solid black;
  }
  td{
    border-right:1px solid black;
    padding:15px;
  }
  tr>td:last-of-type{
    border-right:0px 
  }
  tbody>tr:last-of-type{
    border-bottom:0px 
  }
  input{
    width:100%;
    text-align:center;
  }
</style>