//要先npm install vuex
import {createStore} from "vuex";

import {testRef} from "./firebase.config.js";
import {get,onValue} from "firebase/database"
import {reactive} from "vue";

// let data = [{ "name": "a", "text": "a", "idx": 2 }];
let data = []




const store = createStore({
  state(){
    return {
      data:data,
      count:1
    }
  },
  mutations:{
    updt(state,newData){
      state.data.unshift(newData)
    },
    updtCount(state,newCount){
      state.count = newCount
    }
  }
});

export default store