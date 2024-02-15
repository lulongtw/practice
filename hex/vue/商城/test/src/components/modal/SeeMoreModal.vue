<script setup>
  import {onMounted,ref,watch} from "vue";
  import axios from "axios";
  import {Modal} from "bootstrap";

  import {noCatch} from "@/assets/functions";


  let data = ref([]);
  let isLoading = ref(true);
  let quantity = ref(1)

  let props = defineProps({
    fromDad:Object
  });

  watch(()=>props.fromDad,
    ()=>{ 
        data.value = props.fromDad;
        isLoading.value = false    
    },
    {deep:true}
  )
  function addToCart(){
    let headAPI = import.meta.env.VITE_headAPI;
    let myAPI = import.meta.env.VITE_myAPI;
    let url = `${headAPI}/api${myAPI}/cart`;
    let toSend = {
      "data":{
        "product_id":data.value.id,
        "qty":quantity.value
      }
    }
    noCatch(axios.post(url,toSend)
      .then(res=>{
        //console.log(res)
      })
    );
    quantity.value = 1;
    let modalDOM = document.querySelector("#SeeMoreModal");
    let modalInstance = Modal.getOrCreateInstance(modalDOM);
    modalInstance.hide();
  }

</script>

<template>
<div>
  
  <div class="modal fade" id="SeeMoreModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="staticBackdropLabel">{{data.title}}</h1>
        <button @clicl="quantity= 1" type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <i v-if="isLoading" class="fa-solid fa-spinner fa-spin"></i>
        <div v-else class="seeMoreWrap">
          <div class="seeMorepic" :style="`background-image:url(${data.imageUrl})`"></div>
          <div class="seeMoreContentWrap">
            <div class="seeMoreContent">{{data.content}}</div>
            <div class="seeMorePriceWrap">
              <div class="seeMoreOrigin">原價{{data.origin_price}}元</div>
              <div class="seeMorePrice">現在只要{{data.price}}元</div>
            </div>
            <!-- <select @change="quantity = $event.target.value "> -->
            <select v-model="quantity">
              <option v-for="num in 10" :value="num">{{"選購"+num+data.unit}}</option>
            </select>
          </div>
        </div>

      </div>
      <div class="modal-footer">
        <div class="seeMoreTotal">小計{{data.price*quantity}}</div>
        <button @click="isLoading=true;quantity = 1" type="button"  class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button @click="addToCart()" type="button" class="btn btn-primary">加入購物車</button>
      </div>
    </div>
  </div>
</div>

</div>


</template>

<style scoped>
  i{
    font-size: 100px;;
    position: relative;
    margin:0 auto;
  }
  .modal-body{
    text-align: center;
  }
  .seeMorepic{
    height:350px;
    background-size:cover;
    background-position:center;
  }
  .seeMoreContentWrap{
    padding:20px;
  }
  .seeMoreContent{
    text-align: left;
  }
  .seeMorePriceWrap{
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .seeMoreOrigin{
    text-decoration: line-through;
  }
  .seeMorePrice{
    font-size: 1.5rem;
    font-weight:800;
  }
  select{
    width:100%;
  }
  .seeMoreTotal{
    vertical-align: bottom;
  }
</style>