<script setup>
  import {watch,ref} from "vue"

  let props = defineProps({
    pagi:Object
  });
  let emits = defineEmits(['goPage'])

  let pagination = ref({})

  watch(()=>props.pagi,
        ()=>{
          pagination.value = props.pagi;
        }
  )
  function refreshPage(page){
    emits('goPage',page)
  }
</script>

<template>
  <nav aria-label="Page navigation example">
    <ul class="pagination">
      <li @click.prevent="refreshPage(pagination.current_page-1)" :class="['page-item',{'disabled':!pagination.has_pre}]"><a class="page-link" href="#">Previous</a></li>
      <li @click.prevent="refreshPage(item)" :class="['page-item',{active:item == pagination.current_page}]" v-for="item in pagination.total_pages"><a class="page-link" href="#">{{item}}</a></li>
      <li @click.prevent="refreshPage(pagination.current_page+1)" :class="['page-item',{'disabled':!pagination.has_next}]"><a class="page-link" href="#">Next</a></li>
    </ul>
  </nav>


</template>