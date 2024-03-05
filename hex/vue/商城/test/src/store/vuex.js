import {createStore} from "vuex";

const store = createStore({
  state(){
    return{
      isLoading:false,
    }
  },
  mutations:{
    toggleLoading(state){
      state.isLoading = !state.isLoading
    }
  }
});

export default store