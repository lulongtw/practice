<script setup>
  import {Field,ErrorMessage,Form} from "vee-validate";
  import * as yup from "yup";

  function onSubmit(val){
    console.log(JSON.stringify(val,null,2))
  }
  function check(val){
    if (!val){
      return "要輸入"
    }
    let ok = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/
    return ok.test(val)?true:'不合格'
    // return val.search(ok)!=-1?true:'不合格'
  }
  
  
  const schema = yup.object().shape({
    //yup.第一個必須是決定型態.string() or .number() or .boolean
    email:yup.string().required('給我輸入').email('不合格e04')
  })
</script>
<template>
  <!--name一定要是 和type一樣  少了會缺少動作媽的有夠玄-->
  <Form :validation-schema="schema" @submit="onSubmit">
    <Field name="email" type="email" ></Field>
    <!--是:rules 不是:rule-->
    <!-- <Field name="email" type="email" :rules="check"></Field> -->
    <ErrorMessage name="email"></ErrorMessage>
  </Form>

</template>