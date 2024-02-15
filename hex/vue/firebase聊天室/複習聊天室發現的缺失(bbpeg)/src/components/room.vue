<script setup>
  import {onValue,get,ref} from "firebase/database";
  import database from "../store/firebase.js";
  import {onMounted,ref as vueref,computed,watch} from "vue";

  let data = vueref([]);
  let talkRef = ref(database,"talk");
  onMounted( async ()=>{
    let snapshot = await get(talkRef);
    data.value = snapshot.val();
  })


  //要用computed追蹤日後變化
  let reversedData = computed(()=>{
  
    return Object.values(data.value).reverse()
    // 記得要return = =
    //Object.values是直接抓取data.value的值，變成序列
    //比方說{a:{a:1},b:{b:1}}
    //變成[{a:1},{b:1},{c:1}]
    //如果是Object.keys(data.value)的話
    //就是["a","b","c"]
  });

  //這段也可以用watch???
  // let reversedData = computed(()=>{
  //   return Object.values(data.value).reverse()
  // });
  // let revData = vueRef({})
  //下方v-for要改成revData


  onValue(talkRef,(snapshot)=>{
    data.value = snapshot.val();
  })

 function which(userName){//這變亂射async整個抓不到幹你娘  沒事不要亂射async
    let keyss = Object.keys(data.value).reverse();
    //取得本地端資料data的keys的序列  並倒轉  檢查第一個是否是輸入者
    if (data.value[keyss[0]].user==userName){
      return ""
    }else{
      return "other"
    }
  }
</script>

<template>
  <div class="room">

    <div v-for="key in reversedData" :class="['chat',which(key.user)]">
      <div class="chat">
        {{key.user}} 說: {{key.text}}
      </div>
      <div class="pic">
        <!--bind後=後面都要""  但是網址必須強制有""  變成需要兩個""  那就給網址加上''  然後在屬性不能用{{}}-->
        <img :src="'https://picsum.photos/id/'+key.idx+'/60'" alt="">
      </div>
    </div>

  </div>
  
</template>