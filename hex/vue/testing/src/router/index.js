import {createRouter,createWebHashHistory} from "vue-router";
import com1 from "@/com1.vue";
import com2 from "@/com2.vue";

const router = createRouter({
  history:createWebHashHistory(),
  base:"/com2",
  linkActiveClass:"qq",
  // linkActiveClass:"active",
  routes:[
    {
      path:"/com1",
      component:com1
    },{
      path:"/com2",
      component:com2
    }
  ]
});

export default router