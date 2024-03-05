<script setup>
import { watch, defineProps, ref } from "vue";
let props = defineProps({
  res: Array,
});
let height = ref("")
let lst = ref(props.res); //傳參考  刪掉所以props也會不見
watch(()=>props.res,
  ()=>{   
    //會被這邊笑死 幹你囊
    //想讓結果出現可以在固定在畫面
    //所以想說高手高手高高手用off set 
    //每次取得變亮讓組件出現
    //靠杯媽的幹  直接css設fixed就好啊!!!!!!!!!!!!!
    //fixed啊!!!!!!!!!!!!!!!!!
    // let topDist = window.pageYOffset+150;
    // height.value = topDist + "px";
  },
  {deep:true}
)

//本來想用watch 但是watch也會watch到splice的後果
//而且監看props.res也沒用 因為lst和props.res傳參考都是一樣的東西
//所以使用directives 由標籤自己的生命週期去setTimeout


let vSex = {
  mounted: (el, binding) => {   
    setTimeout(() => {
      del(binding.value);
    }, 5000);
  },
};

function del(idx) {
  for (let i = 0; i < lst.value.length; i++) {
    if (lst.value[i].id === idx) {
      let targetIndex = lst.value.indexOf(lst.value[i]);
      lst.value.splice(targetIndex, 1);
      return;
    }
  }
}
</script>

<template>
 <!-- <div class="nono" :style="{ top: height }"> 
  真滴笑死  
-->
  <div class="nono" >
    <div v-for="item in lst" class="item" v-sex="item.id">
      {{ item.msg }} <span @click="del(item.id)">x</span>
    </div>
  </div>
</template>

<style>
.nono {
  z-index: 1450;
  position: fixed;
  margin-bottom: 30px;
  right: 30px;
  top: 30px;
  display: flex;
  flex-direction: column;
}
.item {
  background-color: pink;
  display: inline;
  padding: 10px 30px;
  margin-bottom: 30px;
  width: auto;
}
span {
  margin-left: 10px;
  font-size: 20px;
}
</style>
