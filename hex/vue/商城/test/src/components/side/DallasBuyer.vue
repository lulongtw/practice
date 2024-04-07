<script setup>
  import {useField,useForm,defineRule,configure} from "vee-validate";
  import {email,required} from "@vee-validate/rules";
  import { localize } from '@vee-validate/i18n';


  defineRule("email",email);
  defineRule("required",required);
  defineRule("number",(value)=>{
    let pattern = /^\d+$/;
    return pattern.test(value)
  });
  defineRule("length",(value)=>{
    return value.length==10?true:false
  })
  defineRule("string",(value)=>{
    value = value.split("")
    return value.every(item=>{
      return isNaN(item*1)
    })
  })

  configure({
    generateMessage:localize("zh-tw",{
      messages:{
        required:"必填",
        email:"正確伊媚兒格式",
        number:"輸入數字",
        length:"10位手機號碼",
        string:"名字沒有數字"
      }
    })
  })

  let {handleSubmit} = useForm();
  let {value:nameValue,errorMessage:nameError} = useField("name","required|string");
  let {value:emaluValue,errorMessage:emaluError} = useField("emalu","email|required");
  let {value:telValue,errorMessage:telError} = useField("tel","required|number|length")
  let {value:addressValue,errorMessage:addressError} = useField("address","required");


  let onSubmit = handleSubmit(values=>{
    console.log(values)
  })
</script>
<template>
  <form @submit.prevent="onSubmit">
    <label for="name">大名
      <input v-model="nameValue" :class="['form-control',{'is-invalid':nameError}]" type="text" name="name" id="name">
      <div class="text-danger">{{nameError}}</div>
    </label>
    <label for="emalu">伊妹兒
      <input v-model="emaluValue" :class="['form-control',{'is-invalid':emaluError}]" type="email" name="emalu" id="emalu">
      <div class="text-danger">{{emaluError}}</div>
    </label>
    <label for="tel">手機
      <input v-model="telValue" :class="['form-control',{'is-invalid':telError}]" type="text" name="tel" id="tel">
      <div class="text-danger">{{telError}}</div>
    </label>
    <label for="address">地址
      <input v-model="addressValue" :class="['form-control',{'is-invalid':addressError}]" type="text" name="address" id="address">
      <div class="text-danger">{{addressError}}</div>
    </label>
    <label for="msg">留言
      <textarea name="" id="msg" placeholder="留言"></textarea>
    </label>
    <input type="submit" value = submit>
  </form>
  
</template>

<style scoped>
  form{
    width:100%;
  }
  label{
    margin-bottom:10px;
  }
  label,textarea{
    display: block;
    width: 100%;
  }

</style>