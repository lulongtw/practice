import {createRouter,createWebHistory} from "vue-router";
import com1 from "../views/com1.vue";
import com2 from "../views/com2.vue";

const router = createRouter({
  history:createWebHistory(import.meta.env.BASE_URL),
  routes:[
    {
      path:"/",
      component:com1
    },
    {
      path:"/com2",
      component:com2
    }
  ]
});

export default router