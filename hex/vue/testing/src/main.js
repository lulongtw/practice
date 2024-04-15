import App from "@/App.vue";
import "bootstrap/dist/css/bootstrap.css";
import router from "./router";
import {createApp} from "vue";
import axios from "axios";
import {noCatch} from "@/function.js"

axios.defaults.withCredentials = true;
let app = createApp(App);

app.use(router)
router.beforeEach(async(to)=>{
   if(to.meta.requiredAuth){
    let headAPI = import.meta.env.VITE_headAPI;
    let api = headAPI + "/api/user/check";
    await noCatch(axios.post(api).then(res=>{
      if (!res.data.success){
        router.push("/")
      }
    }))
  }
})


app.mount("#app")