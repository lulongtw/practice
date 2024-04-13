import {createStore} from "vuex";
import database from "./firebase.js";
import {onValue,get,set,push,ref} from "firebase/database";

let testRef = ref(database,'test');
let countRef = ref(database,'count')
 
const store = createStore({
  state(){
    return{
      data:{},
      count:""
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
    getData(context){
      get(testRef).then((snapshot)=>{
        let temp = snapshot.val();
        context.commit('renewData',temp)
      });
    },
    getCount(context){
      get(countRef).then((snapshot)=>{
        let temp = snapshot.val();
        context.commit('renewCount',temp)
      })
    },
    onValueData(context){
      onValue(testRef,(snapshot)=>{
        let temp = snapshot.val();
        context.commit('renewData',temp)
      })
    },
    onValueCount(context){
      onValue(countRef,(snapshot)=>{
        let temp = snapshot.val();
        context.commit('renewCount',temp)
      })
    },
    setData(context,newVal){
      let newTestRef = push(testRef)
     set(newTestRef,newVal);
    },
    setNewCount(context){
      set(countRef,store.state.count+13);
    }
  }
});

export default store