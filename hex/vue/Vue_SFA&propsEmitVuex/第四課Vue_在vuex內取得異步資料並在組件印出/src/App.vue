<script setup>
  import store from "./store.js";
  import {onMounted,watch,ref} from "vue";


  //最下面還有註解  另一種做法


  onMounted(()=>{//這個子組件一蛋mounted後
    //向store 觸發action 裡的 fetchData函式
    store.dispatch("fetchData")
  })

  let list = ref({})
  //接收必須用watch監視到store.state.data變更後
  //再接收資訊
  watch(()=>store.state.data,(newVal)=>{
    list.value = newVal
  })

  function kill(item){
    //這就是vue屌的地方
    //反方向更改 繞來繞去的
    //在迭代時送進去的變數  直接拿出來更改
    item.selected = !item.selected;
  }

/*
這兩個東西是說明直接在組件內部ajax資料時要注意的地方
反正都要在onMounted裡面

說明函式a和說明函式b都可以成功
重點是ajax要放在onMOunted hooker內
還有.then之後的東西在{}才會異步而得到賦值，
也就是說  
js的話  有關畫面刷新的函式要寫在這裡面
而vue 響應式則只要更新資料就好
*/
function 純粹包裹用的說明函式a() {
  onMounted(() => {
    axios.get("https://randomuser.me/api/?results=50")
      //.then 等get到後 執行.then後面的東西
      .then(function (response) {
        data.value = response.data.results
      })
  })
}
function 純粹包裹用的說明函式b() {
  async function get() {
    try {
      let ans = await axios.get("");
      return ans.data.results;
    } catch (error) {
      console.error("shit", error)
    }
  }
  //在onMounted上async
  //因為要等get()
  onMounted(async () => {
    data.value = await get()
  })
}
</script>

<template>
  <table>
    <thead>
      <tr>
        <td>#</td>
        <td>pic</td>
        <td>name</td>
        <td>location</td>
        <td></td>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(item,key) in list" :class="{bck:item.selected}">
        <td>{{key+1}}</td>
        <td><img :src="item.picture.medium"/></td>
        <!--
              //如果父組件傳進來的props是ajax來的  
//就必須使用watch檢查props是否有更新
//但在最後渲染畫面時有可能發生
//在watch時有資料  但是無法渲染在畫面上的情形
//此時就必須
/*

     這種可以 <div>{{imm.name?.first}}</div>
    這種也可以<div v-if="imm.name">{{imm.name.first}}</div>
     這行印不出來<div>{{imm.name.first}}</div> 


意思是要先檢查傷一層有沒有東西在進行渲染
但是這邊不用  可能資料是從store來的關係
*/
        -->
        <td>{{item.name.first}}</td>
        <td>{{item.location.country}}</td>
        <td><div class="btn" @click="kill(item)">按我</div></td>
      </tr>
    </tbody>
  </table>
</template>

<!--
 原本是把決定是否變紅的變數設在data裡面
 這個是把決定的變數設在組件裡面
 按下就檢查是否在名單內
 不在名單內  就加進名單  透過ref 變紅
 已經在名單內了  代表早變紅了 現在要變白  所以移除  透過ref變白

<script setup>
  import {store} from "./store.js";
  import {onMounted,ref,watch} from "vue";

  let lst = ref([]);
  let toKill = ref([])

  onMounted(async()=>{
    store.dispatch("fetchData")
  })
  watch(()=>store.state.data,
        ()=>{
          lst.value = store.state.data.data.results}
  )
  function kill(idx){
    if (toKill.value.includes(idx)){
      let toRemoveIdx = toKill.value.indexOf(idx);
      toKill.value.splice(toRemoveIdx,1)
    }else{
      toKill.value.push(idx)
    }
  }
  function check(idx){
    return toKill.value.includes(idx)?"red":"white"
  }

</script>

<template>
  <table>
    <thead>
      <tr>
        <th>#</th>
        <th>pic</th>
        <th>name</th>
        <th>location</th>
        <th>kill</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(item,key) in lst" :class="check(key)"> 
        <td>{{key+1}}</td>
        <td><img :src="item.picture.medium" alt=""></td>
        <td>{{item.name.last}}</td>
        <td>{{item.location.city}}</td>
        <td><div class="box" @click="kill(key)"></div></td>
      </tr>
    </tbody>
  </table>

</template>




-->