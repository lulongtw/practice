import {createStore} from "vuex";
//先install vuex
let store = createStore({
  state(){//是state不是setup
    return{
      msg:1
    }
  },
  mutations:{
    //mutations以物件表現
    //透過mutation裡的函式進行資料更動
    //mutations裡的函式都要引入state以及代表新值的變數
    updt(state,newMsg){
      state.msg = newMsg
    }
  }
})

export default store