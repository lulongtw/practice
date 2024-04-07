<script setup>
import { ref } from 'vue';

const props = defineProps(['style1', 'style2']);
const ck1 = ref(false);
const ck2 = ref(false);

function toggleCk(ck) {
  ck.value = !ck.value;
}
</script>

<template>
  <!-- Ensure that we pass the ref itself, not its value -->
  <div @click="() => toggleCk(ck1)" :class="{ [props.style1]: !ck1.value }">按我</div>
  <div @click="() => toggleCk(ck2)" :class="{ [props.style2]: !ck2.value }">按我</div>
</template>
