import {createStore} from "vuex";
import getDatabase from "@/firebase.js";
import {onValue,set,ref,push,get} from "firebase/database";

let dataRef = ref(getDatabase,'data');
let countRef = ref(getDatabase,'count');
let viewRef = ref(getDatabase,'view')

const store = createStore({
  state(){
    return{
      data:{},
      count:0,
      view:0
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
    async addViewer(context,newVal){
      let temp
      await get(viewRef).then(snapshot=>{
        temp = snapshot.val();  

      });
      let time = new Date();
      let viewData = {
        'count':++temp.count,
        'time':String(time)
      }

      set(viewRef,viewData)
    },
    sent(context,payload){
 
      let newData = push(dataRef);
      set(newData,payload)
    },
    setNewCount(context,payload){

      set(countRef,payload)
    }
  }
});

export default store