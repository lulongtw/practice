<script setup>
  import { ref } from 'vue';
  import { Form, Field, ErrorMessage } from 'vee-validate';

  const props = defineProps({
    fromDad: Object, 
    dadLst: Array
  });
  // 初始化data为一个响应式对象，其键是由props.dadLst动态生成
  const data = ref(props.dadLst.reduce((acc, key) => {
    acc[key] = '';
    return acc;
  }, {}));

 
  function onSubmit() {
    console.log(data.value);
    // 清空数据
    Object.keys(data.value).forEach(key => {
      data.value[key] = '';
    });
  }
</script>

<template>
  <Form :validation-schema="props.fromDad" @submit="onSubmit">
    <div v-for="item in props.dadLst" :key="item">
      <Field :name="item" v-slot="{ field, errors }">
        <input type="text" v-model="data[item]" v-bind="field" :class="{'nono': errors.length > 0}">
      </Field>
      <ErrorMessage :name="item"></ErrorMessage>
    </div>
    <button type="submit">Submit</button>
  </Form>
</template>

<style>
  .nono {
    background-color: red;
  }
</style>
