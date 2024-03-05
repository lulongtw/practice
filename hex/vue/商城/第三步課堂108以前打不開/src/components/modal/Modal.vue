

<script setup>
import { ref, onMounted, watch, inject } from "vue";
import { Modal } from "bootstrap";
import axios from "axios";

import { noCatch } from "@/assets/functions";

let props = defineProps({
  fromDad: {
    type: Array,
    required: true,
  },
});


let updtResponseLst = inject("updtResponseLst");
let emit = defineEmits(['refresh'])
let data = ref({});
let stats = ref("");
let isLoading = ref(false)

async function sendRequest() {
  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;
  let url = `${headAPI}/api${myAPI}/admin/product`;
  let method = "post";
  let fromSend = data.value;

  switch (stats.value) {
    case "edit":
      url = `${headAPI}/api${myAPI}/admin/product/${data.value.id}`;
      method = "put";
      fromSend.num = 1;
      fromSend.image = "test.testtest";
      break;
    case "delete":
      url = `${headAPI}/api${myAPI}/admin/product/${data.value.id}`;
      method = "delete";
      break;
  }

    await noCatch(
      axios[method](url, { data: fromSend }).then((res) => {
        //console.log(res);
      })
    );

  let modalDOM = document.querySelector("#staticBackdrop");
  let modalInstance = Modal.getOrCreateInstance(modalDOM);
  modalInstance.hide();
  emit("refresh")
}

function uploadFile(e) {
  isLoading.value = true
  let file = e.target.files[0];
  let toSend = new FormData();
  toSend.append("file-to-upload",file);
  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;
  let url = `${headAPI}/api${myAPI}/admin/upload`;
  noCatch(axios.post(url,toSend)
    .then(res=>{
      if (res.data.success){
        console.log(res)
        data.value.imageUrl = res.data.imageUrl;
        isLoading.value = false
      }else{
        let newTime = Date.now();
        let toSend = {
          id:newTime,
          msg:res.data.message
        }
        updtResponseLst(toSend)
      }
    })
  )

}

watch(
  () => props.fromDad,
  () => {
    data.value = { ...props.fromDad[1] };
    stats.value = props.fromDad[0];
  }
);
</script>

<template>
  <!-- Modal -->
  <div
    class="modal fade"
    id="staticBackdrop"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
    tabindex="-1"
    aria-labelledby="staticBackdropLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="staticBackdropLabel">Modal title</h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body" v-if="stats != 'delete'">
          <div class="wrap">
            <div class="picwrap">
              <div class="piclink">
                <label
                  >輸入網址
                  <input type="text" v-model="data.imageUrl" />
                </label>
              </div>
              <div class="uploadpic">
                <label
                  >上傳檔案
                  <i v-if="isLoading" class="fa-solid fa-spinner fa-spin"></i>
                  <input type="file" @change="uploadFile($event)" />
                </label>
                <img v-if="data.imageUrl" :src="data.imageUrl" width="150" alt="">
              </div>

            </div>
            <div class="contentwrap">
              <div class="title">
                <label
                  >標題殺人黨
                  <input type="text" v-model="data.title" />
                </label>
              </div>
              <div class="cate">
                <label
                  >分類帽
                  <input type="text" v-model="data.category" />
                </label>
              </div>
              <div class="unit">
                <label
                  >你哪個單位
                  <input type="text" v-model="data.unit" />
                </label>
              </div>
              <div class="origin">
                <label
                  >原味內褲
                  <input type="text" v-model="data.origin_price" />
                </label>
              </div>
              <div class="price">
                <label
                  >獸性大發
                  <input type="text" v-model="data.price" />
                </label>
              </div>
              <hr />
              <label for="">產品描述</label>
              <textarea v-model="data.description"></textarea>
              <label for="">說明內容</label>
              <textarea v-model="data.content"></textarea>
              <input type="checkbox" v-model="data.is_enabled" />是否啟動
            </div>
          </div>
        </div>
        <div class="modal-body" v-else>你卻</div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
          >
            Close
          </button>
          <button @click="sendRequest()" type="button" class="btn btn-primary">
            宋七力
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<style>
.wrap {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 20px;
}
input {
  width: 100%;
  display: block;
}
.picwrap > * {
  margin-bottom: 20px;
}
.contentwrap {
  grid-column: 2;
  display: grid;
  gap: 10px;
  grid-template-columns: 1fr 1fr;
}
.cate {
  grid-column: 1;
}
.unit,
.price {
  grid-column: 2;
}

.title > label {
  display: inline-block;
  width: 100%;
}
hr,
textarea,
.title {
  grid-column: span 2;
}
</style>
