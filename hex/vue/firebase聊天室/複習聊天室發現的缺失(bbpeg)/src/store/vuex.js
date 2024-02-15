import {createStore} from "vuex";

const store = createStore({
  state(){
    return{
      data:[],
      count:69
    }
  },
  mutations:{
    updtData(state,newVal){
      state.data.unshift(newVal)
    },
    updtCount(state,newVal){
      state.count+=10
    }
  }
});

export default store