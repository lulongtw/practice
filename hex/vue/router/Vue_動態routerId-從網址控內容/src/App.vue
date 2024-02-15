<script setup>
  import {RouterLink,RouterView} from "vue-router";
  let lst = ["dynamanicInfoA","dynamanicInfoB","dynamanicInfoC"]

</script>
<!--
/*
  這節課是動態網址決定顯示的內容
  意思是網址的內容是動態的
  子組件抓取網址的內容後
  依照內容決定畫面渲染的內容

  router:
  先將path改成/xxx/:id 
  RouterLink也要改  由於id是動態從RouterLink引入
  所以:id部分要改成動態資料
  這樣就可以讓path變成 由ROuterLink 的to 輸入的資料了 
  讓網址變成動態路由



  組件:
  透過useRoute()的方法 .routes.paramas.id
  取得當前路由的id
  在使用此id意思是 向後端取得哪項資料的鑰匙
  有了這id後  ajax取得符合id的資料
  渲染到畫面上
  
  動態路由的意思是
  不可能對每個連結都手動輸入要連向哪邊
  所以使用動態路由  
  讓各種不同的資料  可以使用同一個組件渲染到畫面

  但是因為組件一直出現在畫面上  不是每次重新渲染
  所以需要watch router的 .routes.params.id
  

  目前差在在跳轉畫面時 還會看到還沒渲染成新組件的舊組件
  https://router.vuejs.org/zh/guide/advanced/data-fetching.html
  看不懂


*/ 


-->


<template>
  <RouterLink to="/">com1</RouterLink>
  <br>
  <!--
    有兩種導入動態資料的方式  第一種就無腦引入
    第二種則是如果有大量不同的 資料需要引入時
    就需要使用到name屬性來確定要引入到哪邊
    params引入path的資料
    query引入其他資料 不需在router處理的 而是直接丟給組件的
    這邊透過query屬性將index丟給組件
    組件使用useRoutes().query.idx取得index
    並透過這個idx computed 出 class
  -->
  <!-- <template v-for="item in lst">
    <RouterLink :to="`/com/${item}`">com2 : {{item}}</RouterLink>
    <br>
  </template> -->

  <template v-for="(item,index) in lst">
    <RouterLink :to="{name:'com',params:{id:item},query: { idx: index }}">{{item}}</RouterLink>
    <br>
  </template>

  <hr>



  <RouterView name="view1" v-slot="{Component}">
    <KeepAlive>
      <component :is="Component"></component>
    </KeepAlive>

  </RouterView>
</template>