import {createRouter,createWebHashHistory} from "vue-router";
import Login from "@/components/Login.vue";
import Dashboard from "@/components/Dashboard.vue";
import Product from "@/components/Product.vue";

const router = createRouter({
  history:createWebHashHistory(),
  routes:[
    {
      path:"/:pathMaytch(.*)*",
      component:Login,
    },{
      path:"/dashboard",
      component:Dashboard,
      children:[
        {
          path:"product",
          component:Product,
          meta:{requiredAuth:true}
        }
      ]
    }
  ]
});

export default router