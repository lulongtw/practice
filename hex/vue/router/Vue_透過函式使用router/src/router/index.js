import {createRouter,createWebHashHistory} from "vue-router";
import com1 from "../views/com1.vue";


const router = createRouter({
  history:createWebHashHistory(),
  routes:[
    { name:'com',
      path:"/com/:id",
      components:{
        view1:com1
      }
    }
  ]
});

export default router