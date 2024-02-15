<script setup>
  import {ref,defineProps,onMounted,watch} from "vue";
  import axios from "axios";
  import {noCatch,hideModal} from "@/assets/function.js"
  import { Modal } from 'bootstrap';

  let props = defineProps({
    fromDad:{
      type:Array,
      required:true
    }
  })
  let obj = ref({
    "title": "",
        "category": "",
        "origin_price": "",
        "price": "",
        "unit": "",
        "image": "",
        "description": "",
        "content": "",
        "is_enabled":"1",
        "imageUrl":""
  });
  let addOrEdit = ref("")


watch(()=>props.fromDad,
  ()=>{
    //console.log(props.fromDad)
    addOrEdit.value = props.fromDad[0]?"add":"edit";
    obj.value = props.fromDad[1]
  })


function sendData(status,data){
  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;
  let url = `${headAPI}/api${myAPI}/admin/product`;
  let method = "post";

  if (status=="edit"){
    method = "put"
    url = `${headAPI}/api${myAPI}/admin/product/${data.id}`;
  }
  
  console.log(method)
  noCatch(axios[method](url,{"data":data})
    .then(res=>{
      //console.log(res.data.success)
      hideModal()
    })
  )

}
function uploadPic(e){
  /*
  目前所有檔案上傳都是透過form <form> 這個表單 
  後端也是針對這些表單做處理
  上傳的檔案 不是字  無法作成表單
  所以使用表單物件  這個表單物件<form>是一樣的東西  只是是表單型態

  先透過  事件物件  取得上傳的圖片
  再使用  表單.append(圖片)  將圖片放進表單裡面
  這樣就成功將圖片上傳

  但還必須將  回傳的圖片網址  和  obj.imgURL 連結
  然後下方顯示圖片  ok拉！
  */ 
  let file = e.target.files[0];
  let form = new FormData();
  form.append("file-to-upload",file);//把file放在name=file-to-upload 標籤裡面
  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;
  let url = `${headAPI}/api${myAPI}/admin/upload`;
  noCatch(axios.post(url,form
  //現代化的chrome不需特地設置header
  // ,{
  //   headers:{
  //     "Content-Type":"multipart/form-data"
  //   }
  // }
  ).then(res=>{
    console.log(res);
    obj.value.imageUrl = res.data.imageUrl;
    console.log(obj.value)
  })
  )
  
}

  
</script>

<template>

  
<div class="modal fade" id="staticBackdrop"  tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-10" id="staticBackdropLabel">{{props.fromDad[0]?"新增資料":"編輯資料"}}</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">

        <div class="wrap">

          <div class="picWrap">
            <div class="insertPic">
              <label for="insertPic">輸入圖片網址
                <input id="insertPic" v-model="obj.imageUrl" type="text">
              </label>
            </div>
            <div class="uploadPic">
              <label for="uploadPic">或 上傳圖片
                <input id="uploadPic" type="file" @change="uploadPic($event)">
              </label>
              <img v-if="obj.imageUrl" :src="obj.imageUrl" width="150" style="margin-top:30px" alt="">
            </div>
          </div>

          <div class="contentWrap">
            <div class="title">
              <label for="title">標題
                <input id="title" v-model="obj.title" type="text">
              </label>
            </div>
            <div class="catagory">
              <label for="catagory">分類
                <input id="catagory" v-model="obj.category" type="text">
              </label>
            </div>
            <div class="unit">
              <label for="unit">單位
                <input id="unit" v-model="obj.unit" type="text">
              </label>
            </div>
            <div class="originPrice">
              <label for="originPrice">原價
                <input id="originPrice" v-model="obj.origin_price" type="text">
              </label>
            </div>
            <div class="price">
              <label for="price">售價
                <input id="price" v-model="obj.price" type="text">
              </label>
            </div>
            <hr>
            <div class="des">
              <label for="des">產品描述
                <textarea id="des" v-model="obj.description" ></textarea>
              </label>
            </div>
            <div class="desContent">
              <label for="desContent">說明內容
                <textarea id="desContent" v-model="obj.content" ></textarea>
              </label>
            </div>
            <input type="checkbox" v-model="obj.is_enabled" :true-value=1 :false-value=0>是否啟用
          </div>
        </div>

      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button @click="sendData(addOrEdit,obj)" type="button" class="btn btn-primary">{{props.fromDad[0]?"送出新增":"送出編輯"}}</button>
      </div>
    </div>
  </div>
</div>
</template>
<style>
  .wrap input{
    width:100%;
  }
  input[type=textarea]{
    display: none;
   
    width:200%;
  }
  .wrap{
    width:100%;
    display:grid;
    gap:20px;
    grid-template-columns:1fr 2fr;
  }
  .picWrap{
    grid-column:1;
  }
  .picWrap>div{
    margin-bottom:10px;
  }
  .contentWrap{
    grid-column:2;
    display:grid;
    gap:10px;
    grid-template-columns:1fr 1fr;
    /* grid-template-rows:1fr 1fr 1fr 1fr 1fr 1fr 1fr; 
    不要亂射1fr 因為這個1fr會依據每一個內容做1fr
    以就是說30 30 100 這樣的內容做1fr 1fr 1fr;
    會變成以100作為1fr 也就是說30會超級空

    使用grid-template-xxx  他媽要記得display:grid

    input[type='text']{
  
  }
    */
  }


  .contentWrap *{
    width:100%;
  }
  .title{
    grid-column:span 2;
    grid-row:1;
    width:100%;
    
  }

  .catagory{
    grid-column:1;
    grid-row:2
  }
  .unit{
    grid-column: 2;
    grid-row:2
  }
  .originPrice{
    grid-column: 1;
    grid-row:3
  }
  .price{
    grid-column: 2;
    grid-row:3
  }

  hr{
    grid-column: span 2;
  }
  .des{
    grid-column: span 2;
  }

  .desContent{
    grid-column:span 2
  }
  textarea{
    width:100%;
  }

</style>