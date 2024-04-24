import {createStore} from "vuex";
import {getData,getUrl} from "@/functions.js"



const store = createStore({
  state(){
    return{
      allProducts:[],
      isLoading:false
    }
  },
  mutations:{
    toggleIsLoading(state,newVal){
      state.isLoading = !state.isLoading
    },
    renewAllProducts(state,newVal){
      state.allProducts = newVal
    },

  },
  actions:{
    async fetchAllProducts(context,payload){
      context.commit('toggleIsLoading')
      let url = getUrl(payload.url)
      let res = await getData(url,payload.method);
      if (res.data.success){
        context.commit('renewAllProducts',res.data);
        context.commit('toggleIsLoading',res.data)
        return
      }
      context.commit('toggleIsLoading')
    }
  }
})

export default store