<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <div><RouterLink to="/">com1</RouterLink></div>
  <div><RouterLink to="/com2">com2</RouterLink></div>
  <hr />
    <RouterView v-slot="{Component}">
        <KeepAlive>
            <component :is="Component"></component>
        </KeepAlive>
    </RouterView>

</template>

<style scoped></style>
