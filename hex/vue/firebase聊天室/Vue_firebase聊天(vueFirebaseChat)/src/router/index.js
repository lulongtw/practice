import {createRouter,createWebHistory} from "vue-router";
import Com1 from "../views/com1.vue";
import Com2 from "../views/com2.vue"


const router = createRouter({
    history:createWebHistory(import.meta.env.BASE_URL),
    routes:[
        {
            path:"/",
            component:Com1
        },
        {
            path:"/com2",
            component:Com2
        }
    ]
})

export default router