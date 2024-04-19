<script setup>
  import {Form,Field,ErrorMessage} from "vee-validate";
  import * as yup from "yup";

  //檢查目標必須全部用上才會匯出，如果有沒用到的就要刪掉
  //不然即使檢查成功也會無法console
  const schema = yup.object().shape({
    title:yup.string().required('需要名字').test('length','3~8長度',
    (val)=>{
      return String(val).length >=3 && String(val).length <9;
    }),
    emyer:yup.string().email('不合格email').required('需要伊妹兒'),
    nmbr:yup.string().required('需要電話').test('testNum','輸入數字',
      (val)=>{
        return !isNaN(val)
      }
    )
  })
  function onSubmit(val){
    console.log(val)
  }

</script>
<template>
  <Form :validation-schema="schema" @submit="onSubmit">
    <Field name="title" v-slot="{field,errors}">
      <input type="text" v-bind="field" :class="{'nono':errors.length>0}">
      {{errors}}
    </Field>
    <ErrorMessage name="title"></ErrorMessage>
    <hr>
    <Field name="emyer" v-slot="{field,errors}">
      <input type="text" v-bind="field" :class="{'nono':errors.length>0}">
      {{errors}}
    </Field>
    <ErrorMessage name="emyer"></ErrorMessage>
    <hr>
    <Field name="nmbr" v-slot="{field,errors}">
      <input type="text" v-bind="field" :class="{'nono':errors.length>0}">
      {{errors}}
    </Field>
    <ErrorMessage name="nmbr"></ErrorMessage>
    <hr>
    <button></button>
  </Form>

</template>
<style>
  .nono{
    background-color: red;
  }
</style>