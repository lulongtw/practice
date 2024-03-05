<script setup>
  import axios from "axios";
  import {ref,onMounted,inject} from "vue";


  import {noCatch} from "@/assets/functions";
  import {modalAct} from "@/assets/functions";

  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;
  let coupon = ref({});
  let addToStack = inject("addToStack");
  let emits = defineEmits(["sendNewCoupon"])


  async function addNewCoupon(){
    let url = `${headAPI}/api${myAPI}/admin/coupon`;
    let dataToSend = coupon.value;
    dataToSend.due_date = Math.floor(new Date(dataToSend.due_date)/1000);
    modalAct("hide","addCouponModal")
    await noCatch(axios.post(url,{"data":dataToSend})
      .then(res=>{
        if(res.data.success){
          console.log(res.data.message);
          addToStack(res.data.message);
          emits("sendNewCoupon");
        }
      })
    )
    coupon.value = {}
  }

</script>
<template>
  <div class="couponWrap">
    <div class="modal fade" id="addCouponModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">新增優惠碼</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <label>標題
            <input type="text" v-model="coupon.title">
          </label>
          <label>優惠碼
            <input type="text" v-model="coupon.code">
          </label>
          <label>到期日
            <input type="date" v-model="coupon.due_date">
          </label>
          <label>折扣百分比
            <input type="text" v-model="coupon.percent">
          </label>
          <label>
            <input type="checkbox" v-model="coupon.is_enabled" :true-value="1" :false-value="0">
            使否啟用
          </label>
    
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button @click="addNewCoupon()" type="button" class="btn btn-primary">新增優惠碼</button>
        </div>
      </div>
    </div>
  </div>
  </div>


</template>

<style scoped>
  .couponWrap{
    width:70%;
    margin:50px auto;
  }
  input{
    width:100%;
    margin-bottom:10px;
  }
  label{
    display: block;

  }
  input[type='checkbox']{
    display: inline-block;
    width:30px;

  }
</style>