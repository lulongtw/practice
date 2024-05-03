import {createStore} from "vuex";
import getDatabase from "@/firebase.js";
import {onValue,set,ref,push} from "firebase/database";

let dataRef = ref(getDatabase,'data');
let countRef = ref(getDatabase,'count');

const store = createStore({
  state(){
    return{
      data:{},
      count:0,
    }
  },
  mutations:{
      renewData(state,newVal){
        state.data = newVal
      },
      renewCount(state,newVal){
        state.count = newVal
      }
  },
  actions:{
    onValueData(context){
      onValue(dataRef,(snapshot)=>{
        let temp = snapshot.val();
        context.commit('renewData',temp)
      })
    },
    onValueCount(context,payload){
      onValue(countRef,(snapshot)=>{
        let temp = snapshot.val();
        context.commit('renewCount',temp)
      })
    },
    sent(context,payload){
      console.log(payload)
      let newData = push(dataRef);
      set(newData,payload)
    },
    setNewCount(context,payload){
      console.log(payload)
      set(countRef,payload)
    }
  }
});

export default store