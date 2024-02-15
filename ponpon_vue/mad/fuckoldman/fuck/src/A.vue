<script setup>
import {ref} from "vue"
    let props = defineProps(["fz","fw"])
    let fzz = ref("5px")
    let fww = ref("200")
    
    function click(){
        fzz.value = props.fz
        
    }
    let ck = true
    function newclick(){
        ck=!ck
    
    }
</script>
<template>
    <div @click="click" v-bind:style="{fontSize:fz}">A</div>
    <div @click="newclick" :style="{fontSize:fzz,fontWeight:fww}">AA</div>
</template>
<style scoped></style>