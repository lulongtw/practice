import {createRouter,createWebHashHistory} from "vue-router";
import Login from "@/components/Login.vue";
import Dashboard from "@/components/Dashboard.vue";
import Products from "@/components/Products.vue";
import SimCustomer from "@/components/SimCustomer.vue";
import Coupon from "@/components/Coupon.vue";
import Orderlist from "@/components/Orderlist.vue"

const router = createRouter({
  history:createWebHashHistory(),
  routes:[
    {
      path:"/:pathMatch(.*)*",
      component:Login
    },
    {
      path:"/dashboard",
      component:Dashboard,
      children:[
        {
          path:"products",
          component:Products,
          meta:{
            requiredAuth:true
          }
        },
        {
          path:"orderlist",
          component:Orderlist,
          meta:{
            requiredAuth:true
          }
        },
        {
          path:"coupon",
          component:Coupon,
          meta:{
            requiredAuth:true
          }
        },
        {
          path:"simCustomer",
          component:SimCustomer
        }
      ]
    }
  ]
})

export default router