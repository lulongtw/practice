<script setup>
  import {ref,onMounted,watch,inject} from "vue";
  import {headAPI,myAPI,getData} from "@/functions.js";
  import {useRouter} from "vue-router";
  import {Modal} from "bootstrap";
  
  let props = defineProps(['fromDad']);
  let emits = defineEmits(['callDad']);
  let data = ref(props.fromDad);
  let delView = ref(false);
  let modalTitle = ref("");
  let picUrl = ref("");
  let act = ref("");
  let showStatus = inject('showStatus');

 

  watch(()=>props.fromDad,
    (newVal)=>{
      act.value = newVal[0]
      switch (newVal[0]){
        case 'add':
          modalTitle.value = '新增商品'
          delView.value = false
          data.value = {}
          break
        case "del":
        modalTitle.value = '刪除商品'
          delView.value = true;
          data.value = newVal[1];
          break
          case "edit":
          modalTitle.value = '編輯商品'
          delView.value = false
          data.value = newVal[1]
      }
    }
  );

  async function dealWith(){
    let url;
    let toSend;
    let method
    switch (act.value){
      case 'add':
        url = `${headAPI}/api${myAPI}/admin/product`;
        toSend = {'data':data.value};
        method = 'post'
        break
      case "del":
        url = `${headAPI}/api${myAPI}/admin/product/${data.value.id}`;
        toSend = {'data':data.value};
        method = 'delete'
        break
      case "edit":
        url = `${headAPI}/api${myAPI}/admin/product/${data.value.id}`;
        toSend = {'data':data.value};
        method = 'put'
 
    }
    //console.log(toSend)
    let res = await getData(url,method,toSend);
   // console.log(res)
    let timeStamp = new Date().getTime();

    showStatus({content:res.data.message,stamp:timeStamp})
    let modalId = document.querySelector("#modal3in1");
    let modalDOM = Modal.getOrCreateInstance(modalId);
    emits('callDad')
    modalDOM.hide();
  }

  let spin = ref(false)
  async function uploadFile(e){
    //console.log(e.target.files)
    spin.value = true
    let file = e.target.files[0];
    let form = new FormData();
    form.append("file-to-upload",file);

    let url = `${headAPI}/api${myAPI}/admin/upload`;
    let res = await getData(url,'post',form);
    //console.log(res);
    if (res.data.success){
      data.value.imageUrl = res.data.imageUrl
    }
    spin.value = false
  }


</script>

<template>
<!-- Button trigger modal -->


<!-- Modal  v-model="item.title"  v-model="item.imageUrl" -->
<div class="modal fade" id="modal3in1" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">{{modalTitle}}</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      
      <div v-if="!delView" class="modal-body">
       
          <div class="modalWrap">
        <div class="picWrap">
          <div class="picUrl">
            <label>
              <div>輸入圖片網址</div>
              <input type="text" v-model="data.imageUrl">
            </label>
          </div>
          <div class="uploadPic">
            <label>
              <div>或上傳圖片</div>
              <input @change="uploadFile($event)" type="file" >
            </label>
            <div v-if="spin"><i class="fa-solid fa-spinner fa-spin"></i></div>
            <img v-else :src="data.imageUrl"/>
          </div>
        </div>
        <div class="wordWrap">
          <div class="title">
            <label>
              <div>名稱</div>
              <input type="text" v-model="data.title">
            </label>
          </div>
          <div class="category">
            <label>
              <div>分類</div>
              <input type="text" v-model="data.category">
            </label>
          </div>
          <div class="unit">
            <label>
              <div>分類</div>
              <input type="text" v-model="data.unit">
            </label>
          </div>
          <div class="originPrice">
            <label>
              <div>原價</div>
              <input type="text" v-model="data.origin_price">
            </label>
          </div>
          <div class="price">
            <label>
              <div>售價</div>
              <input type="text" v-model="data.price">
            </label>
          </div>

          <div class="description">
            <label>
              <div>產品描述</div>
              <textarea name="" id="" v-model="data.description"></textarea>
            </label>
          </div>

          <div class="content">
            <label>
              <div>說明內容</div>
              <textarea name="" id="" v-model="data.content"></textarea>
            </label>
          </div>
        </div>
       
        </div>
        <label class="enabled">
          <input type="checkbox" v-model="data.is_enabled"  >啟動狀態
        </label>
        
      </div>
      <div v-else class="modal-body">
        你確定要刪除??
      </div>
      <div class="modal-footer"> 
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button @click="dealWith" v-if="!delView" type="button" class="btn btn-primary">Save changes</button>
        <button @click="dealWith" v-else type="button" class="btn btn-primary">del items</button>
      </div>
    </div>
  </div>
</div>
</template>
<style scoped>
  .modalWrap{
    padding:15px;
    display:flex;
    gap:30px;
    margin:0 auto;
  }
  .picWrap{
    width:30%;
   
  }
  img{
    margin-top:10px;
  }
  .wordWrap{
    width:70%;

  }
  .wordWrap{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:10px;
  }
  .modalWrap label,input,textarea{
    width:100%;
  }
  .title,content,.description,.content{
    grid-column:span 2
  }

  .enabled{
    display:flex;
  }
  .enabled>input{
    width:30px;
  }
  img{
    width:100%;
  }
</style>