const path = require("path")
module.exports={
    //建置模式
    mode:"production",
    //上線模式 也是預設的模式
    //production 和development差在debug 
    //上線模式只會告訴我們看不懂的經由webpack修改過的程式的錯誤碼
    //開發模式會告訴我們我們寫的程式碼錯誤在哪邊


    //入口 從這邊開始執行程式
    entry:"./hehesrc/hehe.js", //(預設是./src/index.js)
    //輸出
    output:{
        filename:"wewe.js",//輸出打包的檔名  (預設是main.js)
        path:path.resolve(__dirname,"hehedist")//輸出位址 __dirname 代表目前資料夾的路徑 (預設是dist)
    }
}