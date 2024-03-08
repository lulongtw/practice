import {getData} from "@/assets/functions"
import store from "./vuex.js";

export default {
  state(){
    return{

    }
  },
  mutations:{

  },
  actions:{
    async addToCart(context,payload){
      let temp = await getData(...payload);
      let msg = temp.data.message;
      context.commit("mutations_addToHints",msg);  
      store.dispatch("getAllCart");
    }
  }
}