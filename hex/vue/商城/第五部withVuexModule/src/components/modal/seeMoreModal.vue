<script setup>
  import {watch,ref,inject} from "vue";
  import axios from "axios";
  import {Modal} from "bootstrap";

  import {noCatch} from "@/assets/functions";

  let props = defineProps({
    fromDad:Object
  });
  let emits = defineEmits(["toggleSeeMoreLoading"])
  let data = ref(props.fromDad);
  let count = ref(1);
  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;
  let msg = ref("");
  let addToStack = inject("addToStack");



  watch(()=>{props.fromDad},
    ()=>{
      data.value = props.fromDad;
      count.value=1
    },{
      deep:true
    })
  function addToCart(){
    emits("toggleSeeMoreLoading")
    let url = `${headAPI}/api${myAPI}/cart`;
    let dataToSend = {
      "data":{
        "product_id":data.value.id,
        "qty":count.value }
      }
      noCatch(axios.post(url,dataToSend)
        .then(res=>{
          if (res.data.success){
            emits("toggleSeeMoreLoading")
            msg.value = res.data.message;
            addToStack(msg.value)
          }
        })
      )
      let modalDom = document.querySelector("#seeMoreModal");
      let modalInstance = Modal.getOrCreateInstance(modalDom);
      modalInstance.hide();
    }

  
</script>

<template>
  <div class="modal fade" id="seeMoreModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">{{data.title}}</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <img :src="`${data.imageUrl}`" alt="">
        <div class="cntn">
          <div class="des">{{data.content}}</div>
          <div class="originPrice">{{data.origin_price}}</div>
          <div class="price">{{data.price}}</div>
          <select v-model="count">
            <option v-for="item in 10" :value="item">選購{{item}}{{data.unit}}</option>
          </select>
        </div>
      </div>
      <div class="modal-footer">
        <div class="total">小計{{count*data.price}}</div>
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button @click="addToCart()" type="button" class="btn btn-primary">加入購物車</button>
      </div>
    </div>
  </div>
</div>

</template>

<style>
  img{
    object-fit:contain;
    width:100%;
  }
  .cntn{
    display: grid;
    grid-template-columns:2fr 3fr;
  }
  .des,select{
    grid-column:span 2;
  }

</style>