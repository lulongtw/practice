import {createStore} from "vuex";
import {getData} from "@/assets/functions";
import isLoadingStore from "./isLoadingStore";
import couponStore from "./couponStore";

const store = createStore({
  state(){
    return{
      // isLoading:false,
      orderList:[]
    }
  },
  mutations:{
    // toggleLoading(state){
    //   state.isLoading = !state.isLoading
    // },
    writeData(state,newVal){
      state.orderList = newVal
    }
  }, 
  actions:{
    async fetchOrderListData(context,info){
      context.commit("toggleLoading")
      let temp = await getData(info[0],info[1]);
      context.commit("writeData",temp.data.orders);
      context.commit("toggleLoading")
    }
  },
  //getters功能類似computed
  getters:{
    orderList(state){
      return state.orderList
    }
  },
  modules:{
   isLoadingStore , couponStore
  }
});

export default store