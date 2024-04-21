<script setup>
  import {Form,Field,ErrorMessage} from "vee-validate";
  import * as yup from "yup";
  import App1 from "@/App1.vue"

  /*
  這個屌了
  組件對傳
  然後還可以響應class
  重點是要傳兩個props進子組件
  一個是schema 不需變
  schema一樣在Form :validation-schema發會作用

  另一個是需要迭代的name
  重點就是那個name
  有了name 規則就可以透過field放在input上面
  透過props傳進Form裡面的div來迭代name
  Field有了name就可以取得schema裡面的rule

  透過dadLst 應該也可以傳遞其他資訊 例如input type=radio這種
  */

  function checklength(val){
    return String(val).length >3 && String(val).length <=7;
  }
  function noNum(val){
    return isNaN(val);
  }
  function noStr(val){
    return !isNaN(val);
  }
  function onSubmit(val){
    console.log(JSON.stringify(val,null,2))
  }

  let lst = ['nam','emyer','pw'];
  const schema = yup.object().shape({
    //使用多個.test()為同一個name加上多個規則
    //同時在.test內部引入函式 以重複使用
    nam:yup.string().test('namlength','不和長度',checklength).test('noNum','不能有數字',noNum),
    emyer:yup.string().email('醜email').required('要有email'),
    pw:yup.string().test('pwlength','不和長度',checklength).test('noStr','不能文字',noStr)
  })
</script>
<template>                
  <App1 :fromDad="schema" :dadLst="lst"></App1>
</template>
<style>
  .nono{
    background-color: red;
  }
</style>