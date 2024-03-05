<script setup>
  import axios from "axios";
  import {ref} from "vue";
  import {Modal} from "bootstrap";

  import {noCatch} from "@/assets/functions";
  import CouponModal from "@/components/modal/CouponModal.vue"

  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;
  let couponLstLoading = ref(false);
  let data = ref([])
  function getData(){
    couponLstLoading.value = true
    let url = `${headAPI}/api${myAPI}/admin/coupons?page=:page`;
    noCatch(axios.get(url)
      .then(res=>{
        if (res.data.success){
          couponLstLoading.value = false;
          data.value = res.data.coupons
        }
      })
    )
  }

  function addCoupon(){
    let modalDOM = document.querySelector("#CouponModal");
    let modalInstance = Modal.getOrCreateInstance(modalDOM);
    modalInstance.show()

  }

</script>

<template>
    <div>
      <div>
        <button @click="getData()">refresh Coupon List</button>
        <div @click="addCoupon()">新增</div>
      </div>
   

    <i v-if="couponLstLoading" class="fa-solid fa-spinner fa-spin"></i>
    <div v-else class="CouponListWrap">
      <table>
        <thead>
          <th>名稱</th>
          <th>折扣百分比</th>
          <th>到期日</th>
          <th>是否啟用</th>
          <th>編輯</th>
        </thead>
        <!-- <Nono :res="sendtoNono"></Nono> -->
        <tbody>
          <tr v-for="item in data">
            <td>{{item.title}}</td>
            <td>{{item.prcent}}</td>
            <td>{{item.due_date}}</td>
            <td>{{item.is_enabled===1?"啟用":"為啟用"}}</td>
            <td><button class="btn btn-primary">編輯</button></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <CouponModal></CouponModal>
</template>

<style>

</style>