//2.router資料夾裡的index.js

/*
router資料夾就是放index.js 不要吵
import createRouter製作router
import createWebHistory製作history

建立router要素
history:router指定位置有兩種，一種是hash# 另一種是webhistory 也就是/ 

routes:內容為由物件組成的序列
其物件必須有兩種屬性:path 和components
path代表和外部RouterLink被點擊到時相對應激活的對象
components:代表當我點擊到path時 這些組件都會被渲染到畫面上
也可以使用name屬性  當作另一種導航方式

但是！！
要渲染到哪裡!
當點擊到特定path時，
router檢查router內部的routes
查找到一樣的path  檢查裡面的components選項
看要啟動哪些view 把view的組件們渲染到畫面上


routerView也可以巢狀
巢狀的概念跟網頁也是一樣一層一層的包裹/index/main/item1....
這個概念在com4.vue裡面的 router-link 的to='/com2/child2' 可以看到
代表導航到com2下的child2 
此時 router 開始從com2的children
查找path 為/com2的物件
再找com2物件裡面 path 為child2的的物件 的children 屬性

這個children 和routes一樣  是一個序列
找到children 裡面path屬性為child2的物件
把該物件的組件丟到相對應的view裡面

注意
在children裡面的path寫法跟parent不一樣
parent 需要加上/
children不需要/



*/

import { createRouter, createWebHistory } from "vue-router";
import com1 from "../views/com1.vue";
import com2 from "../views/com2.vue";
import com3 from "../views/com3.vue";
import com4 from "../views/com4.vue";
import child1 from "../views/child1.vue";
import child2 from "../views/child2.vue";
import child3 from "../views/child3.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      name:"comOne",
      path:"/",//path按了哪個RouterLink這個組件要出線  如果一開始不是/  一開始組件會是空的
      components:{
        view1:com1,//components表示出現的組件 以及 出現的RouterView
        view2:com3//在/com1這個路徑時  view2這個RouterView出現com3
      }
    },
    {
      path: "/com2",
      components: {
        view1: com2,
        view2: com4,
      },
      children: [
        {
          path: "",//不需加上/ 導航到com2就可以直線顯示此componen
          components: {
            childView: child1,
          },
        },
        {
          path: "child2",
          components: {
            childView: child2,
          },
        },
        {
          path: "child3",
          components: {
            childView: child3,
          },
        },
      ],
    },
  ],
});

export default router;
