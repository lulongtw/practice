<script setup>
  import {useForm,useField,defineRule,configure} from "vee-validate";
  import {email,required} from "@vee-validate/rules";
  import {ref,inject} from "vue";
  import axios from "axios";
  import { localize } from '@vee-validate/i18n';
  import {useRouter} from "vue-router"

  import {noCatch} from "@/assets/functions";

  defineRule("email",email);
  defineRule("required",required);
  defineRule('number', (value) => {
    let pattern =  /^\d+$/;
    return pattern.test(value)
  });
  defineRule("length",(value=>{
    return String(value).length>=3 && String(value).length<=10 ? true:false
  }))


configure({
  // Generates an English message locale generator
  generateMessage: localize('zh-tw', {
    messages: {
      required: '必填',
      email:"填入正確伊妹兒格式",
      number:"輸入數字",
      length:"輸入3到8位資料"
    },
  }),
});

  let {handleSubmit} = useForm();
  let {value:userNameValue,errorMessage:userNameError} = useField("userName","required|length");
  let {value:emailValue,errorMessage:emailError} = useField("email","email|required");
  let {value:telValue,errorMessage:telError} = useField("number","required|number|length");
  let {value:addressValue,errorMessage:addressError} = useField("address","required");
  // let {value:remarkValue} = useField("remark")
  let remarkValue = ref("");
  let addToStack = inject("addToStack");
  let emits = defineEmits(["sendOrderList"]);
  let router = useRouter();

  let headAPI = import.meta.env.VITE_headAPI;
  let myAPI = import.meta.env.VITE_myAPI;

  let onSubmit = handleSubmit(values=>{
    let url = `${headAPI}/api${myAPI}/order`;
    let dataToSend = {"data":{
      "user":values,
      "message":remarkValue.value
    }}
    noCatch(axios.post(url,dataToSend)
      .then(res=>{
        addToStack(res.data.message)
        let inputs = document.querySelectorAll("input");
        if (res.data.success){
          inputs.forEach(item=>{
            item.value = null;
          });
          emits("sendOrderList")
          router.push(`/dashboard/pay/${res.data.orderId}`)
        }
      })
    )
  })
</script>

<template>
  <form @submit.prevent="onSubmit">
    <label for="userName">買家名稱
      <input type="text" id="userName" name="userName" v-model="userNameValue" :class="['form-control',{'is-invalid':userNameError}]">
      <div class="text-danger">{{userNameError}}</div>
    </label>
    <label for="email">伊妹兒
      <input type="email" id="email" name="email" v-model="emailValue" :class="['form-control',{'is-invalid':emailError}]">
      <div class="text-danger">{{emailError}}</div>
    </label>
    <label for="tel">電話
      <input type="text" id="tel" name="tel" v-model="telValue" :class="['form-control',{'is-invalid':telError}]">
      <div class="text-danger">{{telError}}</div>
    </label>
    <label for="address">地址
      <input type="text" id="address" name="address" v-model="addressValue" :class="['form-control',{'is-invalid':addressError}]">
      <div class="text-danger">{{addressError}}</div>
    </label>
    <label for="remark">留言
      <br>
      <textarea name="remark" v-model="remarkValue" id="remark" ></textarea>
    </label>
    <br>
    <input type="submit" value="送出訂單">
  </form>
</template>

<style scoped>
form{
  width:80%;
  margin:30px auto;
}
  label{
    display:block;
    margin-bottom:10px;
  }
  textarea{
    width:100%;
  }
</style>