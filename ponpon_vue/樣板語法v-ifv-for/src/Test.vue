<script setup>

//v-if內部==怎麼分辨數字字串
    let num = 3
    let lst = [1,2,3,4,5]
    let data = {
        one:1,
        two:2,
        three:3
    }
</script>
<template>
    <div>判別式</div>
    <div v-if="num==5">老大</div>
    <div v-else-if="num==2">老二</div>
    <div v-else-if="num==='3'">老三</div><!--注意這邊要用===否則num是"3"時，判別式==3也可以true-->
    <div v-else-if="num==4">老四</div>
    <div v-else>老五</div>
    <br>
    <div>迴圈用在陣列上</div>
    <div v-for="(value,index) in lst">{{index+1}},{{value}}</div>
    <div v-for="x in lst">{{x}}</div>
    <br>
    <div>迴圈用在物件上</div>
    <div v-for="(value,key) in data">{{key}},{{value}}</div>
    <div v-for="y in data">{{y}}</div>
    
</template>
<style scope>

</style>