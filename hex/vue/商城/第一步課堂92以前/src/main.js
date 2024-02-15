import {createApp} from "vue";
import router from "./router";
import App from "./App.vue";
import axios from "axios";


let app = createApp(App);




/*
這邊上beforeEach   以及   開通跨域上傳cookie的開關 axios.default.withCreadiencials = true

beforeEach是針對每次透過router替換顯示組件時
都會經過的檢查
to代表要前往的routes物件
from代表目前要離開的routed物件
routes物件就是router裡面的routes裡面的物件{path:"/",component:com1.vue}
在routes物件裡面設置meta:{requiredAuth:true/false} 讓router.beforeEach進行檢查

*/


  //新版不是用next 只有return false會停止導航
  //要設置async 以及 await 
  //否則會跳轉動作  會跳過 的axios回傳值 
  //等於跳到新畫面後  再判斷是否可以到新畫面

  //因為新版不是用next 導航到哪是靠router.push()
  //只有在return false的情況下會停止導航
  //否則都是直接跳轉

  //所以注意在成功if(res.data.success)那邊不能在router.push("/index")
  //否則會無限迴圈
  //因為對城市來說  已經跳轉了  但又多家router.push()又再跳轉一次  會無限



//也可放在router的index.js 看邏輯是怎樣
//新版不需要next了 只會對false有反應 fasle就是不對跳轉產生反應


router.beforeEach( async(to)=>{
  if(to.meta.requiredAuth){// 如果要前往的那頁 他的meta.requiredAuth為true
    //就執行下面check 是否依然登入api
    let headAPI = import.meta.env.VITE_headAPI;
    let url = headAPI + "/api/user/check";
    console.log(url)
    await axios.post(url)
    .then(res=>{
      console.log(res.data.success)
      if (!res.data.success){//新版只會對false有反應  如果沒有回傳false 就是直接下一頁
        router.push("/")//如果需要跳轉頁面則使用router
      }
    })
  }
})


//開通瀏覽器跨域傳給sever的開關
axios.defaults.withCredentials = true;
/*
https://www.udemy.com/course/vue-hexschool/learn/lecture/22708969#content

當你的前端應用嘗試向一個與其不同源（
協議、域名、連接埠任一不同）的伺服器傳送請求時，
這就構成了一個跨域請求。
默認情況下，出於安全考慮，
瀏覽器不會在跨域請求中包含cookies或者認證資訊（如HTTP Basic auth資訊）。

設定withCredentials為true
意味著你告訴瀏覽器在傳送跨域請求時
帶上當前網站的cookies和已經通過認證的憑證（如果有的話  也就是說

這句話他媽只是一個開關  要帶什麼還需要另外設定 = =
要怎麼設定  當然是在登入成功後  接收到伺服器回傳的token和expired後
把token和expired做成cookie

然後在最外層的app.vue,因為所有行為都會經過app.vue ???
將cookie取出  並送出

）。
這對於需要在前後端分離的應用中保持使用者會話
（如使用Session或JWT Tokens儲存在cookies中）非常重要。


*/
//要有這行 在session階段時  瀏覽器在每次發送請求，才會將cookies送給伺服器
//這樣server才會知道目前的使用者是誰

app.use(router);
app.mount("#app")