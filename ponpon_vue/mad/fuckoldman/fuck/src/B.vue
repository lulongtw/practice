<script setup>
    import {ref} from "vue"
    let cls1 = ref("")
    let cls2 = ref("")
    let props = defineProps(["clr1","clr2"])
    function one(){
        cls1.value = props.clr1
    }
    function two(){
        cls2.value = props.clr2
    }

</script>
<template>
    <div @click="one" :class="cls1">按我</div>
    <div @click="two" :class="cls2">案偶</div>

</template>
<style scoped>
    .c1{
        color:red;
        background-color: blue;
    }
    .c2{
        color:green;
        background-color: aqua
    }
</style>