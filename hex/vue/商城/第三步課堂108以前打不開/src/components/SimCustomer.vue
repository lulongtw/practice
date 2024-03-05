<script setup>
import { ref, onMounted,reactive } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
import { Modal } from "bootstrap";

import SeeMoreModal from "@/components/modal/SeeMoreModal.vue";
import Cartlist from "@/components/Cartlist.vue";
import { noCatch } from "@/assets/functions";
import Nono from "@/components/sideComs/Nono.vue"

let isLoading = ref(false)
let simCargoLst = ref([]);
let toSeeMoreModal = ref({});
let nowSelect = ref([]);
let sendtoNono = reactive([])
// let addToCartNowSelect = ref([])

onMounted(() => {
  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;
  let url = `${headAPI}/api${myAPI}/products?page=:page`;
  isLoading.value = true
  noCatch(axios.get(url)
    .then(res => {
      simCargoLst.value = res.data.products;
      isLoading.value = false
    })
  )
});
function seeMore(id) {
  nowSelect.value.push(id)
  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;
  let url = `${headAPI}/api${myAPI}/product/${id}`;
  noCatch(axios.get(url)
    .then(res => {
      if (res.data.success) {
        let idx = nowSelect.value.indexOf(id)
        nowSelect.value.splice(idx,1)
        toSeeMoreModal.value = res.data.product
        let seeMoreDom = document.querySelector("#SeeMoreModal");
        let modalInstance = Modal.getOrCreateInstance(seeMoreDom);
        modalInstance.show()
      }
    })
  )
}

function addToCart(id) {
  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;
  let url = `${headAPI}/api${myAPI}/cart`;
  let toSend = {
    "data": {
      "product_id": id,
      "qty": 1
    }
  }
  noCatch(axios.post(url, toSend)
    .then(res => {
      sendtoNono.push({msg:res.data.message})
    })
  );
}

</script>

<template>
  <div>
    <loading v-model:active="isLoading"/>
    <div class="wrapSim">
      <Nono :res="sendtoNono"></Nono>
      <div class="itemSim" v-for="item in simCargoLst" :key="item.id">
        <div class="picWrapSim" :style="`background-image:url(${item.imageUrl})`"></div>
        <div class="contentWrapSim">
          <div class="titleSim">{{ item.title }}</div>
          <div class="categorySim">{{ item.category }}</div>
          <div class="contentSim">{{ item.content }}</div>
          <div class="originSim">{{ item.origin_price }}</div>
          <div class="priceSim">{{ item.price }}</div>
          <div class="butnWrapSim">
            <div class="seeMoreSim" @click="seeMore(item.id)">
              <i v-if="nowSelect.includes(item.id)" class="fa-solid fa-spinner fa-spin"></i>
              查看更多
            </div>
            <div class="addToCartSim" @click="addToCart(item.id)">
     
              加到購物車
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <SeeMoreModal :fromDad="toSeeMoreModal"></SeeMoreModal>
  <hr>
  <Cartlist></Cartlist>
</template>

<style scoped>
@import "@/assets/SimCustomer.css";
</style>
  