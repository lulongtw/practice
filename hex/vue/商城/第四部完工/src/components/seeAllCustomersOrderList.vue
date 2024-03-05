<script setup>
  import {ref,onMounted,inject} from "vue";
  import Loading from 'vue-loading-overlay';
  import 'vue-loading-overlay/dist/css/index.css';

  import {getData} from "@/assets/functions";
  

  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;
  let allCustomerOrderList = ref([]);
  let addToStack = inject("addToStack");
  let isLoading = ref(false)

  onMounted(async()=>{
    isLoading.value = true;
    let url = `${headAPI}/api${myAPI}/orders?page=:page`;
    let temp = await getData("get",url);
    isLoading.value = false;
    allCustomerOrderList.value = temp.data.orders
  })

  async function checkOut(id){
    isLoading.value = true;
    let url = `${headAPI}/api${myAPI}/pay/${id}`;
    let temp = await getData("post",url);
    if (temp.data.success){
      addToStack(temp.data.message);
      url = `${headAPI}/api${myAPI}/orders?page=:page`;
      temp = await getData("get",url);
      allCustomerOrderList.value = temp.data.orders
      isLoading.value = false
    }
  }
</script>

<template>
  <div class="customersOrderListWrap">
    <loading v-model:active="isLoading"/>
    <table>
      <thead>
      </thead>
      <tbody>
        <template v-for="(item,idx) in  allCustomerOrderList" :key="item.id">
          <tr v-if="!item.is_paid">
            <td>{{new Date(item.create_at*1000).toISOString().split("T")[0]}}</td>
            <td>{{item.user.userName}}</td>
            <td>
              <template v-for="productInfo in item.products">
                <div>{{productInfo.product.title}} {{productInfo.qty}} {{productInfo.product.unit}}</div>
              </template>
            </td>
            <td>{{item.total}}</td>
            <td><button @click="checkOut(item.id)" type="button" class="btn btn-success">checkout</button></td>
          </tr>
        </template>
      </tbody>
    </table>
  </div>

</template>