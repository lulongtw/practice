<script setup>
import { useRoute } from 'vue-router';
//是useRoute 不是useRouter
//useRoute用來取得當前路由的資訊
//例如params.id 或是 query的資訊等

//useRouter是別堂課
//是拿來給代替RouterLink的函式用的
import { ref, watch ,onMounted,computed} from "vue"

// 使用 useRoute 获取当前路由实例
const route = useRoute();
// console.log(route)
let data = ref([]);
let clsidx = ref("")
// console.log(route.params.id)

function getData(newVal) {
  let url = `https://randomuser.me/api/?page=3&results=1&seed=${newVal}`;
  console.log(url)
  fetch(url)
    .then((res) => res.json())
    .then((res1) => {
      data.value = res1.results
    })
    .catch(res => {
      console.log("shit")
    })
}
let lst  =["red","blue","yellow"]
let cls = computed(()=>{
  return lst[route.query.idx]
})

onMounted(()=>{
  // console.log(route)

  getData(route.params.id)
})

watch(() => route.params.id,
  (newVal) => {
    // console.log(newVal)
    //避免在離開此view時取得route id
    //如果取得 id 會因出undefine 進而渲染data
    //因為keepalive的關係  渲染過的資料會留在畫面
    //
    if (newVal){
      getData(newVal)
    }


  }
)





</script>

<template>
  <div v-for="item in data">
    <div :class="cls">
      {{ item.name.first }}
      <img :src="item.picture.medium" alt="">
    </div>
  </div>
</template>

<style scoped>
  .red{
    background-color: red;
  }
  .blue{
    background-color: rgb(30, 0, 255);
  }
  .yellow{
    background-color: rgb(208, 255, 0);
  }
</style>
