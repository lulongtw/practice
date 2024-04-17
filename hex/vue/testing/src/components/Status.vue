<script setup>
  import {ref,watch,computed} from "vue";
  let props = defineProps(['fromDad']);
  let lst = ref(props.fromDad);

  watch(()=>props.fromDad,
    (newVal)=>{
      lst.value = newVal;
     // console.log(lst.value)
    },{
      deep:true
    }
  )

  
  let revLst = computed(()=>{
    return lst.value.sort((a,b)=>{
      return b.stamp-a.stamp
    })
  })
  function del(value){
    let idx
        lst.value.forEach(item=>{
          if (item.stamp==value){
            idx = lst.value.indexOf(item);
            lst.value.splice(idx,1)
          }
        })

  }
  let vKill = {
    mounted(el,binding){
      setTimeout(()=>{
        del(binding.value)
      },10000)
   
    }
  }
</script>
<template>
  <div class="statusWrap">
    <div @click="del(item.stamp)" v-kill="item.stamp"  v-for="(item,idx) in revLst" :key="idx">{{item.content}}</div>
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