<script setup>
  import {ref,watch} from "vue";
  import {Modal} from "bootstrap";

  let props = defineProps(['fromDad'])
  let data = ref({});
  let act = ref('')

  watch(()=>props.fromDad,
    (newVal)=>{
      act.value = newVal.act,
      data.value = newVal.data;
    })

</script>
<template>
  <div class="modal fade" id="couponModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">{{act}}</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <div class="couponWrap">
          <label for="">標題
            <input type="text" v-model="data.title">
          </label>
          <label for="">優惠密碼
            <input type="text" v-model="data.code">
          </label>
          <label for="">到期日
            <input type="date" v-model="data.due_data">
          </label>
          <label for="">折扣百分比
            <input type="text" v-model="data.percent">
          </label>
        </div>
 
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>

</template>