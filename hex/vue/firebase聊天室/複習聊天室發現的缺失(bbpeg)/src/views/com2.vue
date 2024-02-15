<script setup>
  import inputvue from "../coms/vuexinput.vue";
  import namevue from "../coms/vuexname.vue";
  import roomvue from "../coms/vuexroom.vue";
  let name = "com2"

</script>

<template>
  <namevue :here="name"></namevue>
  <inputvue></inputvue>
  <roomvue></roomvue>
  
</template>