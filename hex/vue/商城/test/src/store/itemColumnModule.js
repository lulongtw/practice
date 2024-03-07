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
      // 這邊好破格 因為加到購物車後 右上紅點數字要馬上連動
      //所以要馬上得到購物車數量 不知寫哪變 所以寫這邊
      let headAPI = import.meta.env.VITE_headAPI;
      let myAPI = import.meta.env.VITE_myAPI;
      let url = `${headAPI}/api${myAPI}/cart`
      let payload2 = ["get",url];
      store.dispatch("getAllCart",payload2);
    }
  }
}