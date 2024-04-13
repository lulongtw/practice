<script setup>
  import store from "@/store/store.js";

  import {ref,watch,computed} from "vue";

  let data = ref(store.state.data);
  let props = defineProps(['fromDad'])
  let currentUser = ref("")

  let revData = computed(()=>{
    return Object.values(data.value).reverse()
  })

  watch(()=>store.state.data,
    ()=>{
      data.value = store.state.data
    }
  )

  watch(()=>props.fromDad,
    (newVal)=>{
      currentUser.value = newVal
    }
  )
</script>

<template>
  <div class="ContetComWrap">
    <div v-for="item in revData" :class="item.name==currentUser?'rev':''" >
      <div class="pic">
        <img :src="`https://picsum.photos/id/${item.count}/50`" alt="">
      </div>
      <div class="cntn">
        {{item.name}} 說 {{item.cntn}}
      </div>
    </div>
  </div>
</template>

<style scoped>
 @import "@/assets/ContentCom.css";
</style>