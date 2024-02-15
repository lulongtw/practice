<script setup>
  import {useRouter} from "vue-router";
  import {ref,onMounted} from "vue";
  import axios from "axios";
  import {noCatch} from "/Users/lulong/Desktop/hello/HTML/hex/vue/商城/test/src/assets/function.js"

  let userData = ref({
    username:"",
    password:""
  });
  let router = useRouter();
  let checkBox = ref(false);

  onMounted(()=>{
    if (localStorage.getItem("nextItem")){
      let fromLocal = JSON.parse(localStorage.getItem("nextItem"))
      userData.value = {...fromLocal}
    }
  })


  function send(){
    let headAPI = import.meta.env.VITE_headAPI;
    let url = headAPI+"/admin/signin";
    if (checkBox.value){
      let toLocal = JSON.stringify(userData.value);
      localStorage.setItem("nextItem",toLocal)
    }
    noCatch(axios.post(url,userData.value)

      .then(res=>{
      
        if (res.data.success){
        //  console.log(res.data)
          let token = res.data.token;
          let expired = res.data.expired;
          document.cookie = `nextToken=${token};expires=${new Date(expired)}`;
          router.push("/index/products")
        }else{
          console.log("登入台西掰")
        }
      })
    )
  }
</script>

<template>
<main class="form-signin w-100 m-auto">
  <form @submit.prevent="send()">
    <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

    <div class="form-floating">
      <input v-model="userData.username" type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
      <label for="floatingInput">Email address</label>
    </div>
    <div class="form-floating">
      <input v-model="userData.password" type="password" class="form-control" id="floatingPassword" placeholder="Password">
      <label for="floatingPassword">Password</label>
    </div>

    <div class="form-check text-start my-3">
      <input v-model="checkBox" class="form-check-input" type="checkbox"  id="flexCheckDefault">
      <label class="form-check-label" for="flexCheckDefault">
        Remember me
      </label>
    </div>
    <button class="btn btn-primary w-100 py-2" type="submit">Sign in</button>
    <p class="mt-5 mb-3 text-body-secondary">&copy; 2017–2023</p>
  </form>
</main>
</template>

<style>
  @import "@/assets/style.scss";
  html,
body {
  height: 100%;
}

.form-signin {
  max-width: 330px;
  padding: 1rem;
}

.form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

</style>