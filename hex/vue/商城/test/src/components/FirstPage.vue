<script setup>

import {useRouter} from "vue-router";
import {onMounted,computed,ref} from "vue";

import store from "@/store/vuex"

let router = useRouter();
let headAPI = import.meta.env.VITE_headAPI;
let myAPI = import.meta.env.VITE_myAPI;

let showingSmallCartStatus = computed(()=>{
  return store.state. smallCartShowing
})

onMounted(()=>{
  let url = `${headAPI}/api${myAPI}/cart`
  let payload2 = ["get",url];
  store.dispatch("getAllCart",payload2);
  router.push("/mainarea");
});
let showingCartList = ref(false)


let allCarts = computed(()=>{
  return store.state.AllCarts;
})
function showSmallCartList(){
  showingCartList.value = !showingCartList.value
}
function deleteProductFromCarts(id){
  // let url = `${headAPI}/api${myAPI}/cart/${id}`;
  // let payload = ["delete",url];
  // store.dispatch("deleteProductFromCarts",payload)
  store.dispatch("deleteProductFromCarts",id)
  store.dispatch("getAllCart")
}
</script>

<template>
  <header>
    <div class="topping">
      <div class="firstPageNav"><i class="fa-solid fa-paw"></i>肥狗超商</div>
      <div v-show="showingSmallCartStatus" class="currentCart">
        <button @click.prevent="showSmallCartList()" type="button" class="btn btn-light">
          <div class="cartpic"><i class="fa-solid fa-cart-shopping"></i></div>
          <div class="digit">{{allCarts.length}}</div>
        </button>
      </div>
      <div v-if="showingCartList" class="smallCartList">
        <div>    購物車內商品</div>
            <table>
              <tr v-if="!allCarts.length">
                無商品
              </tr>
              <template v-for="(item,idx) in allCarts">
                <tr>
                  <td @click="deleteProductFromCarts(item.id)"><i class="fa-solid fa-trash"></i></td>
                  <td>{{item.product.title}}</td>
                  <td>{{item.qty}}{{item.product.unit}}</td>
                  <td>${{item.final_total}}元</td>
                </tr>
              </template>
            </table>
            <div @click="router.push(`/checkOutPage`);showingCartList = false" class="checkOutButton"><i class="fa-solid fa-paw"></i> 結帳去</div>
          </div>
    </div>
  </header>
  <router-view></router-view>
  <footer>
    <div class="copyright">
      © Copright 2017 六角血拼賣賣
      <i class="fa-brands fa-instagram"></i> Instagrame
      <i class="fa-brands fa-facebook"></i> Facebook About
    </div>
    <div class="mathWith">Made with Bootstrap4</div>
  </footer>
</template>

<style scoped>
@import "@/assets/style.scss";
@import "@/assets/firstPage.scss";
</style>
