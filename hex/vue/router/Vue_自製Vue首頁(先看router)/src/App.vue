<script setup>
    import {RouterLink,RouterView} from "vue-router"
    import HelloWorld from "./components/HelloWorld.vue"
</script>

<template>
    <div class="wrap">
        <header>
        <img src="@/assets/logo.svg" alt="">
        <HelloWorld msg="u did it"/>
        <div class="nav">
            <RouterLink to="/">home</RouterLink>
            <RouterLink to="/about">about</RouterLink>
        </div>
    </header>
    <RouterView/>
    </div>

</template>

<style scoped>
    header{
        display: flex;
        flex-direction:column;
        align-items: center;
    }
    .nav{
        display:flex;
        gap:10px;
        margin:10px;
       
    }
    img{
        width:300px;
        object-fit: contain;
    }
</style>