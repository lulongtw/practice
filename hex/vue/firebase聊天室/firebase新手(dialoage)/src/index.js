// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";

import { getDatabase, ref, push, onValue, set,get } from 'firebase/database';
//import必要函式


// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAOyIKgNfFbcrGUAuVGNrVg6jzOwzTEwr0",
  authDomain: "dialoague.firebaseapp.com",
  databaseURL: "https://dialoague-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "dialoague",
  storageBucket: "dialoague.appspot.com",
  messagingSenderId: "417193669650",
  appId: "1:417193669650:web:2b2bc736eaf379e8f294cb",
  measurementId: "G-KR6CLXDNHP"
};

  //要使用firebase要有憑證  這個憑證就是firebaseConfig
  //透過這樣初始化firebase這個application應用
const app = initializeApp(firebaseConfig);

//用getDatabase這個函式 取得專案的database這個應用  
const database = getDatabase(app);

//在資料庫中可能會有許多不同區塊資料
//所以使用路徑概念
//就是在資料庫最上面那層的東西  去看筆記裡的圖片
// 創建特定路徑的實體   感覺上是網址之類的
//取得目前這個 專案 裡面  database應用 的 "messages" 路徑
const messagesRef = ref(database, 'messages'); 
console.log(messagesRef)


// 監聽資料變化
//意思是當資料變時馬上這些程式  
onValue(messagesRef, (snapshot) => {
    // snapshot 包含了該路徑下的所有資料
    const data = snapshot.val();
    console.log("資料變化:", data);
  }, {
    onlyOnce: false // 設置為 true 可以讓事件只觸發一次
  });

//單次取得資料 並寫入網頁
//get(xxx)表示是一個異步操作，返回一個proimse物件
//等messageRef獲取後  執行then後面的東西
//最後面也可以加catch 跟下面set()一樣
get(messagesRef).then((snapshot)=>{
  let data = snapshot.val();

  for (let key in data){
    
    if (data[key].msg){
      let div = document.createElement("div");
      div.textContent = data[key].msg;
      document.body.appendChild(div)
    }
  }
})




// 生成新的路徑，而這個路徑是在messageRef之下，是messageRef的子路徑
//想像是一個網址www.google.com/images/  newMessageRef就是/images這個網址 這個路徑
const newMessageRef = push(messagesRef);

// 將資料寫入資料庫
set(newMessageRef, {
  msg: "漂亮阿姨最棒了",
  timestamp: Date.now(),
  // 其他欄位...
})
  .then(() => {
    console.log("資料已成功寫入資料庫");
  })
  .catch((error) => {
    console.error("寫入資料庫失敗: ", error);
  });



  // 使用一个明确的路径，而不是调用 push
  //push(路徑)會返回一個亂數路徑
  //ref則可以使用明確的路徑
  // 當然  路徑名稱必須獨一無二  跟鍵一樣
  //這樣設定路徑如果用迭代方式進去會每次都回迭代掉
  //只留下最後一個
  //其實從這邊可以看出database的巢狀結構
  //messages=>明確路徑={msg:"t33st",...}
  const testRef = ref(database, "messages/明確的路徑"); 
  set(testRef, {
    msg: "t33st",
    timestamp: Date.now()
  });
  





