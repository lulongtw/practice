<script setup>
  import {ref,watch,computed,onMounted} from "vue";
  import store from "@/store/store.js";
  import {useRouter} from "vue-router";
  import {Modal} from "bootstrap";
  import {showModal} from "@/functions.js";
  
  import Jumbo from "@/side/Jumbo.vue";
  import Category from "@/side/Category.vue";
  import Products from "@/side/Products.vue";
  import GoToSellerModal from "@/modal/GoToSellerModal.vue";
  import CartLst from "@/side/CartLst.vue";

  let data = ref(store.state.allProducts);
  let cartList = ref(store.state.cartList)
  let categories = ref([]);
  let showCartLst = ref(false)


  onMounted(()=>{   
    let url = `/api/:api_path/products/all`
    let method = 'get';
    store.dispatch('fetchAllProducts',{url,method});

    
    url = `/api/:api_path/cart`
    method = 'get';
    store.dispatch('getCartList',{url,method});
  })



  watch(()=>store.state.cartList,
    (newVal)=>{
      cartList.value = newVal;
     // console.log(cartList.value)
    }
  )

  watch(()=>store.state.allProducts,
    (newVal)=>{
      data.value = newVal;
      categories.value = Object.keys(data.value)
    }
  )


</script>
showCartLst
<template>
  <GoToSellerModal></GoToSellerModal>
  <div class="buyerMainWrap">
     <header>
    <div @click="showModal('#GoToSellerModal')"><i class="fa-solid fa-paw"></i>肥狗超商</div>
    <div @click="()=>{ showCartLst = !showCartLst}" class="cart">
      <i class="fa-solid fa-cart-shopping"></i>
      {{cartList.length}}
      <CartLst v-if="showCartLst"></CartLst>
    </div>
  </header>
  <aside>
    <Jumbo></Jumbo>
  </aside>
  <main>
      <div class="category">
        <Category :categories="categories" ></Category>
      </div>
      <div class="productsArea">
        <Products></Products>
      </div>
    </main>
  <footer>
    <div>© Copright 2017 六角血拼賣賣  Instagrame  Facebook About</div>
    <div>Made with Bootstrap5</div>
  </footer>

  </div>
 

</template>
<style scoped>
  *{
    padding:0xp;margin:0px;
  }
  .buyerMainWrap{
    width:90%;
    margin:0 auto
  }
  header{
    display:flex;
    justify-content: space-between;
    padding:10px 50px;
    position: sticky ;
    top:0;
    margin: 0 auto;
    background-color: rgb(255, 255, 255);
  }
  header>div{
    font-size: 1.3rem;
  }
  .cart{
    position: relative;
    background-color: gray;
    padding:10px;
    border-radius:10px;
  }
  main{
    display:grid;
    grid-template-columns:1fr 3fr;
    gap:30px;
  }
  footer{
    text-align: center;
  }
  .category{
    z-index:0;
  }
  

</style>