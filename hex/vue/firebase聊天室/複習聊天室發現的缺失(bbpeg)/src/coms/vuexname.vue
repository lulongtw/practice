<script setup>
  let props = defineProps({
    here:String
  })

</script>

<template>
  <div>this is {{props.here}}</div>
  
</template>