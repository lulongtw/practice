import {createRouter,createWebHashHistory} from "vue-router";
import com1 from "@/views/com1.vue"
import com2 from "@/views/com2.vue";
/*
這節課上 router裡面的 mode,base,linkActiveClass 屬性

mode:
分為history模式和hash模式
卡屎伯說用createWebHashHistory比較安全
因為history會跟後端打架
但我們在寫程式的時候不用加上#
差別只差在輸入createWebHashHistory而已

base:
router的根目錄 預設為"/"
如果routerLink是掛載在box下面
則要用base:"/box"


linkActiveClass
當RouterLink被點擊時
vue自動會給被點擊到的RouterLink一個className
有預設值router-link-active 又長又難聽
使用這個屬性更改

*/ 



const router = createRouter({
  base:"/box",
  history:createWebHashHistory(),
  linkActiveClass:"active",
  routes:[
    {
      path:"/box",
      components:{
        view1:com1
      }
    },
    {
       path:"/com2",
      components:{
        view1:com2
      }
    }
  ]
});

export default router