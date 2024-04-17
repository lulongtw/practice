<script setup>
  import {ref,onMounted,inject,watch} from "vue";
  import {headAPI,myAPI,getData,getDot} from "@/functions.js";
  import {useRouter} from "vue-router";
  import {Modal} from "bootstrap";
  import modal3in1 from "@/modal/modal3in1.vue";
  import Page from "@/components/Pages.vue";

  let data = ref([]);
  let toSon = ref("")
  let toggleLoading = inject('toggleLoading');
  let currentPage = ref(1)
  let pagination = ref("");
  
  
  onMounted(async()=>{
    await getProduct()
  })
  watch(()=>currentPage.value,
    async(newVal)=>{
      await getProduct()
    }
  )


  async function getProduct(){
    toggleLoading()
    let url = `${headAPI}/api${myAPI}/admin/products?page=${currentPage.value}`;
    let res = await(getData(url,'get'));
    if (res.data.success){
      data.value = res.data.products;
      pagination.value = res.data.pagination
    }
    toggleLoading()
  }

  function cngPage(newPage){
    currentPage.value = newPage
  }

  function callMadal(method,data){
    let id = document.querySelector("#modal3in1");
    let modalDOM = Modal.getOrCreateInstance(id);
    //console.log(method)
    switch (method){
      case "add":
        toSon.value = ["add",[]]
        break
      case "edit" :
        toSon.value = ["edit",data]
        break
      case "del" :
        
        toSon.value = ['del',data]
 
        break
    }
  
    modalDOM.show()
  }
</script>
<template>
  <div @click="console.log(data)">dasd</div>
  <modal3in1 :fromDad="toSon" @callDad="getProduct"></modal3in1>
  <button @click="callMadal('add')" type="button" class="btn btn-primary">新增商品</button>
  <table>
    <thead>
      <tr>
        <td>分類</td>
        <td>名稱</td>
        <td>原價</td>
        <td>售價</td>
        <td>啟用??</td>
        <td>編輯</td>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(item,idx) in data">
        <td>{{item.category}}</td>
        <td>{{item.title}}</td>
        <td>{{getDot(item.origin_price)}}</td>
        <td>{{getDot(item.origin_price)}}</td>
        <td>{{item.is_enabled?'啟用':'未啟用'}}</td>
        <td>
          <button @click="callMadal('edit',item)" type="button" class="btn btn-outline-success">edit</button>
          <button @click="callMadal('del',item)" type="button" class="btn btn-outline-danger">dele</button>
        </td>
      </tr>
    </tbody>
  </table>
    <Page :fromDad="pagination" @turnPage="cngPage"></Page>
  
</template>
<style scoped>
  table{
    width:min(80%,900px);
    margin:30px auto;
    border:1px solid black;
    border-collapse: collapse;
    text-align: center;
  }
  td{
    border:1px solid black;
    padding:5px 10px;
  }
  
</style>