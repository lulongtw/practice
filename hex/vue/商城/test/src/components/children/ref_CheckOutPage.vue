
<script setup>
//此組件沒有用 只是將allcarts變成ref 用watch和onMounted取得
//媽的下面行為全都不一樣
//還沒修完懶得修 靠杯
  import {onMounted,computed,ref,watch} from "vue";

  import store from "@/store/vuex";
  import checkOutCartsTable from "@/components/side/CheckOutCartsTable.vue"


  let finalTotal = ref(0);
  let showTable = ref(true)
  let allCarts = ref([])


  watch(()=>store.state.AllCarts,
    ()=>{
      if (store.state.AllCarts.length){
        allCarts.value = store.state.AllCarts;
        checkOutTable.style.height = "auto";
        height = getComputedStyle(checkOutTable).getPropertyValue("height");
      }
    }
  ) 
  

  let checkOutTable
  let height
  onMounted(()=>{
    allCarts.value = store.state.AllCarts
    checkOutTable = document.querySelector(".checkOutTable");
    console.log(checkOutTable)
    setTimeout(()=>{
      height = getComputedStyle(checkOutTable).getPropertyValue("height");
    },10)

  })


  function toggleShowTable(){

    showTable.value = !showTable.value;
    if (showTable.value){
      checkOutTable.style.height = height
    }else{
      checkOutTable.style.height = "0px"
    }
  }



</script>
<template>

  <div class="checkOutPageWrap">
    <header>
      <div>肥狗旺旺結帳</div> 
    </header>
    <aside>
      <div class="showStatus">1.輸入買家資料</div>
      <div class="showStatus">2.給我錢</div>
      <div class="showStatus">3.謝謝給我錢</div>
    </aside>
    <main>
      <div class="cartInfo">
        <div @click="toggleShowTable()" class="showCartList">
            顯示購物車內容
        </div>
        <div class="finalTotal"> {{finalTotal}}</div>
      </div>
      <!-- <transition name="slide"> -->
        <div class="checkOutTable">
          <checkOutCartsTable  :cartList="allCarts" ></checkOutCartsTable>
        </div>
      <!-- </transition> -->
      <div class="dallasBuyer">
        v-validate的地方
      </div>
      <button type="button" class="btn btn-success">Success</button>
      <button type="button" class="btn btn-danger">Danger</button>
    </main>
  </div>
</template>

<style scoped>
  .checkOutPageWrap{
    width:80%;
    margin:30px auto;
    padding:20px;
  
  }
  header{
    width:100%;
    font-size: 25px;
    color:gray;
    text-align: center;
    
  }
  aside{
    display:flex;
    width:100%;
    gap:5px;
    justify-content: space-evenly;
    
  }
  .showStatus{
    width:30%;
    padding:10px 30px;
    background-color: rgb(143, 198, 143);
  }
  .cartInfo{
    width:55%;
    margin:30px auto;
    background-color: gray;
    display:flex;
    justify-content: space-between;
    padding:10px;
  }
  .showCartList{
    color:blue;

  }
  .finalTotal{
    font-weight: 800;
    font-size:20px;
  }
  .checkOutTable{
  
    /* height:0px; */
    transition: max-height 0.3s ease-in-out,height 0.3s ease-in-out ;
    overflow: hidden;
  }
  .checkOutTable--active {
    max-height: 1000px; 
}

/* .slide-enter-active, .slide-leave-active {
  transition: opacity  0.5s;
}

.slide-enter-from, .slide-leave-to {
  opacity: 0;
} */
</style>