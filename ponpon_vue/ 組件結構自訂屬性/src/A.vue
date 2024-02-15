<script setup>
    import {ref} from "vue"
    let props = defineProps(["fntsz","fntwgt"])/*記得是序列*/ 
    let fs = props.fntsz /*也可寫 let {fs} = defineProps(["fntsz"])*/
    let fw = props.fntwgt /* 也可  let {fw} = defineProps(["fntwgt"])*/
    let fss = ref(null)  /*設定初始狀態*/
    let fww = ref("100") /*設定初始狀態*/
    let func1 = function(){
        fss.value = fs  /*改變狀態*/
    }
    let func2 = function(){
        fww.value=fw /*改變狀態*/
    }

    let state = ref({
        fss3:null,
        fww3:null
    })
    let func3 = function(){
        state.value.fss3 = fs
        state.value.fww3 = fw
    }

</script>
<template>      
    <!--style內部好像都要{}  跟class只要class=""不一樣-->
    <div v-on:click="func1()" v-bind:style="{fontSize:fss,fontWeight:100}">A</div>
    <div @click="func2()" :style="{fontWeight:fww}">AA</div>
    <div @click="func3()" :style="{fontSize:state.fss3,fontWeight:state.fww3}">AAA</div>
    <!--注意這邊要填入state.fss3 而不是fss3-->
</template>
<style scoped>

</style>