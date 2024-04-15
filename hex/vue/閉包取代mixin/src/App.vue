<script setup>
import com1 from "@/com1.vue"
  import {num,add,useNum} from "@/function.js"
  let {num2,add2} = useNum();
</script>

<template>
  mixins的概念請看   "Vue_mixin官網說被半棄用"<br>
  所以compositionAPI直接import需要的函式或資料  <br>
  而不用什麼mixins <br>
  只是引入的對象變成.js而不是組件和組件間傳輸 <br>
  <br><br>
  這邊引入兩種資料 一種互相響應 一種不互相響應 <br>
  互相響應的是因為ref設在functions裡面 所以操作的是functions的ref<br>
<br><br>
  而不互相響應的是閉包概念<br>
  閉包要素還記得媽<br>
  一個函式 回傳  一個使用內部建立變數 的 一個內部建立的函式<br>
  夠饒舌吧<br>
  看function.js比教清楚<br>
  <br>

  <div @click="add">{{num}}</div>
  <div @click="add2">{{num2}}</div>

  <com1></com1>
</template>