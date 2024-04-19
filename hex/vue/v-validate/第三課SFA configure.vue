<script setup>
  import {Form,Field,ErrorMessage,configure} from "vee-validate";
  import * as yup from "yup";
  
  function onSubmit(val){
    console.log(JSON.stringify(val,null,2))
  }
  //v-validate是在下列hook進行檢查
  //如果 validateOnInput: true 就會輸入時一直檢查
  //configuare針對全域Field設定
  //以可以針對個別標籤設定
  //給他們新增:validateOnXxxxx = 布林 就可以 
  //如下面這個例子  name 等到輸入完才反應  email只要輸入後沒達標就報錯
  configure({
  validateOnBlur: true, // controls if `blur` events should trigger validation with `handleChange` handler
  validateOnChange: true, // controls if `change` events should trigger validation with `handleChange` handler
  validateOnInput: false, // controls if `input` events should trigger validation with `handleChange` handler
  validateOnModelUpdate: true, // controls if `update:modelValue` events should trigger validation with `handleChange` handler
});
const schema = yup.object().shape({
  name:yup.string().required('needname').min(10,'name bigger than 10'),
  email:yup.string().email('email超級連動').required('need email')
})
</script>
<template>
  <Form :validation-schema="schema" @submit="onSubmit">
    <Field name="name"></Field>
    <ErrorMessage name="name"></ErrorMessage>

<Field name="email" :validateOnBlur="false" :validateOnChange="false" :validateOnInput="true" />
  <ErrorMessage name="email"></ErrorMessage>    
<button></button>
  </Form>

</template>