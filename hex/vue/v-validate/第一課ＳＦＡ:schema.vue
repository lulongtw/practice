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
    email:yup.string().required('給我輸入').email('不合格e04'),
    name:yup.string().required('幹你娘'),
    password:yup.number('數字').required(),
    nickName:yup.string().required('小明必須').test('no_digit','不能有數字',val=>!/\d/.test(val))
    //.string()無法檢查因為html輸入num會被轉成string 所以要手動.test()檢查
    //yup的.test(此test唯一名稱,errormsg,函式返回布林)
    /*
      第一個參數 因為可能會有一堆.test 所以為這個test設名字  就這樣= =
      第二個參數 此.test()不合格時出現的errormsg
      第三個參數  一個布林值  通常由函式返回
    */
 })
</script>
<template>
  <!--name是連結Field 和 ErrorMessage 和 schema裡面的規則的關鍵   type代表引用input的哪個type標籤-->
  <Form :validation-schema="schema" @submit="onSubmit">
    <Field name="email" type="email" ></Field>
    <!--是:rules 不是:rule-->
    <!-- <Field name="email" type="email" :rules="check"></Field> -->
    <ErrorMessage name="email"></ErrorMessage>
    <Field name="name"></Field>
    <ErrorMessage name="name"></ErrorMessage>
    <Field name="password" type="password"></Field>
    <ErrorMessage name="password"></ErrorMessage>
    <Field name="nickName" type="text"></Field>
    <ErrorMessage name="nickName"></ErrorMessage>

       <!--超過一個就他媽一定 必須要button 或是submit的input
    不然成功的話不會出現幹你娘老雞掰-->
    <input type="submit">
    <button>e04</button>
  </Form>

</template>