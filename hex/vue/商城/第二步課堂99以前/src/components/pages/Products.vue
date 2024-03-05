<script setup>
import axios from "axios";
import { Modal } from 'bootstrap';//新東西
import { ref, onMounted,watch } from "vue";
import { noCatch } from "@/assets/function";
import ModalCom from "@/components/pages/ModalCom.vue";
import DeleteModal from "@/components/pages/DeleteModal.vue";

let data = ref({});

let writeData = ref({});
let isNew = ref(false)
let delData = ref({})

onMounted(() => {
  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;
  let url = `${headAPI}/api${myAPI}/admin/products?page=:page`;
  noCatch(
    axios.get(url).then((res) => { 
      data.value = res.data.products;
    // console.log(res)
    })
  );
});





let showing = ref(false);
//modal是一種從畫面中彈跳而出的另一個新視窗
//行為通常會將原本瀏覽的畫面變暗變淡  讓用戶集中注意力到新視窗身上
//通常用在用戶繳交資料或者確認以及資料提示等用途

//而bootastape也有提供現成的modal
//可以透過標籤呼叫modal
//如下
//在按鈕標籤中設置 data-bs-toggle=modal data-bs-target="modal名稱"  這兩種屬性
//在modal選手中設置 id="modal名稱" 屬性
//按下按鈕即modal彈跳而出

//但有時候不只有click事件 會需要modal出線
//取得資料後也可以 這樣就沒有標籤可以click觸發
//所以要透過bootstrap的js函式觸發
//如下 
//首先import bootstrap的 modal 函式
//在取得modal 的DOM元素 
//然後使用modal.getOrCreateInstance(modalDOM元素)方法 取得modal實例
//modal實例.show() 出現

// watch(showing, (newVal) => {
//   let modalElement = document.getElementById('staticBackdrop');
//   //下面這叫modal實例 什麼鬼
//   let modalInstance = Modal.getOrCreateInstance(modalElement); // 获取或创建 Modal 实例
//   modalInstance.show();
// });

function writeOnModal(isnew,data){
  let modalDom = document.querySelector("#staticBackdrop");
  let modalInstance = Modal.getOrCreateInstance(modalDom);
  modalInstance.show();
  isNew.value = isnew;
  writeData.value = data
}

function deleteItem(item){
  // console.log(item)
  let modalDOM = document.querySelector("#deleteModal");
  let modalInstance = Modal.getOrCreateInstance(modalDOM);
  delData.value = item
  modalInstance.show()
}

</script>

<template>
  <div>
    <div class="right mt-4">
      <button class="btn btn-primary" @click=" writeOnModal(true,{})" >建立新產品</button>
    </div>
   
    <table class="table mt-4">
      <thead>
        <th  width="120">分類</th>
        <th width="150">產品名稱</th>
        <th width="100">原價</th>
        <th width="100">售價</th>
        <th width="80">啟用狀態</th>
        <th width="80">編輯</th>
      </thead>
      <tbody>
        <template v-for="(item, key) in data" :key="item.id">
          <tr>
            <td width="120">{{ item.category }}</td>
            <td width="150">{{ item.title }}</td>
            <td width="100" class="right">{{ item.origin_price }}</td>
            <td width="100" class="right">{{ item.price }}</td>
            <td width="100">{{ item.is_enabled ? "啟用" : "未啟用" }}</td>
            <td width="140">
              <button @click=" writeOnModal(false,item)" class="btn btn-outline-primary btn-sm">編輯</button>
              <button @click="deleteItem(item)" class="btn btn-outline-danger btn-sm">刪除</button>
            </td>
          </tr>
        </template>
      </tbody>
    </table>
  </div>
  <!--在這邊引入Modal html-->
  <ModalCom :fromDad="[isNew,writeData]"></ModalCom>
  <DeleteModal :fromDad="delData"></DeleteModal>
</template>

<style>
.right {
  text-align: right;
}
thead>th{
  text-align:center
}
thead>*,tr>*{
  padding:0 10px;
  background-color:red;
}
td:nth-child(odd){
  /* color:red ; */
  
  /* background-color:rgb(0, 4, 255) !important; */
}
td:nth-child(even){
  /* background-color:green !important; */
}
td{
  padding:0 30px !important;
  border-right:1px solid rgb(222, 222, 222)  !important;
}
td:last-of-type{
  text-align: center;
  padding:0 !important;

}
td:last-of-type>button{
  margin:0 5px;
}
</style>
