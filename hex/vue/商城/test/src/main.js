import {createApp} from "vue";
import axios from "axios";
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/css/index.css';

import router from "./router";
import App from "./App.vue";
import {noCatch} from "./assets/functions"

axios.defaults.withCredentials = true ; 
//開啟axios 向後端的request Headers 夾帶token
//這token是伺服器端接收登入資訊後 回傳的加密訊息
//訊息可以讓伺服器辨認出我是登入的人

let app = createApp(App);

app.use(router);

app.component("Loading",Loading)

//要ａｓｙｎｃ否則會先跳轉在回到login
router.beforeEach( async (to)=>{
  if (to.meta.requiredAuth){
    let headAPI = import.meta.env.VITE_headAPI;
    let url = headAPI + "/api/user/check"
    await noCatch(axios.post(url)
      .then(res=>{
        if (!res.data.success){
          router.push("/")
        }
      })
    )
  }
})



app.mount("#app")
