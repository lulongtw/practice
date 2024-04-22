<script setup>
  import axios from 'axios';
  import {ref,onMounted,inject,watch} from "vue";
  import {headAPI,myAPI,getData,getDot} from "@/functions.js";
  import {Modal} from "bootstrap";
  import * as yup from 'yup';
  import { Form, Field, ErrorMessage } from 'vee-validate';


// 不能亂用.boolean
//不能在button設submit的click
//所有schema的name都要用上

  let emits = defineEmits(['toDad']);
  let data = ref({});


 function onSubmit(val){
    // let url = `${headAPI}/api${myAPI}/admin/coupon`;
    // let method = 'post';
    // data.value.due_date = new Date(data.value.due_date).getTime()/1000;
    // console.log(data.value);
    // let target = document.querySelector("#couponModal");
    // let modalDOM = Modal.getOrCreateInstance(target);
    // data.value = {}
    // console.log('g')
    console.log('val',val);
    console.log('data.value',data.value);


    data.value = {}
    document.querySelectorAll("#couponModal input").forEach(input => {
      // console.log(input)
  if (input.type === 'checkbox') {
    input.checked = false;
  } else {
    input._value = '';
    console.dir(input)
  }
});

  
    
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
              <Field v-slot="{field,errors}" name="title">
                <input v-bind="field" type="text" v-model="data.title">
                {{errors}}
              </Field>
              
          </label>
          <ErrorMessage name="title"></ErrorMessage>
          <label for="">優惠密碼
            <Field v-slot="{field,errors}" name="code">
              <input  v-bind="field" type="text" v-model="data.code">
            </Field>
          </label>
          <ErrorMessage name="code"></ErrorMessage>
          <label for="">到期日
            <Field v-slot="{field,errors}" name="duedate">
              <input  v-bind="field"  type="date" v-model="data.due_date">
            </Field>
          </label>
          <ErrorMessage name="duedate"></ErrorMessage>
          <label for="">折扣百分比
            <Field v-slot="{field,errors}" name="percent">
              <input v-bind="field"  type="text" v-model="data.percent">
            </Field>
          </label>
          <ErrorMessage name="percent"></ErrorMessage>
          <label for="">是否啟用
         
              <input  type="checkbox" v-model="data.is_enabled" true-value="1" false-value="0">

          </label>
    
          <!-- <button  @click.prevent="sendNewCoupon" ></button> -->
          <button   class="btn btn-primary">Save changes</button>
          <!-- <div class="modal-footer">
        <button @click.prevent=""  class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button @click.prevent="onSubmit"  class="btn btn-primary">Save changes</button>
      </div> -->
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
  label{

  }
</style>