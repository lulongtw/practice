<script setup>
import whichCom from "../components/whichCom.vue"
import inputCol from "../components/inputCol.vue"
import room from "../components/room.vue"

</script>

<template>
  <div class="wrap">
    <whichCom :com="'組件1'"></whichCom>
    <inputCol></inputCol>
    <room></room>
  </div>
</template>

<style scoped></style>