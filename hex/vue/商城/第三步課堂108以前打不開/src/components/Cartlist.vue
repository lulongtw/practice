<script setup>
  import axios from "axios";
  import {ref,onMounted,reactive} from "vue";

  import {noCatch} from "@/assets/functions";
  import {getDot} from "@/assets/functions";
  import Nono from "@/components/sideComs/Nono.vue"

  let cartLst = ref([]);
  let allData = ref({});
  let cartLstLoading = ref(false);
  let sendtoNono = reactive([])

  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;


  async function getData(){
    cartLstLoading.value = true
    let url = `${headAPI}/api${myAPI}/cart`;
    await noCatch(axios.get(url)
    .then(res=>{
      if(res.data.success){
        //console.log(res);
        cartLst.value = res.data.data.carts;
        allData.value = res.data.data;
        cartLstLoading.value = false
      }
    })
  )
  }

  async function delThis(id){
    let url = `${headAPI}/api${myAPI}/cart/${id}`;
    await noCatch(axios.delete(url)
      .then(res=>{
        sendtoNono.push({msg:res.data.message})
        getData();
      })
    )
  }

  onMounted(async ()=>{
    await getData()
  })


</script>


<template>
  <div>
    <button @click="getData()">refresh Cart List</button>
    <i v-if="cartLstLoading" class="fa-solid fa-spinner fa-spin"></i>
    <div v-else class="CartListWrap">
      <table>
        <thead>
          <th></th>
          <th>品名</th>
          <th>數量</th>
          <th>單價</th>
        </thead>
        <Nono :res="sendtoNono"></Nono>
        <tbody>
          <tr v-for="item in cartLst">
            <td>
              <button @click="delThis(item.id)" class="del"><i class="fa-solid fa-trash-can"></i></button>
            </td>
            <td>
              <div>
              {{item.product.title}}
              <div class="coupon" v-if="item.coupon">以套用優惠券</div>
              </div>
            </td>
            <td>{{item.qty}}</td>
            <td>{{getDot(item.product.price)}}</td>
          </tr>
          <tr>
            <td></td>
            <td></td>
            <td>總計</td>
            <td>{{getDot(allData.total)}}</td>
          </tr>
          <tr v-if="allData.final_total!=allData.total" style="color:green">
            <td></td>
            <td></td>
            <td>折扣</td>
            <td>{{getDot(allData.final_total)}}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  
</template>

<style scoped>
  .CartListWrap{
    padding:15px;
    width:min(500px,80%);
    margin:0 auto;
  }
  table{
    width:100%;
    text-align: center;
  }

  thead{
    border-top:3px solid gray;
    border-bottom:3px solid gray;
  }
  th{
    padding:5px 20px;
  }

  .del{
    vertical-align: middle;
    color:red;
    border-color: red;
    border-radius: 7px;
    
  }
  td{
    border-bottom:1px solid gray;
    padding:20px;

  }
  .coupon{
    color:green;
  }
</style>