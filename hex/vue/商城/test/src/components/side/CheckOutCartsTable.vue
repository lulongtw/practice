<script setup>
  import store from "@/store/vuex";

  let props = defineProps({
    cartList:Array
  });

  function deleItemFromCart(id){
    store.dispatch("deleteProductFromCarts",id);
  }

</script>
<template>
  <div class="tableWrap">
    <table>
    <thead>
      <tr>
        <th></th>
        <th></th>
        <th>商品名稱</th>
        <th>數量</th>
        <th>小計</th>
      </tr>
    </thead>
    <tbody>
      <template v-for="(item,idx) in props.cartList" :key="item.id">
        <tr >
          <td @click="deleItemFromCart(item.id)"><i class="fa-regular fa-trash-can"></i></td>
          <td><img :src=item.product.imageUrl alt="" width=100></td>
          <td>{{item.product.title}}</td>
          <td>{{item.qty}}{{item.product.unit}}</td>
          <td>{{item.final_total}}</td>
        </tr>
      </template>
    </tbody>
    <div>運費</div>
    <div>合計</div>
  </table>
  </div>  
</template>
<style scoped>

  table{
    width:100%;
    margin:0 auto;
  }
  tr{
    border-top:1px solid gray;
    border-bottom:1px solid gray;
  }
  img{
    padding:5px;
    border:1px solid black;
  }
  tr>td:first-of-type{
    text-align: center;
  }
  td{
    padding:5px 0;
  }
</style>