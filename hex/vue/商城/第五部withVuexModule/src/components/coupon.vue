<script setup>
  import axios from "axios";
  import {ref,onMounted,inject,computed} from "vue";

  import {noCatch} from "@/assets/functions";
  import {modalAct} from "@/assets/functions";
  import addCouponModal from "@/components/modal/addCouponModal.vue";
  import store from "@/store/vuex";


  // let data = ref([]);
  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;
  let isLoading = ref(false);
  let editId = ref("");
  let editData = ref({});
  let addToStack = inject("addToStack");
  // let data = ref([]);
  let data = computed(()=>{
    return store.state.couponStore.couponData
  })

  onMounted(()=>{
     refreshCoupon()
  });

  

  function refreshCoupon(){
    //store.commit("isLoadingStore/toggleLoading");
    let url = `${headAPI}/api${myAPI}/admin/coupons?page=:page`;
    store.dispatch("fetchCouponListData",url);
    //store.commit("toggleLoading");
    // await noCatch(axios.get(url)
    //   .then(res=>{
    //     if (res.data.success){
    //       isLoading.value = false
    //       data.value = res.data.coupons;
    //     }
    //   })    
    // )
  }
  function editCoupon(item){
    editId.value = item.id;
    editData.value.title = item.title;
    editData.value.is_enabled = item.is_enabled;
    editData.value.due_date = new Date(item.due_date*1000).toISOString().split("T")[0];
    editData.value.percent = item.percent;
  }
  async function sendEditedCoupon(id){
    isLoading.value = true;
    editId.value = "noId"
    let url = `${headAPI}/api${myAPI}/admin/coupon/${id}`;
    console.log( editData.value.due_date)
    editData.value.due_date = new Date(editData.value.due_date)/1000
    let dataToSend = editData.value;
    await noCatch(axios.put(url,{"data":dataToSend})
      .then(res=>{
        if (res.data.success){
          addToStack(res.data.message);
          refreshCoupon()
        }
      })
    )
  }

  async function deleCoupon(id){
    isLoading.value = true;
    let url = `${headAPI}/api${myAPI}/admin/coupon/${id}`;
    await noCatch(axios.delete(url)
      .then(res=>{
        if (res.data.success){
          addToStack(res.data.message);
          refreshCoupon()
        }
      })
    )

  }


</script>

<template>
  <div class="couponWrap">
    <button @click="modalAct('show','addCouponModal')" type="button" class="btn btn-primary">新增coupon</button>
  <table>
    <thead>
      <th>名稱</th>
      <th>折扣</th>
      <th>到期日</th>
      <th>啟用狀態</th>
      <th>編輯</th>
    </thead>
    <tbody>
      <template v-for="(item,idx) in data" :key="item.id">
        <tr v-if="editId==item.id">
          <td><input type="text" v-model="editData.title"></td>
          <td><input type="text" v-model="editData.percent"></td>
          <td><input type="date" v-model="editData.due_date"></td>
          <td><input type="checkbox" v-model="editData.is_enabled" :true-value="1" :false-value="0">{{editData.is_enabled?"已啟用":"未啟用"}}</td>
          <td><button @click="sendEditedCoupon(item.id)" type="button" class="btn btn-primary">send</button></td>
        </tr>
        <tr v-else>
          <td>{{item.title}}</td>
          <td>{{item.percent}}</td>
          <td>{{new Date(item.due_date*1000).toISOString().split("T")[0]}}</td>
          <td>{{item.is_enabled?"已啟用":"未啟用"}}</td>
          <td>
            <button @click="editCoupon(item)" type="button" class="btn btn-primary">edit</button>
            <button @click="deleCoupon(item.id)" type="button" class="btn btn-secondary">dele</button>
          </td>
        </tr>
      </template>
    </tbody>
  </table>
  </div>

  <addCouponModal @sendNewCoupon="refreshCoupon"></addCouponModal>

</template>
<style scoped>

  td:nth-of-type(2)>input{
    width:70px;
    text-align: center;
  }
  td:nth-of-type(1)>input,td:nth-of-type(3)>input{
    width:100%;
    text-align: center;
  }

  
</style>



