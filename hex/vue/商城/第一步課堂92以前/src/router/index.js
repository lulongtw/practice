import {createRouter, createWebHashHistory} from "vue-router";
import Dashboard from "../components/pages/Dashboard.vue";
import Index from  "../components/pages/Index.vue";
import Login from  "../components/pages/Login.vue";

const router = createRouter({
  history:createWebHashHistory(),
  routes:[
    {
      path:"/",
      components:{
        view1:Dashboard
      }
    },
    {
      path:"/login",
      components:{
        view1:Login
      }
    },
    {
      path:"/index",
      components:{
        view1:Index
      },
      meta:{
        requiredAuth:true
       
      }
    }
  ]
});

export default router