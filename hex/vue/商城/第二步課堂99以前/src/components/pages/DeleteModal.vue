<script setup>
  import axios from "axios";
  import {noCatch} from "@/assets/function";
  import {Modal} from "bootstrap";

  let props = defineProps({
    fromDad:{
      type:Object,
      required:true
    }
  })
  


  function deleteData(){
    let headAPI = import.meta.env.VITE_headAPI;
    let myAPI = import.meta.env.VITE_myAPI;
    let id = props.fromDad.id;
    let url = `${headAPI}/api${myAPI}/admin/product/${id}`;
    noCatch(axios.delete(url)
      .then(res=>{
       // console.log(res.data.success)
      })
    );
    let modalDOM = document.querySelector("#deleteModal");
    let modalInstance = Modal.getOrCreateInstance(modalDOM);
    modalInstance.hide()
  }
</script>

<template>


<!-- Modal -->
<div class="modal fade" id="deleteModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="staticBackdropLabel">刪除資料</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        確定刪除此筆資料?
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">算了</button>
        <button @click="deleteData()" type="button" class="btn btn-primary">刪除</button>
      </div>
    </div>
  </div>
</div>

</template>