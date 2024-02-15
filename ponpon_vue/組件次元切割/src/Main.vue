<script setup>
    import {ref} from "vue"
    let n = 0
    let num = ref(n)
    let func1 = function(){
        n++
        num.value = n
    }
</script>
<template>
    <div @click="func1">{{num}}</div>
</template>
<style scoped></style>
  