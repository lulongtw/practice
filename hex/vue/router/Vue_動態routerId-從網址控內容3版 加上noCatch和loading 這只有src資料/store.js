import { createStore } from "vuex";
import axios from "axios";
import {noCatch} from "@/function.js";

const store = createStore({
  state(){
    return {
      data:{},
      num:""
    }
  },
  mutations:{
    renewData(state,newVal){
      state.data = newVal;
 
    },
    renewNum(state,newVal){
      state.num = newVal
    }
  },
  actions:{
    async getData(context,argus){
      let api = `https://randomuser.me/api/?seed=${argus[0]}`
      let temp = await noCatch(axios.get(api));
      context.commit('renewData',temp.data.results[0]);
      context.commit('renewNum',argus[1])
    }
  }
});

export default store