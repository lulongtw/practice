import {createStore} from "vuex";

import {getData} from "@/assets/functions"
import isLoadingModule from "./isLoadingModule";
import itemColumnModule from "./itemColumnModule";

let headAPI = import.meta.env.VITE_headAPI;
let myAPI = import.meta.env.VITE_myAPI;

const store = createStore({
  state(){
    return{
      AllProducts:[],
      AllCarts:[],
      AllHints:[],
      smallCartShowing:true,
    }
  },
  mutations:{
    mutations_getAllProducts(state,newVal){
      state.AllProducts = newVal
    },
    mutations_addToHints(state,newVal){
      state.AllHints.push(newVal) 
      setTimeout(()=>{
        state.AllHints.splice(0,1)
      },2000)
    },
    mutations_deleteHints(state,newVal){
      state.AllHints.splice(0,1);
    },
    mutations_getAllCarts(state,newVal){
      state.AllCarts = newVal
    },
    noShowSmallCart(state){
      state.smallCartShowing = false
    },
    showSmallCart(state){
      state.smallCartShowing = true
    }
  },
  actions:{
    async getAllProducts(context,payload){
      let temp = await getData(payload[0],payload[1],payload[3])
      context.commit("mutations_getAllProducts",temp.data.products)
    },
    async getAllCart(context){
      let url = `${headAPI}/api${myAPI}/cart`;
      let payload = ["get",url]
      let temp = await getData(...payload);
      context.commit("mutations_getAllCarts",temp.data.data.carts);
  
    },
    async deleteProductFromCarts(context,id){
      let url = `${headAPI}/api${myAPI}/cart/${id}`
      let payload = ["delete",url]
      let temp = await getData(...payload);
      context.commit("mutations_addToHints",temp.data.message)
      store.dispatch("getAllCart");
    }
  },
  modules:{
    isLoadingModule,itemColumnModule
  }
});

export default store