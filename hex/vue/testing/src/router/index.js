import {createRouter,createWebHashHistory} from "vue-router";
import Login from "@/components/Login.vue";
import Dashboard from "@/components/Dashboard.vue";
import Seller from "@/components/Seller.vue";
import Buyer from "@/components/Buyer.vue";

const router = createRouter({
  history:createWebHashHistory(),
  routes:[
    {
      path:"/",
      component:Dashboard,
      children:[
        {
          path:"seller",
          component:Seller,
          meta:{requiredAuth:true}
        },{
          path:"buyer",
          component:Buyer
        }
      ]
    },{
      path:"/login",
      component:Login
    }
  ]
});

export default router