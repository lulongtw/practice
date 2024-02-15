/*
router第一課超基本教學

router是啥？
就是在單頁應用裡，點擊連結，來刷新特定部分頁面，且不使整個頁面翻新的技術
會使用到RouterLink和RouterView這兩個標籤
RouterLink相當於a標籤 只是a標籤是href="位址" RouterLink是to="位址"
這個位址意思是讓某個組件Ａ來渲染畫面，
點擊RouterLink取得位址後，
會根據router的設定
在特定name=xxx的RouterView讓組件Ａ刷新頁面


建好vue後
使用routern4大要素

1.main.js引入router以及.use(router)
2.router資料夾裡的index.js 
3.views建立view組件
4.組件使用RouterLink以及RouterView

*/

//1.main.js引入router以及.use(router)

import {createApp} from "vue";
import router from "./router";//整個import進來 = =
import App from "./App.vue";

let app = createApp(App);

app.use(router);//記得use

app.mount("#app")