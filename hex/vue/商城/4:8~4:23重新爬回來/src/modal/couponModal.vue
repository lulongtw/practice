<script setup>
  import axios from 'axios';
  import {ref,onMounted,inject,watch} from "vue";
  import {headAPI,myAPI,getData,getDot} from "@/functions.js";
  import {Modal} from "bootstrap";
  import * as yup from 'yup';
  import { Form, Field, ErrorMessage } from 'vee-validate';


// 不能亂用.boolean
//button要在form內
//不能在button設submit的click  該click無法submit
//所有schema的name都要用上
//v-model要綁在Field標籤 而不是input標籤 透過Field的v-slot field 屬性傳給input

  let emits = defineEmits(['toDad']);
  let data = ref({});
  let toggleLoading = inject('toggleLoading')
  let showStatus = inject('showStatus')

async function onSubmit(val){
  let target = document.querySelector("#couponModal");
  let modalDOM = Modal.getOrCreateInstance(target);
  modalDOM.hide()
  toggleLoading()
  let url = `${headAPI}/api${myAPI}/admin/coupon`;
  let method = 'post';
  data.value.due_date = new Date(data.value.due_date).getTime()/1000;
  let toSend = {'data':data.value}
  let res = await getData(url,method,toSend);
  if (res.data.success){
    let timeStamp = new Date().getTime();
    showStatus({content:res.data.message,stamp:timeStamp})
  }
  data.value = {}
  toggleLoading()    
  emits('toDad')
  }
  const schema = yup.object().shape({
    title:yup.string().required('必須名稱'),
    code:yup.string().required('必須優惠碼'),
    percent:yup.string().required('必須百分比').test('百分比數字','數字',(val)=>{
      return !isNaN(val)
    }),
    duedate:yup.string().required('必須過期日')

  })

</script>
<template>
  <div class="modal fade" id="couponModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">新增coupon</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <div class="couponWrap">

            <Form :validation-schema="schema" @submit="onSubmit">
            <label for="">標題
              <Field v-slot="{field,errors}" name="title"  v-model="data.title" >
                <input v-bind="field" type="text" :class="['ok',{'nono':errors.length>0}]">
              </Field>
              
          </label>
          <ErrorMessage name="title"></ErrorMessage>
          <label for="">優惠密碼
            <Field v-slot="{field,errors}" name="code"  v-model="data.code">
              <input  v-bind="field" type="text" :class="['ok',{'nono':errors.length>0}]">
            </Field>
          </label>
          <ErrorMessage name="code"></ErrorMessage>
          <label for="">到期日
            <Field v-slot="{field,errors}" name="duedate"  v-model="data.due_date">
              <input  v-bind="field"  type="date" :class="['ok',{'nono':errors.length>0}]">
            </Field>
          </label>
          <ErrorMessage name="duedate"></ErrorMessage>
          <label for="">折扣百分比
            <Field v-slot="{field,errors}" name="percent"  v-model="data.percent">
              <input v-bind="field"  type="text" :class="['ok',{'nono':errors.length>0}]">
            </Field>
          </label>
          <ErrorMessage name="percent"></ErrorMessage>
          <label for="">是否啟用
         
              <input  type="checkbox" v-model="data.is_enabled" true-value="1" false-value="0">

          </label>
    
            <div class="modal-footer">
          <button   class="btn btn-primary">Save changes</button>
          <button @click.prevent=""  class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          </div>

        </Form>
        </div>
 
      </div>

    </div>
  </div>
</div>

</template>
<style scoped>
  input,label{
    width:100%;
  }

  .ok{
    border-color: greenyellow;
  background-color: #eeffe0;
  }
  .nono{
    border-color: red;
  background-color: #ffe0e0;
  }
</style>