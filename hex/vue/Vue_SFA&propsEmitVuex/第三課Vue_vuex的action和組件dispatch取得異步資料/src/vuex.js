

import axios from "axios";//在這邊向外部取得異步資料  所以在這變axios
import {createStore} from "vuex";

let store = createStore({
  state(){//幹殺小這邊我打錯打成data這樣子組件也讀的到資料幹殺小= = 但是text就讀不到  什麼鬼拉
    return{
      data:"等組件onMounted後發送dispatch，叫store的action取得外部資料後，觸發mutation更改資料，在用watch監聽store的資料變動，在印出來好累",
      text:"準備接收input給的資料"
    }
  },
  mutations:{//就是更改資料的函式
    getData(state,newVal){
      state.data = newVal
    },
    updtText(state,newVal){
      state.text = newVal
    }
  },
  actions:{//取得異步資料後 並觸發mutations
    //重點要引入參數context
    fetchData(context){
      axios.get("https://randomuser.me/api/?results=50")
      .then(function(response){
        //然後要用content.commit 而不是在組件使用的store.commit
        context.commit("getData",response)
      })
    }
  }
});

export default store