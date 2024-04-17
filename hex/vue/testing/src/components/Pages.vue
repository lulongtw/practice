<script setup>
  import {ref,watch} from "vue";

  let props = defineProps(['fromDad']);
  let emits = defineEmits(['turnPage']);
  let data = ref({})
  let currentPage = ref()
  watch(()=>props.fromDad,
    (newVal)=>{
    //  console.log(data.value)
      data.value = newVal
    }
  )
  function decidePage(page){
    emits('turnPage',page)
  }

</script>

<template>
  <nav aria-label="Page navigation example">
  <ul class="pagination">
    <li v-if="data.has_pre" class="page-item"><a  @click.prevent="decidePage(data.current_page-1)" class="page-link" href="#">Previous</a></li>
    <li v-for="(item,idx) in data.total_pages" class="page-item"><a @click.prevent="decidePage(item)" class="page-link" href="#">{{item}}</a></li>
    <li v-if="data.has_next" class="page-item"><a @click.prevent="decidePage(data.current_page+1)" class="page-link" href="#">Next</a></li>
  </ul>
</nav>
</template>
<style></style>