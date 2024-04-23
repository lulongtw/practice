<script setup>
import axios from 'axios';
import {ref,onMounted,inject,watch} from "vue";
import {headAPI,myAPI,getData,getDot} from "@/functions.js";
import {useRouter} from "vue-router";
import {Form,Field,ErrorMessage} from "vee-validate";
import * as yup from "yup";

let cartInfo = ref([]);
let couponCode = ref("");
let toggleLoading = inject('toggleLoading')
let showStatus = inject('showStatus');
let data = ref({});
let emits = defineEmits(['couponCng'])

function emailtest(val){
  let ok = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/;
  return ok.test(val)
}
function teltest(val){
  return !isNaN(val)
}
function lengtest(val){
  return String(val).length==8
}

const schema = yup.object().shape({
  name:yup.string().required('需要名字'),
  email:yup.string().required('需要伊妹兒').test('emailtest','不合格伊妹兒',emailtest),
  tel:yup.string().required('需要電話').test('teltest','要數字',teltest).test('lengtest','長度不對',lengtest),
  address:yup.string().required('需要地址'),
  txarea:yup.string()
})

async function useCoupon(){
  toggleLoading()
  let url = `${headAPI}/api${myAPI}/coupon`;
  let method = 'post';
  let toSend = {'data':{'code':couponCode.value}};
  let res = await getData(url,method,toSend);
  if (res.data.success){
    let timeStamp = new Date().getTime()
    showStatus({content:res.data.message,stamp:timeStamp})
  }
  toggleLoading()
  emits('couponCng')
}
async function onSubmit(val){
  toggleLoading()
  let url = `${headAPI}/api${myAPI}/order`;
  let method = 'post';
  let toSend =     {
      "data": {
        "user": {
          "name": data.value.name,
          "email": data.value.email,
          "tel": data.value.tel,
          "address": data.value.address
        },
        "message": data.value.txarea
      }
    };
  let res = await getData(url,method,toSend);
  if (res.data.success){
    console.log(res)
    let timeStamp = new Date().getTime()
    showStatus({content:res.data.message,stamp:timeStamp})
  }
  toggleLoading()
}

</script>
<template>
  <div class="input-group mb-3">
    <input v-model="couponCode" type="text" class="form-control" placeholder="Recipient's username" aria-label="Recipient's username" aria-describedby="button-addon2">
    <button @click="useCoupon" class="btn btn-outline-secondary" type="button" id="button-addon2">Button</button>
  </div>
  <Form :validation-schema="schema" @submit="onSubmit">
    <label for="name">買家名稱
      <Field v-slot="{field,errors}" name="name" v-model="data.name">
        <input type="text" v-bind="field" :class="{'nono':errors.length>0}">
      </Field>
      <ErrorMessage name="name"></ErrorMessage>
    </label>
    <label for="email">伊妹兒
      <Field v-slot="{field,errors}" name="email" v-model="data.email">
        <input type="text" v-bind="field" :class="{'nono':errors.length>0}">
      </Field>
      <ErrorMessage name="email"></ErrorMessage>
    </label>
    <label for="tel">電話
      <Field v-slot="{field,errors}" name="tel" v-model="data.tel">
        <input type="text" v-bind="field" :class="{'nono':errors.length>0}">
      </Field>
      <ErrorMessage name="tel"></ErrorMessage>
    </label>
    <label for="address">地址
      <Field v-slot="{field,errors}" name="address" v-model="data.address">
        <input type="text" v-bind="field" :class="{'nono':errors.length>0}">
      </Field>
      <ErrorMessage name="address"></ErrorMessage>
    </label>
    <label for="">留言
      <Field v-slot="{field,errors}" name="txarea" v-model="data.txarea">
       <textarea v-bind="field"></textarea>
      </Field>
    </label>
    <button>songla</button>
  </Form>
</template>
<style scoped>
  .nono{
    border-color:red;
  }
  input,label,textarea{
    width:100%;
  }
  Form{
    width:min(80%,600px);
    margin:30px auto;
  }
  label{
    margin-bottom:10px;
  }
</style>

