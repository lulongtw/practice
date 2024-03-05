<script setup>
  import {useRouter} from "vue-router";
  import {ref,onMounted} from "vue";
  import axios from "axios";
  import {noCatch} from "@/assets/functions"

  let data = ref({})
  let router = useRouter();
  let checkBox = ref(false)

  function signIn(){
    if (checkBox.value){
      let toLocal = JSON.stringify({...data.value});
      localStorage.setItem("saveItem",toLocal)
    }
    let headAPI = import.meta.env.VITE_headAPI;
    let myAPI  =import.meta.env.VITE_myAPI;
    let url = headAPI+"/admin/signin";
    noCatch(axios.post(url,data.value))
    .then(res=>{
      if (res.data.success){
      //如果帳號密碼ok 
      //就取得server回傳的token與expired
      //並把他們做成cookie
      //最後再跳頁  因為在跳頁前  必須先做好餅乾
      //在跳頁時才能axios才能在送出請求時夾帶cookie
      //要在那邊夾帶呢  就在最外層的app.vue 因為他是最外增的組件
        let token = res.data.token;
        let expired = res.data.expired;
        document.cookie = `beforeShootingToken=${token};expires=${expired}`
        router.push("/dashboard/product")
      }else{
        console.log(res.data.message)
      }
    })
  }
  onMounted(()=>{
    let fromLocal = localStorage.getItem("saveItem");
    if (fromLocal){
      fromLocal = JSON.parse(fromLocal)
      data.value = {...fromLocal}
    }
  })

</script>

<template>

  <body class="d-flex align-items-center py-4 bg-body-tertiary">    
<main class="form-signin w-100 m-auto">
  <form @submit.prevent="signIn()">
 <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

    <div class="form-floating">
      <input v-model="data.username" type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
      <label for="floatingInput">Email address</label>
    </div>
    <div class="form-floating">
      <input v-model="data.password" type="password" class="form-control" id="floatingPassword" placeholder="Password">
      <label for="floatingPassword">Password</label>
    </div>

    <div class="form-check text-start my-3">
      <input v-model="checkBox" class="form-check-input" type="checkbox"  id="flexCheckDefault">
      <label class="form-check-label" for="flexCheckDefault">
        Remember me
      </label>
    </div>
    <button class="btn btn-primary w-100 py-2" type="submit">Sign in</button>
    <p @click="router.push('/dashboard')" class="mt-5 mb-3 text-body-secondary">按我進dashboard</p>
    <p class="mt-5 mb-3 text-body-secondary">&copy; 2017–2023</p>
  </form>
</main>
</body>
</template>

<style>
  @import "@/assets/Login.scss";

</style>