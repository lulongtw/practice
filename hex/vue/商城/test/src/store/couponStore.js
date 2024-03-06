import {getData} from "@/assets/functions";
import store from "./vuex.js"

let couponStore = {
  state(){
    return{
      couponData:[]
    }
  },
  mutations:{
    refreshCoupon(state,newVal){
      state.couponData = newVal
    }
  },
  actions:{
    async fetchCouponListData(context,url){
      store.commit("isLoadingStore/toggleLoading");
      let temp = await getData("get",url);
      store.commit("isLoadingStore/toggleLoading");
      context.commit("refreshCoupon",temp.data.coupons)
    }
  },
  getters:{
    couponData(){
      return state.couponData
    }
  }
}

export default couponStore