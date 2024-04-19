<script setup>
  import {useForm,useField,defineRule,configure} from "vee-validate";
  //以下兩個import 都要npm install
  import {localize} from "@vee-validate/i18n";//把文字變成各國語言
  import {required,email} from "@vee-validate/rules"//輸入現成的rule

  let {handleSubmit} = useForm()
  //這要最先let 不能比 useField下面 ＝＝ 會抓不到 黑人問號
  let onSubmit = handleSubmit(val=>{
    console.log(JSON.stringify(val,null,2))
  })


  //此為vee-validate的方法 無法引入yup
  //要使用yup 需直接在form中引入yup的scheme
  defineRule('email',email);//引入現成rule
  defineRule('required',required);
  defineRule('length',(val)=>{//自訂rule
    return String(val).length>=3 && String(val).length <6
  })
  defineRule('onlyNum',(val)=>{
    return !isNaN(val)
  });

  //核心部分
  //建立 檢查對象的名字(emyer) 的value 與 errorMessage  以及 檢查規則
  let {value:emailVal,errorMessage:emailErr} = useField('emyer','email|required')
  let {value:numVal,errorMessage:numErr} = useField('num','required|length|onlyNum')


  //這行直接在官網找
  configure({
  generateMessage: localize('zh-tw', {
    messages: {
      required: '必須輸入',//當不符此規則時出現的錯誤訊息
      email:'不合email',
      length:'不和長度',
      onlyNum:'只有數字'
    },
  }),
});
</script>
<template>
  <form @submit.prevent="onSubmit">
    <!--引入v-model以響應取得值 並在class檢查響應錯誤-->
    <input type="text" name="emyer" v-model="emailVal" :class="{'nono':emailErr}">
    {{emailErr}}
    <hr>
    <input type="text" name="num" v-model="numVal" :class="{'nono':numErr}">
    {{numErr}}
    <button></button>
  </form>

</template>
<style>
  .nono{
    background-color: red;
  }
</style>