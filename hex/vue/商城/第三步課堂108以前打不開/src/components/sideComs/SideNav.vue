<script setup>
  import axios from "axios";
  import {noCatch} from "@/assets/functions";
  import {useRouter} from "vue-router";
  let router = useRouter();
 
  function logOut(){
    let headAPI = import.meta.env.VITE_headAPI;
    let url = headAPI + "/logout";
    noCatch(axios.post(url)
      .then(res=>{
        if (res.data.success){
          router.push("/")
        }
      })
    )
  }
</script>

<template>
       <div class="sidebar border border-right col-md-3 col-lg-2 p-0 bg-body-tertiary">
       <div class="offcanvas-md offcanvas-end bg-body-tertiary" tabindex="-1" id="sidebarMenu" aria-labelledby="sidebarMenuLabel">
         <div class="offcanvas-header">
           <h5 class="offcanvas-title" id="sidebarMenuLabel">Company name</h5>
           <button type="button" class="btn-close" data-bs-dismiss="offcanvas" data-bs-target="#sidebarMenu" aria-label="Close"></button>
         </div>
         <div class="offcanvas-body d-md-flex flex-column p-0 pt-lg-3 overflow-y-auto">

 
           <h6 class="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-body-secondary text-uppercase">
             <span>Saved reports</span>
           </h6>
           <ul class="nav flex-column mb-auto">

            <li class="nav-item">
              <router-link to="/dashboard/products">
                <a class="nav-link d-flex align-items-center gap-2">
                 <svg class="bi"><use xlink:href="#file-earmark-text"/></svg>
                 產品列表
               </a>
              </router-link>
             </li>

             <li class="nav-item">
              <router-link to="/dashboard/orderlist">
                <a class="nav-link d-flex align-items-center gap-2">
                 <svg class="bi"><use xlink:href="#file-earmark-text"/></svg>
                 看所有訂單
               </a>
              </router-link>
             </li>

             <li class="nav-item">
              <router-link to="/dashboard/coupon">
                <a class="nav-link d-flex align-items-center gap-2">
                 <svg class="bi"><use xlink:href="#file-earmark-text"/></svg>
                 到優惠券
               </a>
              </router-link>
             </li>

             <hr class="my-3">



             <li class="nav-item">
              <router-link to="/dashboard/simCustomer">
                <a class="nav-link d-flex align-items-center gap-2">
                 <svg class="bi"><use xlink:href="#file-earmark-text"/></svg>
                 到模擬訂單
               </a>
              </router-link>
             </li>

           </ul>
 
           <hr class="my-3">
 
           <ul class="nav flex-column mb-auto">

             <li class="nav-item">
               <a @click.prevent="logOut()" class="nav-link d-flex align-items-center gap-2" href="#">
                 <svg class="bi"><use xlink:href="#door-closed"/></svg>
                 Sign out
               </a>
             </li>
           </ul>
         </div>
       </div>
     </div>

</template>