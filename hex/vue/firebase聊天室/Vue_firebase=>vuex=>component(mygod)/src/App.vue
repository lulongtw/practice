<script setup>
  import store from "./vuex.js";
  import {ref,onMounted,watch,computed} from "vue";
  let text = ref(store.state.text);
  let newText = ref("");


  onMounted(()=>{
    text.value = store.state.text
    //不需設置get的dispatch 只要設置onvalue就可以監聽到一開始的動態了
    store.dispatch("onValueSpyData")
    //這個意思是當組件mount好之後 發送異步
    //叫store去onValue監聽遠端
  })
  
  watch(//組件記得監聽store的資料
    ()=>store.state.text,
    (newVal)=>{text.value = newVal;}
  )

  function send(){
    store.dispatch("sentToBase",newText.value)

  }

//=================第二部分================================
  let testUser = ref("");
  let testContent = ref("");
  let testobj = ref(store.state.testobj);

  //將取得的資料reverse 透過computed  保持響應
  let reversedTestobj = computed(()=>{
    console.log( Object.values(testobj.value).reverse())
    return Object.values(testobj.value).reverse()
  })


  onMounted(()=>{
     store.dispatch("onValueSpyObjData")
  })

  watch(()=>store.state.testobj,
        (newVal)=>{testobj.value = newVal}
  )

  function sendObj(){
    store.dispatch("setObjToBase",{
      testUser:testUser.value,
      testText:testContent.value
    })
  }

</script>

<template>
  <input type="text" v-model="newText">
  <button @click="send">click</button>
  <div>  {{text}}</div>
  <hr>
  <input type="text" v-model="testUser">
  <input type="text" v-model="testContent">
  <button @click="sendObj">按我</button>
  <div v-for="item in reversedTestobj">{{item.testUser}}說{{item.testText}}</div>

</template>
<style scoped>
  button{
    width:50px;height:50px;background-color: red;
  }
</style>