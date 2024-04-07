<script setup>
  import {onMounted,computed,ref,watch} from "vue";

  import store from "@/store/vuex";
  import checkOutCartsTable from "@/components/side/CheckOutCartsTable.vue";
  import dallasBuyer from "@/components/side/DallasBuyer.vue"


  let finalTotal = ref(0);
  let showTable = ref(true)
  //用computed的資料傳props進子組件 子組件的props也是響應式????
  let allCarts = computed(()=>{
    finalTotal.value = store.state.AllCarts.reduce((accumulator,currentItem)=>{
      return accumulator+currentItem.final_total
    },0)
    return store.state.AllCarts
  })
  //第一步
  //要在其他函式內取得dom元素 必須先let變數 意思是在create階段就let此變數為全域變數
  //這樣函式才能onMounterd後被復職的dom元素
  //dom元素只能在onMounted階段之後取得
  let checkOutTable
  let height
  onMounted(()=>{
    checkOutTable = document.querySelector(".checkOutTable");
    //取得最初cartsTable的高度
    height = getComputedStyle(checkOutTable).getPropertyValue("height");
    //進入函式 將cartsTable高度設為0
    toggleShowTable()
  })

  //第二步
  function toggleShowTable(){
    //因為showTable一開始是true onMounted進入此函式將showTable變成flase
    //意思是一開始取得height變數 然後馬上將cartsTable的高度變成0
    showTable.value = !showTable.value;
    if (showTable.value){
      checkOutTable.style.height = height
    }else{
      checkOutTable.style.height = "0px"
    }
  }
  //第三步
  //監控ALLcarts
  //一有變動  將cartsTable高度設為auto 讓他自動符合內容
  //再取得他自動符合後的高度
  //這邊刊起來很白痴 但是應該必要的吧?
  //因為沒有這邊 height無法重設 變成toggleShowTable時 cartTable的height依然是一開始的高度
  //變成空白很多
  //那有笨蛋就把toggleShowTable的true情況變"auto" 靠杯那就不能transition了啊
  //所以就是這樣
  //然後這變用setTimeOut是因為好像有時間問題
  //沒有setTimeout 第一次delete會追蹤不到 高度依然是一開始的高度
  //就是註解那個//console.log(height)
  watch(()=>store.state.AllCarts,
    ()=>{
      setTimeout(()=>{
        checkOutTable.style.height = "auto"
        height = getComputedStyle(checkOutTable).getPropertyValue("height");
        checkOutTable.style.height = height;
        //console.log(height)
      },10)
    }
  )


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
        <dallasBuyer></dallasBuyer>
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
