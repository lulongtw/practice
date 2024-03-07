<script setup>
import { ref, onMounted, computed } from "vue";

import categoryNav from "@/components/side/CategoryNav.vue";
import pagination from "@/components/side/Pagination.vue";
import itemColumn from "@/components/side/ItemColumn.vue";
import store from "@/store/vuex.js";

let headAPI = import.meta.env.VITE_headAPI;
let myAPI = import.meta.env.VITE_myAPI;
let currentCategory = ref("");

let allProducts = computed(() => {
  //不能store.state.AllProducts.data.products 直接探查 好像在哪課學過
  if (store.state.AllProducts.length) {
    store.commit("hideLoading");
    return store.state.AllProducts;
  } else {
    store.commit("showLoading");
  }
});

let categories = computed(() => {
  if (store.state.AllProducts.length) {
    let list = [];
    store.state.AllProducts.forEach((item) => {
      if (
        !list.some((listItem) => {
          return listItem == item.category;
        })
      ) {
        list.push(item.category);
      }
    });
    currentCategory.value = list[0];
    return list;
  }
});

onMounted(() => {
  let url = `${headAPI}/api${myAPI}/products/all`;
  let payload = ["get", url];
  store.dispatch("getAllProducts", payload);
});

function changeShow(item) {
  currentCategory.value = item;
}
</script>

<template>
  <div class="jumboTron">
    <div class="p-5 mb-4 bg-body-tertiary rounded-3">
      <div class="container-fluid py-5">
        <h1 class="display-5 fw-bold">肥狗敲讚賣場五告讚</h1>
        <p class="col-md-8 fs-4">
          福利熊　熊福利 福利熊　熊福利 福利熊　熊福利 福利熊　熊福利 one two
          福利 one two 福利 happy 　everyday ~♪ one two 福利 one two 福利
        </p>
      </div>
    </div>
  </div>
  <main>
    <div class="categoryNav">
      <categoryNav
        :data="categories"
        :currentShow="currentCategory"
        @changeCategory="changeShow"
      ></categoryNav>
    </div>
    <div class="itemColumn">
      <itemColumn
        :data="allProducts"
        :currentShow="currentCategory"
      ></itemColumn>
      <div class="pagination">
        <pagination></pagination>
      </div>
    </div>
  </main>
</template>

<style scoped>
main {
  height: auto;
  display: flex;
  padding: 30px 50px;
  gap: 30px;
}

.categoryNav {
  width: 30%;
}

.itemColumn {
  width: 70%;
}
</style>
