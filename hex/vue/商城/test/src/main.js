import {createApp} from "vue";

import App from "./App.vue";
import router from "./router";
import store from "@/store/vuex";

let app = createApp(App);
app.use(router)

router.beforeEach((to)=>{
  if (to.path=="/checkOutPage"){
    store.commit("noShowSmallCart")
  }else{
    store.commit("showSmallCart")
  }
})

app.mount("#app")