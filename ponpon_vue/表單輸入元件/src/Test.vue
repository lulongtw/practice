<script setup>
    import {ref} from "vue"
    let cntn = ref("")
    let func = function(){
        cntn.value=""
    }
    let gender = ref(null)
    let fruits = ref([])//注意checkbox多選匡要用[]
    let slctgender = ref("yellow")//注意select要用""
</script>
<template>
    <input type="text" v-model="cntn"/>
    <div>{{cntn}}</div> <!--注意 這邊沒有.value-->
    <button @click="func">清空</button>
    red<input type="radio" value="red" v-model="gender"/><!--注意 v-model
    就是直接取得該標籤的value-->
    green<input type="radio" value="green" v-model="gender"/>
    <div :class="gender">顏色</div>

    apple<input type="checkbox" value="appele" v-model="fruits"/>
    banana<input type="checkbox" value="banana" v-model="fruits"/>
    <ul>
        <li v-for="item in fruits">{{item}}</li>
    </ul>

    <select v-model="slctgender"><!--select 不再是<input>加type 而且v-model直接加在select-->
        <option value="yellow">choose</option><!--注意要跟初始狀態""一樣-->
        <option value="black">黑</option>
        <option value="blue">藍</option>
    </select>
    <div v-bind:class="slctgender">color</div>

</template>
<style scoped>
    .red{
        color:red
    }
    .green{
        color:green
    }
    .black{
        color:black
    }
    .blue{
        color:blue
    }
    .yellow{
        color:yellow
    }
</style>