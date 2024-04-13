import {createRouter,createWebHashHistory} from "vue-router";
import com1 from "@/com1.vue";
import com2 from "@/com2.vue";

const router = createRouter({
  history:createWebHashHistory(),
  linkActiveClass:'act',
  box:"/com1",
  routes:[
    {
      path:"/com1",
      component:com1
    },{
      name:"com2",
      path:"/com2/:id",
      component:com2
    }
  ]
});

export default router