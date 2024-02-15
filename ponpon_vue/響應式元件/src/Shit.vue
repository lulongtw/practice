<script setup>
    import {ref} from "vue"
    let ck = true
    let title = ref("old")
    let hndlr = function(){
        ck = !ck
        title.value = ck? "old":"new"
    }
    let state = ref({//注意 ref包裹object
        cntn:"舊內文",
        className:"oldstyle"
    })
    let func = function(){
        state.value.cntn = "新內文"  //注意 state.value不是state.cntn.value
        state.value.className="newstyle"
    }
    let func2 = function(){
        state.value.cntn = "舊內文"
        state.value.className="oldstyle"
    }
    let n = 0
    let num = ref(n)
    let add = function(){
        n++ //注意 不能直接和下一行融合變成num.value = n++ 不然第一個迭代會消失
        num.value = n
    }
    let cng = true
    let s1 = ref("s1")
    let func3 = function(){
        cng = !cng
        s1.value = cng?"s1":"s2"
    }

    let p1 = ref("p1")
    let press = function(){
        p1.value = "p1 p2"//注意此處兩個classname疊加就是style疊加
    }

    let s = true
    let show = ref(s)
    let func4 = function(){
        s = !s
        show.value = s
    }
</script>
<template>
    <div >{{title}}</div>
    <div @click="hndlr">click</div>
    <br>
    <br>
    <div :class="state.className">{{state.cntn}}</div>
    <!--為什麼上面要用v-on:語法  因為要跟js相通啊笨-->
    <div @mouseover="func" @mouseout="func2">over</div>
    <br>
    <br>
    <div>{{num}}</div>
    <div @click="add">按我</div>
    <br>
    <br>
    <div :class="s1" @click="func3">台灣變色龍</div>
    <br>
    <br>
    <div :class="p1" @click="press">這個重點是class的疊加，看code</div>
    <br>
    <br>
    <div v-if="show">跳進去</div>
    <div v-else>跳出來</div>
    <div v-on:mouseover="func4" @mouseout="func4">滑我是用v-if喔</div>
</template>
<style scoped>
    .oldstyle{
        color:grey
    }
    .newstyle{
        color:red
    }
    .s1{
        color:green;
        font-weight:bold;
        font-size:30px
    }
    .s2{
        color:red;
        font-weight:bold;
        font-size:30px;
    }
    .p1{
        font-size:30px
    }
    .p2{
        color:red
    }
</style>