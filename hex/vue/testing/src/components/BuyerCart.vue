<script setup>
  import {ref,onMounted,inject,watch} from "vue";
  import {headAPI,myAPI,getData,getDot} from "@/functions.js";
  import {useRouter} from "vue-router";
	import {Modal} from "bootstrap";

  let data = ref([]);

  let showStatus = inject('showStatus');
  let toggleLoading = inject('toggleLoading');

  onMounted(async ()=>{
    await getCarts()
  })
  async function getCarts(){
    toggleLoading()
    let url = `${headAPI}/api${myAPI}/cart`;
    let method = 'get';
    let res = await getData(url,method);
    if (res.data.success){
      data.value = res.data.data;
      console.log(data.value)
    }
    toggleLoading()
  }

  async function delCart(id){
    toggleLoading()
    let url = `${headAPI}/api${myAPI}/cart/${id}`;
    let method = 'delete';
    let res = await getData(url,method);
    if (res.data.success){
      let timeStamp = new Date().getTime();
      showStatus({content:res.data.message,stamp:timeStamp})
    }
    toggleLoading();
    await getCarts();
 
  }
</script>

<template>
  <table>
    <thead>
      <th></th>
      <th>品茗</th>
      <th>數量</th>
      <th>單價</th>
    </thead>
    <tbody>
      <tr v-for="(item,idx) in data.carts">
        <td>
          <div @click="delCart(item.id)" class="button">
            <i class="fa-solid fa-paw"></i>
          </div>
        </td>
        <td>{{item.product.title}}</td>
        <td>{{item.qty}}</td>
        <td>{{getDot(item.product.price)}}</td>
      </tr>
      <tr>
        <td></td>
        <td></td>
        <td>總計</td>
        <td>{{getDot(data.final_total)}}</td>
      </tr>
    </tbody>
  </table>

</template>

<style scoped>
  table{
    width:min(70%,900px);
    margin: 30px auto;
    text-align: center;
    border-collapse: collapse;
  }
  thead{
    border-top:3px solid gray;
    border-bottom:3px solid gray;
  }
  tr{
    border-bottom: 1px solid gray;
  }
  td,th{
    padding:20px
  }
  th{
    padding:5px 10px;
  }
  .button{
    border:2px solid red;
    background-color: rgb(224, 224, 224);
    padding:3px;
    border-radius: 3px;
    color:red
  }
  .button:hover{
    background-color: red;
    color:black
  }
</style>