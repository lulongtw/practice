<script setup>
  import {Form,Field,ErrorMessage} from "vee-validate";
  let props = defineProps({
    fromDad:{
      Object
    }
  })
  function onSubmit(val){
    console.log(JSON.stringify(val,null,2))
  }
</script>
<template>
  <Form @submit="onSubmit">
    <!--注意作為物件傳入  要用{}而不是()
      其實不需要寫這麼多 v-bind:attrs會自動帶入所有鍵值對 = =
      --->
    <div v-for="{name,type,label,...attrs} in props.fromDad.fields">
      <!--label 的for    input 的id  互相響應  沒忘記吧-->
      <label :for="name">{{label}}</label>
      <!--這邊最屌的事v-bind=attrs 很懶-->
      <Field :id="name" :name="name" :type="type" v-bind="attrs"></Field>
       <ErrorMessage :name='name'></ErrorMessage>
    </div>
    <button></button>
  </Form>

</template>