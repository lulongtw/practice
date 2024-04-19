<script setup>
import { Form, Field, ErrorMessage } from "vee-validate";
import * as yup from "yup";

// 定义验证规则
//結果他媽問機器人一下就出來了
//前面都一樣  到template才不一樣
const schema = yup.object().shape({
  name: yup.string().required('必須')
});

function onSubmit(values) {
  console.log(values);
}
</script>

<template>
  <Form :validation-schema="schema" @submit="onSubmit">
    <!-- 使用作用域插槽来动态添加类 
      在Field標籤添加name引入規則  與v-slot提供插入資料
      Field內部input 接收filed和 errors
      errors 就是這個檢察單位(name)有幾個錯誤訊息
    -->
    <Field name="name" v-slot="{ field, errors }">
      <input
        :class="{'nono': errors.length > 0}"
        v-bind="field"
      />
      <ErrorMessage name="name" />
      {{errors}}
    </Field>
    <button type="submit">提交</button>
  </Form>
</template>

<style>
.nono {
  background-color: red;
}
</style>
