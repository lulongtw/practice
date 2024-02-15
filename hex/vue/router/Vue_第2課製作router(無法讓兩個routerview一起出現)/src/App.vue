<template>
    <div>
        <!--
         我無法使兩者view同時出現在畫面上
        -->
        fasff
        <h1>This is App.vue</h1>
      <RouterLink to="/component1">main</RouterLink>
      <RouterLink to="/component2">foot</RouterLink>
      <br>
      <RouterLink to="/component3">a</RouterLink>
      <RouterLink to="/component4">b</RouterLink>
      <RouterLink to="/component5">c</RouterLink>
      <hr>

        第一view
        <br>
        <RouterView name="view1" v-slot="{Component}">
          <KeepAlive>
            <component :is="Component"></component>
          </KeepAlive>
        </RouterView>
     
   
      <hr>
        第二view
        <br>
        <RouterView name="view2" v-slot={Component}>
          <KeepAlive>
            <component :is="Component"></component>
          </KeepAlive>
        </RouterView>

       
  



    </div>
    </template>
  
  <script setup>
  import { RouterLink, RouterView } from 'vue-router';
  import { KeepAlive } from 'vue';


  </script>
  
  <style scoped>
    *{
        margin:10px;
    }
  </style>
