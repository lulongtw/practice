//先install vuex axios

import {createStore} from "vuex";
import axios from "axios";

let store = createStore({
  state(){//重點要state不能data==
    return{
      data:{}
    }
  },
  mutations:{
    cngData(state,newVal){//被觸發後更改data
      state.data = newVal
    }
  },
  actions:{
    fetchData(context){//等待被觸發的函式
      axios.get("https://randomuser.me/api/?results=50")
      .then(function(response){

        response.data.results.forEach(function(item){//這部分是對取出來的資料  給每一筆資料都上一個鍵值對 selected:false 
          item.selected = false;                     //目的是給之後kill用的
        })

        context.commit("cngData",response.data.results) 
        //觸發mutation的cngData函式 並傳值給cngData 讓cngData更改state.data的值
      })
    }
  }
});

export default store