let path = require("path")
module.exports = {
    mode:"development",
    entry:"./asrc/aindex.js",
    output:{
        filename:"amain.js",
        path:path.resolve(__dirname,"adist")
        },
    //模組載入規則
    module:{
        rules:[//有很多規則，所以是陣列
                //每個載入器規則都會有test和use兩個屬性 描述該語言的如何檢查test和如何使用use
                
                //test  表示如果"載入"的"副檔名"是css，則執行use 
                //而test用正規表示式regular expression表示

                //use  表示如果test過關，則使用use屬性的載入器，有先後之分，不可搞亂
            
                {   //這個物件是說明css模組載入的規則
                test:/\.css$/i,
                //注意，有順序之分 先style後css
                use:["style-loader","css-loader"]
            },
            
            {   //這個物件是說明scss模組載入的規則
                test:/\.scss$/i,
                use:["style-loader","css-loader","sass-loader"]
            }
        ]
    }   
}