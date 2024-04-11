import {createStore} from "vuex";
import axios from "axios"

const store = createStore({
  state(){
    return{
      data:"1",
      lst:['dick','penis','asshole'],
      currentPic:""
     
    }
  },
  mutations:{
    renewData(state,newVal){
      state.data = newVal
    },
    renewCurrentPic(state,newVal){
      state.currentPic = newVal
    }
  },
  actions:{
    async fetchData(context,argu){
      try{
        console.log(argu)
        let api = `https://randomuser.me/api/?page=3&results=1&seed=${argu[0]}`;
        let temp = await axios.get(api);
        context.commit('renewData',temp.data.results[0])
        context.commit('renewCurrentPic',argu[1])
      }catch(error){
        console.log(error)
      }
    }
  }

});

export default store