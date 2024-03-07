<script setup>
  import {watch} from "vue";

  let props = defineProps({
    data:Array,
    currentShow:String
  })
  let emits = defineEmits(["changeCategory"])
  
  //本來要watchcurrentShow 但他是String 傳值不是傳餐靠 不用watch
  
</script>

<template>
  <div class="list-group">
    <a @click.prevent="emits('changeCategory',item)" v-for="(item,idx) in props.data" :class="['list-group-item list-group-item-action',{'active':props.currentShow==item}]" aria-current="true">
      {{item}}
    </a>
  </div>
</template>