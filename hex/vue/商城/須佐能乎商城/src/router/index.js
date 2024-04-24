import {createRouter,createWebHashHistory} from "vue-router";
import BuyerMain from "@/buyer/BuyerMain.vue";

const router = createRouter({
  history:createWebHashHistory(),
  routes:[
    {
      path:"/",
      component:BuyerMain
    }

  ]
});

export default router