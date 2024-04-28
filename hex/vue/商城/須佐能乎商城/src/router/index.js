import {createRouter,createWebHashHistory} from "vue-router";
import BuyerMain from "@/buyer/BuyerMain.vue";
import SellerMain from "@/seller/SellerMain.vue";
import Login from "@/seller/Login.vue";

const router = createRouter({
  history:createWebHashHistory(),
  routes:[
    {
      path:"/",
      component:BuyerMain
    },{
      
      path:"/sellerMain",
      component:SellerMain,
      meta:{requiredAuth:true}
    },{
      path:'/login',
      component:Login
    }

  ]
});

export default router