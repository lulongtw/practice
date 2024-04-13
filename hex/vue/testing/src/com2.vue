<script setup>
  import {useRoute} from "vue-router";
  import {ref,watch} from 'vue';
  import store from "@/store.js";

  let route = useRoute();
  let pstn = ref("");
  let num = ref("");
  let data = ref({});
  let isLoading = ref(false)
 
  let lst = ref(['a','b','c'])
  watch(()=>route.params.id,
    async()=>{
      pstn.value = route.params.id;
      isLoading.value = true
      store.dispatch('getData',[route.params.id,route.query.idx])
    }
  )
    watch(()=>store.state.data,
      ()=>{
        isLoading.value = false
        data.value = store.state.data;
        num.value = store.state.num
      }
    )

</script>
<template>
com2
  <!-- <div ><img :src="data." alt=""></div> -->
  <div v-if="isLoading" class="aa">
    loading
  </div>
    <div v-if="data.name" :class="lst[num]">
    <img :src="data.picture.medium" alt="">
    {{data.name.last}}
  </div>
</template>
<style>
  .a{
    background-color: red;
  }
  .b{
    background-color: blue;
  }
  .c{
    background-color: rgb(0, 255, 72);
  }
  .aa{
    background-color: rgb(131, 131, 131);
    position:absolute;
    width:100%;
    height:100%;
    opacity:0.7;
  }
</style>