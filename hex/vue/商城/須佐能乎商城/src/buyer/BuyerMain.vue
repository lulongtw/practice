<script setup>
  import {ref,watch,computed,onMounted} from "vue";
  import store from "@/store/store.js";
  
  import Jumbo from "@/side/Jumbo.vue";
  import Category from "@/side/Category.vue";
  import Products from "@/side/Products.vue";

  let data = ref(store.state.allProducts);
  let allProducts = ref({})
  let currentCategory = ref("衣服")
  let cartNum = ref(0)

  onMounted(()=>{   
    let url = `/api/:api_path/products/all`
    let method = 'get';
    store.dispatch('fetchAllProducts',{url,method})
  })

  watch(()=>store.state.allProducts,
    (newVal)=>{
      data.value = newVal.products;
      data.value.forEach(item=>{
        if (!allProducts.value[item.category]){
          allProducts.value[item.category] = [];
        }
        allProducts.value[item.category].push(item)
      })
      console.log(allProducts.value)
    }
  )


</script>

<template>
  <header>
    <div><i class="fa-solid fa-paw"></i>肥狗超商</div>
    <div class="cart">
      <i class="fa-solid fa-cart-shopping"></i>
      {{cartNum}}
    </div>
  </header>
  <aside>
    <Jumbo></Jumbo>
  </aside>
  <main>
      <div class="category">
        <Category></Category>
      </div>
      <div class="productsArea">
        <Products></Products>
      </div>
    </main>
  <footer>
    <div>© Copright 2017 六角血拼賣賣  Instagrame  Facebook About</div>
    <div>Made with Bootstrap5</div>
  </footer>


</template>
<style scoped>


</style>