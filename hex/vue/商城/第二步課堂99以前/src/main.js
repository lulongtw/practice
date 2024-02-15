import {createApp} from "vue";
import "bootstrap";
import axios from "axios";
import router from "./router";
import App from "./App.vue";
import {noCatch} from "./assets/function.js";

axios.defaults.withCredentials = true;

let app = createApp(App);

router.beforeEach( async(to)=>{
  if(to.meta.requiredAuth){
    let headAPI = import.meta.env.VITE_headAPI;
    let url = headAPI + "/api/user/check";
    await noCatch(axios.post(url)
      .then(res=>{
       // console.log(res)
        if(!res.data.success){
          router.push("/")
        }
      })
    )
  }
})

app.use(router);
app.mount("#app")