<script setup>
  import axios from "axios";
  import {useRouter} from "vue-router";
  import {onMounted,ref} from "vue"; 
  import {Modal} from 'bootstrap';
  import Loading from 'vue-loading-overlay';
  import 'vue-loading-overlay/dist/css/index.css';

  import {noCatch} from "@/assets/functions";
  import addNewItemModal from "@/components/modal/addNewItemModal.vue";
  import pageCom from "@/components/side/pageCom.vue"

  let router = useRouter();
  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;
  let data = ref([]);
  let action = ref("1");
  let itemToEdit = ref({});
  let isLoading = ref(false);
  let pagination = ref({});

  function callModal(act,item){
    action.value = act;
    if (item){
      itemToEdit.value = item
    }
    let modalCom = document.querySelector("#addNewItemModal");
    let modalInstance = Modal.getOrCreateInstance(modalCom);

    modalInstance.show();
  }


  function getRes(enabled){
    return enabled?"啟用":"未啟用"
  }

  function showLoading(){
    isLoading.value = true
  }

  async function refreshPage(page=1){
    let url = `${headAPI}/api${myAPI}/admin/products?page=${page}`;
    await  noCatch(axios.get(url))
    .then(res=>{
         //如果在登入後  在Index畫面時  進入console application 把cookies刪掉  就無法進入
      console.log(res.data)
      data.value = res.data.products;
      isLoading.value = false
      pagination.value = res.data.pagination;
    })
  }

  onMounted(()=>{
    refreshPage()
  })

</script>

<template>

  <div class="productWrap">

    <loading v-model:active="isLoading"/>
    <button @click="callModal('create',{})" type="button" class="btn btn-primary addNew">建立新產品</button>
    <table>
    <thead>
      <th>分類</th>
      <th>名稱</th>
      <th>原價</th>
      <th>售價</th>
      <th>啟用狀態</th>
      <th>編輯</th>
    </thead>
    <tbody>
      <template v-for="(item,idx) in data" :key="item.id">
        <tr>
          <td>{{item.category}}</td>
          <td>{{item.title}}</td>
          <td>{{item.origin_price}}</td>
          <td>{{item.price}}</td>
          <td>{{getRes(item.is_enabled)}}</td>
          <td>
            <button @click="callModal('edit',item)" class="btn btn-outline-secondary edit" type="button" id="button-addon1">edit</button>
            <button @click="callModal('del',item)" class="btn btn-outline-secondary del" type="button" id="button-addon1">del</button>
          </td>
        </tr>
      </template>
    </tbody>
  </table>

  <pageCom :pagi="pagination" @goPage="refreshPage"></pageCom>
  </div>
  <addNewItemModal :fromDad="[action,itemToEdit]" @callRefresh="refreshPage" @isLoading="showLoading"></addNewItemModal>
</template>

<style>
  @import "@/assets/Product.scss";

</style>