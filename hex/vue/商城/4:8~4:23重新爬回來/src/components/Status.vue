<script setup>
  import {ref,watch,computed} from "vue";
  let props = defineProps(['fromDad']);
  let lst = ref([]);

  watch(()=>props.fromDad,
    (newVal)=>{
      lst.value.unshift(newVal);
      setTimeout(()=>{
        lst.value.forEach(item=>{
          if (item.stamp==newVal.stamp){
            let idx = lst.value.indexOf(item);
            lst.value.splice(idx,1)
          }
        })
      },2000)
    },{
      deep:true
    }
  )
    /*
    這邊好討厭  
    一開始在父組件傳來的所有事件序列
    然後sort放到畫面
    使用directives安裝定時炸彈

    但directives會抓到錯誤的stamp
    是因為REVERSE的關係  反而抓到最頭的stamp
    好怪

    所以不能用directives裝定時炸彈
    要讓父組件傳資料進來
    資料一進來塞進本地lst
    lst直接針對新進弟兄裝炸彈

    然後塞資料的方法 可以直接用unshift
    這樣之後就不需要computed => .sort()了
    
    */
  
  //這也可以 只是比較麻煩  //一開始進來unshift就好
  let revLst = computed(()=>{
    lst.value.sort((a,b)=>{
      return b.stamp-a.stamp
    })
    return lst.value
  })
  function del(value){
    let idx
        lst.value.forEach(item=>{
          if (item.stamp==value){
            idx = lst.value.indexOf(item);
            lst.value.splice(idx,1)
            return
          }
        })

  }
  // let vKill = {
  //   mounted(el,binding){
  //     console.log(binding.value)
  //     setTimeout(()=>{
  //       del(binding.value)
  //     },20000)
   
  //   }
  // }
</script>
<template>
  <div class="statusWrap">
    <div @click="del(item.stamp)"  v-for="(item,idx) in lst" :key="idx">{{item.content}}</div>
  </div>
</template> 
<style>
  .statusWrap{
    position: fixed;
    top:30px;right:30px;
    display: flex;
    flex-direction:column;
    gap:10px;
    z-index:999999
  }
  .statusWrap>div{
    padding:20px;
    background-color: pink;
  }
</style>