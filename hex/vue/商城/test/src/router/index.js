import {createRouter,createWebHashHistory} from "vue-router";

import Login from "@/components/Login.vue";
import FirstPage from "@/components/FirstPage.vue";
import MainArea from "@/components/children/MainArea.vue";
import CheckOutPage from "@/components/children/CheckOutPage.vue";

const router = createRouter({
  history:createWebHashHistory(),
  routes:[
    {
      path:"/",
      component:FirstPage,
      children:[
        {
          path:"mainArea",
          component:MainArea
        },{
          path:"checkOutPage",
          component:CheckOutPage
        }
      ]
    },
    {
      path:"/login",
      component:Login
    }
  ]
})

export default router