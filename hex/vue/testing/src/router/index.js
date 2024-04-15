

import {createRouter,createWebHashHistory} from "vue-router";
import Dashboard from "@/components/Dashboard.vue";
import ForBuyer from "@/components/ForBuyer.vue";
import ForSeller from "@/components/ForSeller.vue";
import Login from "@/components/Login.vue";

const router = createRouter({
  history:createWebHashHistory(),
  routes:[
    {
      path:"/",
      component:Dashboard,
      children:[
        {
          path:"ForSeller",
          component:ForSeller,
          meta:{requiredAuth:true}
        },
        {
          path:"ForBuyer",
          component:ForBuyer
        }
      ]
    },
    {
      path:"/login",
      component:Login
    },

  ]
});

export default router
