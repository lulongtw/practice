<script setup>
  import {Modal} from "bootstrap";
	import {ref,onMounted,inject,watch} from "vue";
  import {headAPI,myAPI,getData,getDot} from "@/functions.js";
  
  let props = defineProps(['fromDad']);
  let data = ref(props.fromDad);
  let amount = ref(1);
  let toggleLoading = inject('toggleLoading');
  let showStatus = inject('showStatus')

  watch(()=>props.fromDad,
    (newVal)=>{
      amount.value = 1
      data.value = newVal;
   //   console.log(data.value)
    }
  )
  async function addToCart(){
    let htmlDOM = document.querySelector('#seeMoreModal');
    let modalDOM = Modal.getOrCreateInstance(htmlDOM);
    modalDOM.hide();
    toggleLoading()
    let url = `${headAPI}/api${myAPI}/cart`;
    let method = 'post';
    let toSend = { "data": { "product_id":data.value.id,"qty":amount.value } };
    let res = await getData(url,method,toSend);
    if (res.data.success){
      toggleLoading()
      //console.log(res.data.message)
      let timeStamp = new Date().getTime();
      showStatus({content:res.data.message,stamp:timeStamp})
     
    }
    //console.log(res);
    
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
          <div class="seeMoreWrap">
            <div class="pic" :style="`background-image:url(${data.imageUrl})`"></div> 
            <div class="contentWrap">
              <div class="content">{{data.content}}</div>
              <div class="originPrice">{{data.origin_price}}</div>
              <div class="price">{{data.price}}</div>
              <select v-model="amount" name="" id="">
                <option v-for="item in 10" :value="item">選購{{item}}{{data.unit}}</option>
              </select>
            </div>     
          </div>
        </div>
        <div class="modal-footer">
          <div class="total">小計{{data.price * amount}}</div>
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button @click="addToCart" type="button" class="btn btn-primary">加入購物車</button>
        </div>
      </div>
    </div>
  </div>

</template>
<style scoped>
  .pic{
    width:100%;
    height:350px;
    background-size: cover;
    background-position: center;
  }
  .contentWrap{
    padding:10px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap:10px;
    align-items: baseline;
    font-size: 1.5rem;
  }
  .content{
    grid-column:span 2
  }
  .originPrice{
    text-decoration:line-through;
    vertical-align:middle;

  }
  .price{
    font-size:2rem;
    font-weight:800;
    text-align: right;

  }
  select{
    grid-column:span 2
  }
  
</style>