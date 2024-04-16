import {createApp} from 'vue';
import App from "@/App.vue";
import router from "./router";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.css"

axios.defaults.withCredentials = true;

let app = createApp(App);

router.beforeEach(async(to)=>{
  if (to.meta.requiredAuth){

    let headAPI = import.meta.env.VITE_headAPI;
    let url = headAPI + "/api/user/check";
 //   console.log(url)
    await axios.post(url).then(
      res=>{
        if (!res.data.success){
          router.push("/login")
        }
      }
    )
  }
})

app.use(router);

app.mount("#app")