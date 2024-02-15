<script setup>
import axios from "axios";
import { ref, onMounted, computed } from "vue";

import { noCatch, getDot } from "@/assets/functions";
import { Modal } from "bootstrap";
import ModalCom from "./modal/Modal.vue";
import Pagination from "./sideComs/Pagination.vue";


let data = ref({});
let pagination = ref({})

let doWhat = ref("");
let newItem = ref({});
let isLoading = ref(false);



function dealWithModal(status, item) {
  doWhat.value = status;
  newItem.value = item;
  let modalDOM = document.querySelector("#staticBackdrop");
  let modalInstance = Modal.getOrCreateInstance(modalDOM);
  modalInstance.show();
}

async function getData(page = 1) {
  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;
  let url = `${headAPI}/api${myAPI}/admin/products?page=${page}`;
  isLoading.value = true
  await noCatch(
    axios.get(url).then((res) => {
      data.value = res.data.products;
      pagination.value = res.data.pagination;
      // console.log(pagination.value)
      isLoading.value = false

    })
  );
}


onMounted(() => {
  getData()
});
</script>
<template>
  <div>
    <loading v-model:active="isLoading" />
    <div class="right mt-4">
      <button class="btn btn-primary" @click="dealWithModal('add', {})">
        建立新產品
      </button>
    </div>

    <table class="table mt-4">
      <thead>
        <th width="120">分類</th>
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
            <td width="100" class="right">{{ getDot(item.origin_price) }}</td>
            <td width="100" class="right">{{ getDot(item.price) }}</td>
            <td width="100">{{ item.is_enabled ? "啟用" : "未啟用" }}</td>
            <td width="140">
              <button @click="dealWithModal('edit', item)" class="btn btn-outline-primary btn-sm">
                編輯
              </button>
              <button @click="dealWithModal('delete', item)" class="btn btn-outline-danger btn-sm">
                刪除
              </button>
            </td>
          </tr>
        </template>
      </tbody>
    </table>
  </div>
  <Pagination :fromDad="pagination" @goToPage="getData"></Pagination>
  <ModalCom :fromDad="[doWhat, newItem]" @refresh="getData"></ModalCom>
</template>

<style>
@import "@/assets/dashboard.scss";
</style>
