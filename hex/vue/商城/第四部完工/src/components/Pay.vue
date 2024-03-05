<script setup>
  import {useRoute} from "vue-router";
  import {onMounted,ref} from "vue";

  import {getData} from "@/assets/functions";

  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;
  let route = useRoute()
  let orderId = route.params.orderID;
  let orderListData = ref({});
  let customerInfo = ref({})


  onMounted(async()=>{
    let url = `${headAPI}/api${myAPI}/order/${orderId}`
    let temp = await getData("get",url);
    orderListData.value = temp.data.order;
    customerInfo.value = temp.data.order.user
    console.log(orderListData.value.user.email);
  })

  async function checkOut(){
    let url = `${headAPI}/api${myAPI}/pay/${orderId}`;
    let res = await getData("post",url);
    console.log(res.data)
  }
</script>

<template>
  <div class="payWrap">
    <table>
      <thead>
        <tr>
          <th>品名</th>
          <th>數量</th>
          <th>單價</th>
        </tr>
      </thead>
      <tbody>
        <template v-for="(item,idx) in orderListData.products" :key="idx">
          <tr>
            <td>{{item.product.title}}</td>
            <td>{{item.qty}}</td>
            <td>{{item.product.price}}</td>
          </tr>
        </template> 
        <tr>
          <td></td>
          <td></td>
          總計{{orderListData.total}}
        </tr>
      </tbody>
    </table>


    <!-- <td>{{orderListData.user.email}}</td>
    <td>{{orderListData.user.userName}}</td>
    <td>{{orderListData.user.number}}</td>
    <td>{{orderListData.user.address}}</td>
    <td>{{orderListData.is_paid}}</td> -->

    
    <table>
      <tbody>
        <tr>
          <td>email</td>
          <td>{{customerInfo.email}}</td>
        </tr>
        <tr>
          <td>姓名</td>
          <td>{{customerInfo.userName}}</td>
        </tr>
        <tr>
          <td>電話</td>
          <td>{{customerInfo.number}}</td>
        </tr>
        <tr>
          <td>地址</td>
          <td>{{customerInfo.address}}</td>
        </tr>
        <tr>
          <td>付款</td>
          <td>{{orderListData.is_paid}}</td>
        </tr>
      </tbody>
    </table>
  </div>
  <button @click="checkOut()" type="button" class="btn btn-danger">去付款</button>
</template>