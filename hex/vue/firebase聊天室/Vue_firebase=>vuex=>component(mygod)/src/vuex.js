import {createStore} from "vuex";
import database from "./firebase.js";
import {get,set,push,onValue,ref} from "firebase/database";



//這節課是從firebase取得資料  放在vuex裡面  組間需要資料統一由vuex處理
//流程是  
//當組件onMounted時 向vuex dispatcch一個行動物件action  也就是叫vuex執行對應的函式   
//這個函式目的要用onValue監聽firebase裡的目標資料
//然後監聽取得資料後 context.commit給mutations  叫mutations裡對應的函式更新對應的資料
//自此vuex的資料更新完成
//接著要在組件內watch store.state.的目標資料  即可完成更新

//組件發送新資訊也是一樣
//組件觸發事件  向vuex dispatch一個行動物件  呼叫vuex的action裡對應的函式
//這函式內部執行set 也就是向firebase發送新資訊
//發送之後就不須再管vuex的資料是否更新，因為一開始時已經onValue監聽了
//組間方面也使用watch了
//流程完畢

//也就是說vuex透過onvalue監聽firebase資料
//組件透過watch監聽vuex資料
//組件送新資料時，透過vuex的action直接發送  不會經過store.state 也就是不會使用commit
//vuex 待firebase更新資料後  用onValue監聽新資料在改動  組件使用watch監聽新資料改動畫面


const store = createStore({
  state(){
    return{
      data:{},
      count:1,
      text:"no",
      testobj:{}
    }
  },
  mutations:{
    spyData(state,newVal){
      state.text = newVal
    },
    spyObjData(state,newVal){
      state.testobj = newVal
    }
  },
  actions:{
   //不需設置get的dispatch 只要設置onvalue就可以監聽到一開始的動態了
   //================這是第一課  第一個簡單的input========
   //onValueSpyData意思是當mount好之後，store開始onVlaue監聽遠端動態
   //一有動態馬上呼叫mutation
   onValueSpyData(context){
      let textRef = ref(database,"test");
      onValue(textRef,(snapshot)=>{
        context.commit("spyData",snapshot.val())
      })
    },

    //當組件送資料時，向遠端送出資料
    //第一個變數必須引入context 第二個才是引入的值
    sentToBase(context,newVal){
      let textRef = ref(database,"test");
      set(textRef,newVal)
    },



    //＝＝＝＝＝＝＝＝＝這是第二課  處理兩個input==========

    onValueSpyObjData(context){
      let testobjRef = ref(database,"testobj");
      onValue(testobjRef,(snapshot)=>{
        context.commit("spyObjData",snapshot.val());
      
      })
    },
    setObjToBase(context,newVal){
      let testObjRef  =ref(database,"testobj");
      let newTestObjRef = push(testObjRef);
      set(newTestObjRef,newVal)
    }
  },


})

export default store