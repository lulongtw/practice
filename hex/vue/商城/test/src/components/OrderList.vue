<script setup>
  import {ref,onMounted,computed} from 'vue';
  import {mapGetters} from "vuex";//mapGetters 在composition api不好用

  import {getData} from "@/assets/functions";
  import store from "@/store/vuex.js";



  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;


  
  //這行也可以
  // let data = computed(()=>{
  //   return store.state.orderList
  // })

  let data = computed(()=>store.getters.orderList)


  // watch(()=>store.state.orderList,
  //   ()=>{
  //     // 如果loading出現是跟非同步程式一起的話
  //     // 那麼切換loading的動作要寫在非同步程式裡面
  //     // 如果寫在同步程式裡面會因為非同步慢點執行的關係
  //     // 導致切換loading瞬間完成 連loading畫面都來不及出現就切回來了
  //     //store.commit("toggleLoading");
  //     data.value = store.state.orderList
  //     //store.commit("toggleLoading");
  //   }
  // )

  onMounted(()=>{
    let info = ["get",`${headAPI}/api${myAPI}/admin/orders?page=:page`]
    store.dispatch("fetchOrderListData",info)
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
