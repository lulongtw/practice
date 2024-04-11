<script setup>
  import {useRoute} from "vue-router";
  import {ref,watch} from "vue";
  import store from "@/store/store.js"

  let route = useRoute();
  let data = ref("");
  let lst = ref(['a',"b","c"])
  let currentIdx = ref("1")

  watch(()=>route.params.id,
    (newVal)=>{
      //console.log(newVal)
      store.dispatch("fetchData",[newVal,route.query.dataSet])
    }
  )



  watch(()=>store.state.data,
    (newVal)=>{
      data.value = newVal;
    }
  )
  watch(()=>store.state.currentPic,
    (newVal)=>{
      currentIdx.value = newVal
    }
  )

</script>

<template>
  com2
  <template v-if="data">
    <div :class="lst[currentIdx]">
      {{data.name.last}}
      <img :src="data.picture.medium" alt="">
    </div>
  </template>
  <template v-else>
    qq
  </template>
</template>

<style scoped>
  .a{
    background-color:red
  }
  .b{
    background-color:blue
  }
  .c{
    background-color:green
  }
</style>