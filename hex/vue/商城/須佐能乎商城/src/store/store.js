import {createStore} from "vuex";
import {getData,getUrl} from "@/functions.js"
import loginModule from "./loginModule";


const store = createStore({
  state(){
    return{
      allProducts:[],
      isLoading:false,
      sellerProductList:{},
      currentCategory:"衣服",
      messages:{},
      cartList:[]
    }
  },
  mutations:{
    toggleIsLoading(state,newVal){
      state.isLoading = !state.isLoading;
    },
    renewAllProducts(state,newVal){
      state.allProducts = newVal
    },
    renewSellerProductList(state,newVal){
      state.sellerProductList = newVal
    },
    renewCurrentCategory(state,newVal){
      state.currentCategory = newVal
    },
    renewMessages(state,newVal){
      state.messages = newVal
    },
    renewCartList(state,newVal){
      state.cartList = newVal
    }

  },
  actions:{
    async fetchAllProducts(context,payload){
      let res = await getData(payload.url,payload.method);
      if (res.data.success){
        let temp = {}
        res.data.products.forEach(item=>{
          if (!temp[item.category]){
            temp[item.category] = [];
              }
          temp[item.category].push(item)
        })
        context.commit('renewAllProducts',temp);
      }
    },
    async getSellerProductList(context,payload){
      let res = await getData(payload.url,payload.method);
      if (res.data.success){
        context.commit('renewSellerProductList',res.data.products);
      }
    },
    async getCartList(context,payload){
      let res = await getData(payload.url,payload.method);
      if (res.data.success){
        context.commit('renewCartList',res.data.data.carts);
      }
    }
  },modules:{
    loginModule
  }
})

export default store