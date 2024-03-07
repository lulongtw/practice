<script setup>
  import {ref,watch} from "vue"

  import store from "@/store/vuex.js";

  let props = defineProps({
    data:Array,
    currentShow:String
  })
  // let selectedData = ref([]);

  // watch(()=>props.data,
  //   ()=>{
  //     selectedData.value = props.data
  //   },
  //   {deep:true}
  // )

  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;

  function addToCart(id,qty=1){
    let url = `${headAPI}/api${myAPI}/cart`
    let payload = ["post",url,{
      "data":{
        "product_id":id,"qty":qty
    }}]
    store.dispatch("addToCart",payload);
  }
</script>
<template>
  <div class="itemColumnWrap">
    <template v-for="(item,idx) in props.data" :key="item.id">   
      <div class="item"  v-if="item.category==props.currentShow">
        <div class="pic" :style="`background-image:url('${item.imageUrl}')`"></div>
        <div class="title">
          {{item.title}}
        </div>
        <div class="description">
          {{item.description}}
        </div>
        <div class="button">
          <button type="button" class="btn btn-primary btn-sm">SeeMore</button>
          <button @click="addToCart(item.id,1)" class="btn btn-outline-secondary btn-sm" type="button" id="button-addon2">
            <i class="fa-solid fa-cart-shopping"></i>
            加入購物車</button>
          
        </div>
      </div>
    </template>
  </div>
</template>

<style scoped>
  .itemColumnWrap{
    display:flex;
    flex-wrap:wrap;
    gap:30px;
    text-align: center;
  }
  .item{
    width:250px;
    padding:10px;
  }
  .pic{
    height:200px;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
  }
  .button{
    display: flex;
    justify-content: space-between;
    padding:0 5px;
  }
  .item>*{
    margin-bottom:20px;
  }
</style>