<script setup>
import { useField, useForm, defineRule, configure } from "vee-validate";
import { email, required } from "@vee-validate/rules";
import { localize } from "@vee-validate/i18n";

defineRule('email', email);
defineRule('required', required);
defineRule('allNumber', val => {
  return !isNaN(Number(val)); // 确保输入是数字
});
defineRule('length', val => {
  return val.length >= 3 && val.length <= 7; // 确保长度是3到7位
});

  let {value:nameValue,errorMessage:nameErr} = useField('nam','required|length')
  let {value:emailValue,errorMessage:emailErr} = useField('emyer','required|email');
  let {value:pwValue,errorMessage:pwErr} = useField('pw','required|allNumber');
let { handleSubmit} = useForm();

let onSubmit = handleSubmit(values => {
  console.log(values); // 这将输出所有值
});

configure({
  generateMessage: localize('zh-TW', {
    messages: {
      required: '必填',
      email: "填入正确的邮箱格式",
      allNumber: "输入数字",
      length: "输入3到7位数据"
    },
  }),
});
</script>

<template>
<form @submit.prevent="onSubmit">
  <input type="text" v-model="nameValue" name="nam" :class="{'nono': nameErr}">
  {{ nameErr }}
  <hr>
  <input type="text" v-model="emailValue" name="emyer" :class="{'nono': emailErr}">
  {{ emailErr }}
  <hr>
  <input type="text" v-model="pwValue" name="pw" :class="{'nono': pwErr}">
  {{ pwErr }}
  <input type="submit" value="送出订单">
</form>
</template>

<style>
.nono {
  background-color: red;
}
</style>
