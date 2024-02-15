<script setup>
    import {ref} from "vue"
    let props = defineProps(["cls1","cls2"])
    let c1 = props.cls1
    let c2 = props.cls2
    let cs1 = ref(null)
    let cs2= ref(null)
    let func1 = function(){
        cs1.value=c1
    }
    let func2 = function(){
        cs2.value=c2
    }
</script>
<template>
    <div @click="func1()" :class="cs1" >按我</div>
    <div @click="func2()" :class="cs2">變色色</div>
</template>
<style scoped>
    .c1{
        background-color: brown;
        color:yellow
    }
    .c2{
        background-color: aqua;
        color:indianred
    }

</style>