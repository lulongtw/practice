<script setup>
  import {ref,watch,computed,onMounted,inject,provide} from "vue";
  import store from "@/store/store.js";
  import {useRouter} from "vue-router";
  import {Modal} from "bootstrap";
  import {showModal,hideModal,getData} from "@/functions.js";
  import * as yup from "yup"

  let cartLst = ref(store.state.cartList)
  watch(()=>store.state.cartList,
    (newVal)=>{
      cartLst.value = newVal
    }
  )
  
  function delThisItem(id){
    let url = `/api/:api_path/cart/${id}`;
    let method = 'delete'
    let res = store.dispatch('delSingleItem',{url,method})
  }
  
</script>

<template>
  <div class="cartLst">
    <div class="item" v-for="(item,idx) in cartLst">
      <td @click="delThisItem(item.id)"><i class="fa-regular fa-trash-can"></i></td>
      <td> {{item.product.title}}</td>
      <td><span>{{item.qty}}{{item.product.unit}}</span></td>
      <td>${{item.product.price}}元</td>
    </div>
  </div>

</template>
<style scoped>

.cartLst{
    width:250px;
    position:absolute;
    top:50px;
    right:0px;
    padding:10px;
    border:1px solid black;
    background-color: white;
    height:300px;
    overflow: scroll;
  }
.item{
  border-bottom: 1px solid gray;
  display:flex;
  gap:3px;
  font-size:12px;
  align-items: center;

}
.item>td:nth-of-type(1){
  color:red;
}
.item>td:nth-of-type(2){
  width:60%;
  text-align:center;
}

</style>