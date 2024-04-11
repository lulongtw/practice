import {createRouter,createWebHashHistory} from "vue-router";
import com1 from "@/views/com1.vue";
import com2 from "@/views/com2.vue";

const router = createRouter({
  history:createWebHashHistory(),
  box:"/com1",
  linkActiveClass:"active",
  routes:[
    {
      path:"/com1",
      component:com1
    },{
      name:"/com2",
      path:"/com2/:id",
      component:com2
    }
  ]
});

export default router