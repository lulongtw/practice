<script setup>

import { ref } from "vue";
let simCargoLst = ref([{
  "category": "衣服3",
  "content": "這是內容",
  "description": "Sit down please 名設計師設計",
  "id": "-L9tH8jxVb2Ka_DYPwng",
  "imageUrl": "test.testtest",
  "is_enabled": 1,
  "num": 1,
  "origin_price": 100,
  "price": 600,
  "title": "[賣]動物園造型衣服3",
  "unit": "個"
}])
</script>

<template>
  <div>
   
    <div class="wrapSim">
      <div class="itemSim" v-for="item in simCargoLst" :key="item.id">
        <div class="picWrapSim" :style="`background-image:uri(${item.imageUrl})`"></div>
        <div class="contentWrapSim">
          <div class="titleSim">{{ item.title }}</div>
          <div class="categorySim">{{ item.category }}</div>
          <div class="contentSim">{{ item.content }}</div>
          <div class="originSim">{{ item.origin_price }}</div>
          <div class="priceSim">{{ item.price }}</div>
          <div class="butnWrapSim">
            <div class="seeMoreSim"></div>
            <div class="addToCartSim"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.wrapSim {
  margin: 20px;
  padding: 30px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  justify-content: center;
  gap: 10px;
}


.itemSim {
  width: 100%;
  height: 250px;
  margin-bottom: 0;
  background-color: white;
  border: 1px solid gray;
}

.picWrapSim {
  height: 50%;
  background-color: rgb(108, 32, 32);
}

.contentWrapSim {
  display: grid;
  grid-template-columns: 2fr 3fr;
  padding: 10px;
}

.tilteSim {
  background-color: red !important;

}

.contentSim {
  grid-column: span 4;
}

.categorySim {
  text-align: right;
}

.originSim {
  grid-column: span 2
}</style>