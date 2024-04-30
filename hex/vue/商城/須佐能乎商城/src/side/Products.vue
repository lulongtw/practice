<script setup>
  import {ref,watch,computed,onMounted,inject,provide} from "vue";
  import store from "@/store/store.js";
  import {useRouter} from "vue-router";
  import {Modal} from "bootstrap";
  import {showModal,hideModal,getData} from "@/functions.js";
  import LookDetailModal from "@/modal/lookDetailModal.vue"
  import * as yup from "yup"

  let products = ref([]);
  let currentCategory = ref(store.state.currentCategory);
  let currentItem = ref({});


  let currentCategoryLength = ref("");
  let currentPage = ref(0);

//1 , 5, 9  %4==1

  let currentShow = computed(()=>{
    if ( products.value[currentCategory.value]){
      let ans = products.value[currentCategory.value].slice(currentPage.value,currentPage.value+2);
    return ans
    }
  });
  let pages = computed(()=>{
    return Math.ceil(currentCategoryLength.value/2)
  })


  watch(()=>store.state.currentCategory,
    (newVal)=>{
      currentCategory.value = newVal;
      currentCategoryLength.value = products.value[currentCategory.value].length
   
    }
  )
  watch(()=>store.state.allProducts,
    (newVal)=>{
      products.value = newVal;
    }
  )
  function lookDetail(item){
    currentItem.value = item
  }

  async function addToCart(item){
    let url = '/api/:api_path/cart';
    let method = 'post';
    let toSend = { "data": { "product_id":item.id,"qty":1 } };
    let res = await getData(url,method,toSend);
    if (res.data.success){
       url = `/api/:api_path/cart`
       method = 'get';
      store.dispatch('getCartList',{url,method});
    }
  }
  function goPage(page){
    currentPage.value = page*2+1
  }
</script>

<template>
  <LookDetailModal :currentItem="currentItem"></LookDetailModal>
  <div class="productsWrap">
      <div  v-for="(item,idx) in currentShow" class="item">
        <div class="pic"><img :src="item.imageUrl"></div>
        <div class="name">{{item.title}}</div>
        <div class="content">{{item.content}}</div>
        <div class="buttons">
          <button @click="lookDetail(item)" type="button" class="btn btn-primary"
           style="--bs-btn-padding-y: .25rem; --bs-btn-padding-x: .5rem; --bs-btn-font-size: .75rem;"  data-bs-toggle="modal" data-bs-target="#lookDetailModal">
              看仔細
          </button>
          <button @click="addToCart(item)" type="button" class="btn btn-danger"
            style="--bs-btn-padding-y: .25rem; --bs-btn-padding-x: .5rem; --bs-btn-font-size: .75rem;">
            直購霸狗！
          </button>
        </div>
      </div>
  </div>

  <nav aria-label="Page navigation example">
  <ul class="pagination">
    <li class="page-item"><a class="page-link" href="#">Previous</a></li>
    <li @click="goPage(item-1)" class="page-item" v-for="item in pages"><a class="page-link" href="#">{{item}}</a></li>
    <li class="page-item"><a class="page-link" href="#">Next</a></li>
  </ul>
</nav>
</template>
<style scoped>
  .productsWrap{
    /* display:grid;
    grid-template-columns:1fr 1fr; */
    display:flex;
    flex-wrap:wrap;
    gap:30px;    
  }
  .item{
    border:1px solid gray;
    text-align:center;
    display:flex;
    flex-direction: column;
    gap:10px;
    width:250px;
    border-radius:30px 0px 30px 0px;
  }
  img{
    width:100%;
    height:200px;
    object-fit:cover;
    border-radius:30px;
    border-radius:30px 0px 0px 0px;
    
  }
  .buttons{
    padding:10px;
    background-color: rgb(214, 214, 214);
    border-radius:0px 0px 30px 0px;
    display:flex;
    justify-content: space-evenly;
  }
  @media (max-width:800px){
    .productsWrap{
      justify-content: center;
    }
  }
</style>