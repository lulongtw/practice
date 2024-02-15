<script setup>
  import inputCom from "./components/inputCom.vue";

  import {ref} from "vue";

  /*
  這節課是sfa的emit和props


  props父組件部分
  首先在子組件標籤上bind :變數Ａ="給子組件的值A"
  接著父組件用select取出要給子組件的值A 這部分用函式getVal決定
  取出之後 透過響應式將值A 傳到子組件的標籤


  props子組件部分
  到了子組件標籤門口了 要怎麼簽收
  在子組件內部
  let props = defineProps({變數A:型態})
  就可以使用props.變數Ａ取得父組件傳來的值Ａ了
 
  但是!還需要監聽 props必須watch看到變動
  在watch內部將新值付給子組件  這樣就可以過關





  emit父組件部分
  首先在子組件標籤上事件監聽 @emit事件暗號A="父組件要做啥函式"
  父組件要做啥函式寫好 然後在該函式第一個參數引入newVal代表emit進來的值  在復職
  父組件就沒事了  不需watch 
  因為emit透過事件監聽了

  emit子組件部分
  一樣let emit = defineEmits(["emit事件案號A"])
  取得emit函式
  接著看哪個函式要觸發emit
  在該函式內部寫
  emit("emit事件案號A",傳給父組件的值)
  就ok拉
 
  
  */ 

  let selVal = ref("");
  function getVal(e){
    selVal.value = e.target.value;
  }



  let info = ref("等待child emit")
  function infoFromSon(newVal){
    info.value = newVal
  }




</script>
<template>
  <div>{{info}}</div>
  <select @change="getVal"><!--getVal 當值變動時，將value傳進子組件props-->
    <option value="無">無</option>
    <option value="迪">迪</option>
    <option value="猛">猛</option>
    <option value="博">博</option>
    <option value="起">起</option>
  </select>
  <hr>
   <!-- 傳props資訊selVal進子組件
        前面是出現在子組件的props變數
        後面是父組件的值 -->
  <inputCom :fromDad="selVal" @sendToDad="infoFromSon"></inputCom>
                         <!-- emit事件案號 = 父組件要幹啥的函式
                              透過事件監聽所以不用watch -->
  <hr>

</template>