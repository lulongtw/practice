<script setup>
  import axios from "axios";
  import {ref,onMounted} from "vue";
  import {useRouter} from "vue-router";
  let router = useRouter();
  
  let checkBox = ref(false)
  let userData = ref(  {
    "username": "",
    "password": ""
  });

  function send(){
    let headAPI = import.meta.env.VITE_headAPI;
    let url = headAPI+"/admin/signin";

    if (checkBox.value){
      let toLocal = JSON.stringify(userData.value);
      localStorage.setItem("remItem",toLocal);
    }
    
    axios.post(url,userData.value)
    .then(res=>{
      //如果帳號密碼ok 
      //就取得server回傳的token與expired
      //並把他們做成cookie
      //最後再跳頁  因為在跳頁前  必須先做好餅乾
      //在跳頁時才能axios才能在送出請求時夾帶cookie
      //要在那邊夾帶呢  就在最外層的app.vue 因為他是最外增的組件
      if (res.data.success){
        let token = res.data.token;//取得server回傳的token
        let expired = res.data.expired;
        document.cookie = `newToken=${token};expires=${new Date(expired)}`//做成餅乾
        router.push("/Index")
      }
    }).catch(res=>{
      console.error("shit",res)
    })
  }

  onMounted(()=>{
    if (localStorage.getItem("remItem")){
      let fromLocal = JSON.parse(localStorage.getItem("remItem"));
      userData.value = {...fromLocal}//淺複製  第二層會傳參考
      //直接複製值  不會傳參考
      // userData.value.username = fromLocal.username;
      // userData.value.password = fromLocal.password;
    }
  })

</script>

<template>
    
    <main class="form-signin w-100 m-auto">
  <form @submit.prevent="send()">
 <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

    <div class="form-floating">
      <input type="email" v-model="userData.username" class="form-control" id="floatingInput" placeholder="name@example.com">
      <label for="floatingInput">Email address</label>
    </div>
    <div class="form-floating">
      <input type="password" v-model="userData.password" class="form-control" id="floatingPassword" placeholder="Password">
      <label for="floatingPassword">Password</label>
    </div>

    <div class="form-check text-start my-3">
      <input @click="console.log(checkBox)" class="form-check-input" type="checkbox" v-model="checkBox" id="flexCheckDefault">
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
@import "/Users/lulong/Desktop/hello/HTML/hex/vue/test/src/assets/style.scss";
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