<script setup>
  import {Form,Field,ErrorMessage} from "vee-validate";
  import * as yup from "yup";


  function onSubmit(val){
    console.log(JSON.stringify(val,null,2))
  }

  let props = defineProps(['fromDad','dadLst']);

</script>
<template>  
dsad  d
  <Form :validation-schema="props.fromDad" @submit="onSubmit">
    <div v-for="item in props.dadLst">
      <Field :name="item" v-slot="{field,errors}">
        <input type="text" v-bind="field" :class="{'nono':errors.length>0}">
      </Field>
      <ErrorMessage :name="item"></ErrorMessage>
    </div>
    <button></button>
  </Form>


</template>
<style>
  .nono{
    background-color: red;
  }
</style>