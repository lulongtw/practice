<script setup>
  import axios from "axios";
  import {ref,onMounted,inject} from "vue";
  import {Modal} from "bootstrap";

  import {noCatch} from "@/assets/functions";
  import SeeMoreModal from "@/components/modal/seeMoreModal.vue";
  import buildOrderList from "@/components/buildOrderList.vue";
 
  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;
  let productList = ref([]);
  let itemId = ref({});
  let cartList = ref([]);
  let addToStack = inject("addToStack");
  let seeMoreLoading = ref(false);
  let addToCartLoading = ref(false);
  let currebtItemId = ref("");
  let couponCode = ref("");


  onMounted(async()=>{
    await getProductList()
    await refreshCartList()
  });
  
  async function getProductList(){
    let url = `${headAPI}/api${myAPI}/products?page=:page`
    await noCatch(axios.get(url)
      .then(res=>{
        //console.log(res)
        productList.value = res.data.products
      })
    )
  }
  function showModal(item){
    currebtItemId.value = item.id;
    console.log(item)
    itemId.value = item;
    let modalDom = document.querySelector("#seeMoreModal");
    let modalInstance = Modal.getOrCreateInstance(modalDom);
    modalInstance.show();
  }

  async function refreshCartList(){
    let url = `${headAPI}/api${myAPI}/cart`;
    await noCatch(axios.get(url)
      .then(res=>{
        if (res.data.success){
          cartList.value = res.data.data;
           //console.log(cartList.value)
        }
      })
    )
  }

  async function delItem(id){
    let url = `${headAPI}/api${myAPI}/cart/${id}`;
    await noCatch(axios.delete(url)
      .then(res=>{
        if (res.data.success){
          addToStack(res.data.message)
          refreshCartList()
        }
      })
    )
  }
  function addToCart(item){
    currebtItemId.value = item.id
    addToCartLoading.value = true;
    let url = `${headAPI}/api${myAPI}/cart`;
    let dataToSend = {
      "data":{
        "product_id":item.id,
        "qty":1 }
      }
      noCatch(axios.post(url,dataToSend)
        .then(res=>{
          if (res.data.success){
            addToCartLoading.value = false;
            addToStack(res.data.message)
          }
        })
      )
    }
    function changeStatus(){
      seeMoreLoading.value = !seeMoreLoading.value;
    }
    function checkSeeMoreLoading(id){
      if (seeMoreLoading.value && currebtItemId.value == id){
        return true
      }
  
    }
    function checkAddToCartLoading(id){
      if (addToCartLoading.value && currebtItemId.value == id){
        return true
      }
    }

    async function useCoupon(){
      let url = `${headAPI}/api${myAPI}/coupon`;
      await noCatch(axios.post(url,{"data":{
        "code":couponCode.value
      }})
        .then(res=>{
          addToStack(res.data.message);
          if (res.data.success){
            
          }
        })
      )
    }
</script>

<template>
  <div class="semiOrderWrap">
    <div class="semiOrderItem" v-for="(item,key) in productList" :key="item.id">
      <div class="semiOrderPic" :style="`background-image:url('${item.imageUrl}')`"></div>
      <div class="semiOrderContent">
        <div class="semiOrderTitle">{{item.title}}
        </div>
        <div class="semiOrderCategory">{{item.category}}</div>
        <div class="semiOrderDes">{{item.description}}</div>
        <div class="semiOrderOriginPrice">{{item.origin_price}}</div>
        <div class="semiOrderPrice">{{item.price}}</div>
        <div class="semiOrderButtons">
          <div @click="showModal(item)"  class="btnn seeMoreBtn"><i  v-if="checkSeeMoreLoading(item.id)" class="fa-solid fa-rotate-right fa-spin"></i>查看更多</div>
          <div @click="addToCart(item)" class="btnn addToCartBtn"><i v-if="checkAddToCartLoading(item.id)" class="fa-solid fa-rotate-right fa-spin"></i>加入購物車</div>
        </div>
      </div>
    </div>
  </div>
  <SeeMoreModal :fromDad="itemId" @toggleSeeMoreLoading="changeStatus"></SeeMoreModal>
  <hr>
  <button @click="refreshCartList()" class="btn btn-outline-secondary" type="button" id="button-addon1">refreshCartList</button>
  <div class="cartListWrap">
    <table>
    <thead>
      <th></th>
      <th>品名</th>
      <th>數量</th>
      <th>單價</th>
    </thead>
    <tbody>
      <template v-for="(item,key) in cartList.carts" :key="item.id">
        <tr>
          <td @click="delItem(item.id)"><i class="fa-solid fa-trash-can"></i></td>
          <td>
            {{item.product.title}}
            <span v-if="item.coupon">已套用優惠券</span>
          </td>
          <td>{{item.qty}}</td>
          <td>{{item.product.price}}</td>
        </tr>
      </template>
    </tbody>
  </table>
  <div style="text-align:right;padding:5px;">{{cartList.total}}元
    <div v-if="cartList.total != cartList.final_total">
      只要 <span style="color:rgb(12, 184, 12);font-size:30px;">{{cartList.final_total}}</span>元
    </div>
  </div>
  <div class="input-group mb-3">
    <input v-model="couponCode" type="text" class="form-control" placeholder="輸入優惠碼" aria-label="Recipient's username" aria-describedby="button-addon2">
    <button @click="useCoupon()" class="btn btn-outline-secondary" type="button" id="button-addon2">送出優惠碼</button>
  </div>
  <buildOrderList @sendOrderList="refreshCartList"></buildOrderList>
  
  </div>
</template>

<style scoped>
  .semiOrderWrap{
    display:flex;
    margin: 50px auto;
    flex-wrap:wrap;
    gap:10px;
  }
  .semiOrderItem{
    width:32%;
    border:1px solid black;
  }
  .semiOrderPic{
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    height:200px;
  }
  .semiOrderContent{
    padding:10px 15px;
    display:grid;
    grid-template-columns:3fr 2fr;
    gap:10px;
  }
  .semiOrderDes,.semiOrderButtons{
    grid-column:span 2;
  }
  .semiOrderCategory,.semiOrderPrice{
    text-align:right;
  }
  .semiOrderButtons{
    display: flex;
    justify-content: space-between;
    padding:10px 5px;
    background-color: rgb(214, 210, 210);
  }
  .btnn{
    width:45%;
    display: inline-block;
    border:1px solid green;
    padding:3px;
    text-align: center;
    font-size: 13px;
    
  }
  .seeMoreBtn{
    border-color: red;
  }

  .cartListWrap{
    width:80%;
    margin:30px auto;
  }
  thead{
    border:none;
    border-top:5px solid gray;
    border-bottom:5px solid gray;
    
  }
  th{
    padding:5px;
  }
  td{
    border:none;
    padding:20px 5px;
  }
  span{
    color:rgb(88, 147, 0);
    font-size: 12px;
  }
  .price>td{
    width:100%;
  }
  div{
    width:100%;
  }
</style>