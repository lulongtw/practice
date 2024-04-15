import {ref} from 'vue';
/*
使用num和add 操作的響應源於此  所以會互相響應
*/

let num = ref(69);

function add(){
  num.value++
}
/*
下面是就是閉包
一個內部建立的變數
一個內部建立的函式
內部建立的函式使用內部建立的變數
回傳內部建立的函式

對於每個組件解包後 每個函式內部的資料都是獨一無二的
所以不會互相響應
*/
function useNum(){
  let num2 = ref(1);
  function add2(){
    num2.value++
  }
  return {num2,add2}//記得要return
}

export {num,add,useNum}