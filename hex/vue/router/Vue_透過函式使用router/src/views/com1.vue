<script setup>
  import {useRoute} from "vue-router";
  import {onMounted,ref,watch} from "vue";
  
  let route = useRoute();
  //useRoute和useRouter不一樣
  //useRoute是取得當前router實例
  //可以透過params取得當前路由  以及透過query取得傳入參數

  //useRouter是直接取代ROuterLink :to="" 的方法  可以用在函式裡面



  //組件一mount好 檢查目前路由的query的idx 響應渲染到畫面
  onMounted(()=>{
    n.value = route.query.idx;
  })

  //因為動態傳入path的位置 使用的都是同一個組件
  //所以只靠mount不行  要靠watch監視router實例傳入的params是否有變動
  //有變動代表換頁了  換頁內容也要更新
  watch(()=>route.params.id,
        (newVal)=>{
          n.value = route.query.idx
        }
  )
  let n = ref("")
</script>

<template>
  com{{n}}
</template>