<script setup>
  import {ref,onMounted} from 'vue'

  import {getData} from "@/assets/functions";
  import store from "@/store/vuex.js"


  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;
  let data = ref({})

  onMounted(async()=>{
    store.commit("toggleLoading");
    let url = `${headAPI}/api${myAPI}/admin/orders?page=:page`
    let temp = await getData("get",url);
    store.commit("toggleLoading");
    data.value = temp.data.orders
  })
</script>

<template>
  <div class="orderListWrap">
    <table>
      <thead>
        <th>購買時間</th>
        <th>伊妹兒</th>
        <th>購買項目</th>
        <th>應付金額</th>
        <th>是否付款</th>
      </thead>
      <tbody>
        <template v-for="(item,idx) in data" :key="item.id">
          <tr>
            <td>{{new Date(item.create_at*1000).toISOString().split("T")[0]}}</td>
            <td>{{item.user.email}}</td>
            <td><div v-for="product in item.products">{{product.product.title}} 數量 : {{product.qty}}{{product.product.unit}}</div></td>
            <td>${{item.total}}</td>
            <td>
              <div v-if="item.is_paid" style="color:rgb(100, 166, 0)">已付款</div>
              <div v-else>尚未付款</div>
            </td>
          </tr>
        </template>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
  tr>td:nth-of-type(3){
    font-size:13px;
  }
</style>
