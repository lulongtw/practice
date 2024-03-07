import {createRouter,createWebHashHistory} from "vue-router";

import Login from "@/components/Login.vue";
import FirstPage from "@/components/FirstPage.vue";
import MainArea from "@/components/children/MainArea.vue";

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