import {createRouter,createWebHistory} from "vue-router";
import com1 from "../views/com1.vue"
import com2 from "../views/com2.vue";




const router = createRouter({
  history:createWebHistory(),
  routes:[
    {
      path:"/",
      components:{
        view1:com1
      }
    },
    {
      name:'com',
       path:"/com/:id",
      components:{
        view1:com2
      }
    }
  ]
});

export default router