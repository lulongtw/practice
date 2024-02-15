import {createRouter,createWebHashHistory} from "vue-router";
import Login from "@/components/pages/Login.vue";
import Dashboard from "@/components/pages/Dashboard.vue";
import Index from "@/components/pages/Index.vue";
import Products from "@/components/pages/Products.vue";

const router = createRouter({
  history:createWebHashHistory(),
  routes:[
    {
      path:"/",
      component:Dashboard
    },
    {
      path:"/login",
      component:Login
    },
    {
      path:"/index",
      component:Index,
      children:[
        {
          path:"products",
          component:Products,
          meta:{
            requiredAuth:true
          }
        }
      ]
    }
  ]
});

export default router