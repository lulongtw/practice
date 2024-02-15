<script setup>
  import inputvue from "../components/input.vue";
  import roomvue from "../components/room.vue";
  import namevue from "../components/name.vue";
  let name = "com1"
</script>

<template>
  <namevue :here="name"></namevue>
  <inputvue ></inputvue>
  <roomvue></roomvue>
</template>