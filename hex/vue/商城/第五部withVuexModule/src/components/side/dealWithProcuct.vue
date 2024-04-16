<script setup>
  import {ref,watch} from "vue";
  import {noCatch} from "@/assets/functions";
  import axios from "axios";
  let props = defineProps({
    fromDad:Object
  })

  let data = ref(props.fromDad);
  let picIsLoading = ref(false);


  watch(()=>props.fromDad,
        ()=>data.value = props.fromDad
  )

  async function uploadFile(e){
    picIsLoading.value = true
    let files = e.target.files
    let toUploadData = new FormData();
    toUploadData.append("pic",files[0]);
    let headAPI = import.meta.env.VITE_headAPI;
    let myAPI = import.meta.env.VITE_myAPI;
    let url = `${headAPI}/api${myAPI}/admin/upload`;
    await noCatch(axios.post(url,toUploadData)
    .then(res=>{
      console.log(res)
      picIsLoading.value = false
      data.value.imageUrl = res.data.imageUrl;
    })
    )
  }
</script>

<template>
  <div class="dealWithProcuctWrap">
    <div class="picWrap">
      <label for="picUrl">輸入圖片網址
        <input v-model="data.imageUrl" type="text" id="picUrl">
      </label>
      <label for="picFile">或上傳圖片  
        <i v-if="picIsLoading" class="fa-solid fa-spinner fa-spin"></i>
        <input @change="uploadFile($event)" type="file" id="piFile">
      </label>
      <img :src="data.imageUrl" alt="">
      
    </div>
    <div class="contentWrap">
      <label for="title">標題
        <input v-model="data.title" type="text">
      </label>
      <label for="title">分類
        <input v-model="data.category" type="text">
      </label>
      <label for="title">單位
        <input v-model="data.unit" type="text">
      </label>
      <label for="title">原價
        <input v-model="data.origin_price" type="text">
      </label>
      <label for="title">售價
        <input v-model="data.price" type="text">
      </label>
      <hr>
      <label for="description">描述
        <textarea v-model="data.description" id="description"></textarea>
      </label>
      <br>
      <label for="content">內容
        <textarea v-model="data.content" id="content"></textarea>
      </label>

     <label class="a">
      啟用?
      <input v-model="data.is_enabled" type="checkbox"  id="is_enabled" >
    </label>
     
    
    </div>
  </div>
</template>

<style scoped>
  .dealWithProcuctWrap{
    box-sizing: border-box;
    padding:5px;
    display:grid;
    grid-template-columns:1fr 2fr;
    gap:20px;

  }

  label,input,textarea{
    width:100%;

  }
  .picWrap{
    display:flex;
    flex-direction:column;
    gap:15px;
  }
  .contentWrap{
    display:grid;
    grid-template-columns:1fr 1fr;

    column-gap:10px;
  }
  .contentWrap>label:nth-of-type(1),.contentWrap>label:nth-of-type(6),.contentWrap>label:nth-of-type(7),hr{
    grid-column:span 2;
  }
  label{
    margin-bottom:10px;
  }
  .a{

    display: flex;
  }
  input[type='checkbox']{
    width:50%;
  }
  img{
    width:100%;
    object-fit:cover;
  }
</style>