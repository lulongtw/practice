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
      AllHints:[]
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
    }
  },
  actions:{
    async getAllProducts(context,payload){
      let temp = await getData(payload[0],payload[1],payload[3])
      context.commit("mutations_getAllProducts",temp.data.products)
    },
    async getAllCart(context,payload){
      let temp = await getData(...payload);
      context.commit("mutations_getAllCarts",temp.data.data.carts)
    },
    async deleteProductFromCarts(context,payload){
      let temp = await getData(...payload);
      console.log(temp)
    }
  },
  modules:{
    isLoadingModule,itemColumnModule
  }
});

export default store