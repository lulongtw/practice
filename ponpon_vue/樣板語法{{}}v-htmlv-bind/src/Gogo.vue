<script setup>
    let t1 = "pureword"
    let t2 = "<u>word with html</u>"
    let t3 = "style1"
    let t4 = "style2"
    let t5 = "雙大括號嵌入程式雨具baaa"
    let t6 = "用vhtml嵌入程式雨具baaa"
    let swch = true
</script>
<template>
    <div>{{t1}}</div>
    <div v-html="t2"></div>
    <div v-bind:class="t3">操作標籤class1</div>
    <div v-bind:class=t3>操作標籤class2</div>
    <div :class="'t3'">操作標籤class3</div>
    <div :class="t4">簡寫操作標籤class</div>
    <div>{{t5.toUpperCase()}}</div>
    <div v-html="t6.toUpperCase()"></div>
    <div v-bind:class="swch?'on':'off'">bind帶入js雨具</div>
    <div :class="swch?'on':'off'">簡寫冒號帶入js雨具</div>
</template>
<style scoped>
    .on{
        background-color: yellow;
        color:black
    }
    .off{
        background-color: black;
        color:yellow
    }
    .style1{
        background-color: goldenrod;
        color:red
    }
    .style2{
        background-color: blueviolet;
        color:yellow
    }
    .t3{
        background-color: khaki;
        color:pink
    }
</style>