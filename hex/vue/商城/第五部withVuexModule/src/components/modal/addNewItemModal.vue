<script setup>
import { ref, watch, onMounted } from "vue";
import axios from "axios";
import { Modal } from "bootstrap";

import { noCatch } from "@/assets/functions";
import dealWithProcuct from "@/components/side/dealWithProcuct.vue";

let props = defineProps({
  fromDad: Array,

});

let emit = defineEmits(["callRefresh","isLoading"]);

let act = ref(props.fromDad);
let headAPI = import.meta.env.VITE_headAPI;
let myAPI = import.meta.env.VITE_myAPI;
let data = ref({});
let toDel = ref(false);

//忘記props如果有變動 需要watch觀察
watch(
  () => props.fromDad,
  () => {
    act.value = props.fromDad[0];
    data.value = {...props.fromDad[1]};
    // console.log(act.value);
    toDel.value = act.value == "del" ? true : false;
  }
);
// watch(
//   () => props.item,
//   () => {
//     data.value = props.item;
//     console.log(data.value);
//   }
// );
//忘記要處理依照指令create edit del客製化 Modal 不能用onMOunted
//因為modal跟父組件一開始就onMOunter了 要用watch
// onMounted(()=>{
// })

async function sent() {
  let url;
  let method;
  let modalDom = document.querySelector("#addNewItemModal");
  let modalInstance = Modal.getOrCreateInstance(modalDom);
  modalInstance.hide();
  emit("isLoading")
  switch (act.value) {
    case "create":
      url = `${headAPI}/api${myAPI}/admin/product`;
      method = "post";
      break;
    case "edit":
      url = `${headAPI}/api${myAPI}/admin/product/${data.value.id}`;
      method = "put";
      break;
    case "del":
      url = `${headAPI}/api${myAPI}/admin/product/${data.value.id}`;
      method = "delete";
      break;
  }
    let dataToSend = {data:data.value};
    // data.value = {};
    await noCatch(axios[method](url,dataToSend)
    .then(res=>{
      console.log(res)
    })
    )
  emit("callRefresh");
}
</script>

<template>
  <div
    class="modal fade"
    id="addNewItemModal"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
    tabindex="-1"
    aria-labelledby="staticBackdropLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="staticBackdropLabel">這便要改</h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <dealWithProcuct v-if="!toDel" :fromDad="data"></dealWithProcuct>
          <div v-else>del</div>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
          >
            Close
          </button>
          <button @click="sent()" type="button" class="btn btn-primary">
            Understood
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- <div v-else>
  del
</div> -->
</template>
