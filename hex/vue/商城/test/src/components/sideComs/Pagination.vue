<script setup>
  import {ref,watch} from "vue"

  let props = defineProps({
    fromDad:Object
  });

  let emits = defineEmits(['goToPage']);
  let lst = ref(props.fromDad);
  let allData = ref(props.fromDad)
  
  watch(()=>props.fromDad,
    (newVal)=>{
     // console.log(newVal)
      allData.value = newVal;
      lst.value = newVal.total_pages;
    }  
  )

  function goPage(page){
    console.log(page)
    emits("goToPage",page)
  }
</script>

<template>
<nav aria-label="...">
  <ul class="pagination">

    <li :class="['page-item',{'disabled':!allData.has_pre}]">
      <a class="page-link" @click.prevent="goPage(allData.current_page-1)">Previous</a>
    </li>

    <li v-for="item in lst" :class="['page-item',{'active':allData.current_page===item}]">
      <a class="page-link" @click.prevent="goPage(item)">{{item}}</a>
    </li>
    <li :class="['page-item',{'disabled':!allData.has_next}]">
      <a class="page-link" href="#" @click.prevent="goPage(allData.current_page+1)">Next</a>
    </li>

  </ul>
</nav>
</template>

<style>
  
</style>