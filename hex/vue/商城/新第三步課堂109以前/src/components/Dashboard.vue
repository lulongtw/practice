<script setup>
  import axios from "axios";
  import {useRouter} from "vue-router";

  import {noCatch} from "@/assets/functions"

  let router = useRouter();

  function logOut(){
    let headAPI = import.meta.env.VITE_headAPI;
    let url = headAPI+"/logout";
    noCatch(axios.post(url))
    .then(res=>{
      if(res.data.success){
        router.push("/fsaf")
      }
    })
  }
</script>

<template>

<header class="navbar sticky-top bg-dark flex-md-nowrap p-0 shadow" data-bs-theme="dark">
  <a class="navbar-brand col-md-3 col-lg-2 me-0 px-3 fs-6 text-white" href="#">肥狗超商</a>

  <ul class="navbar-nav flex-row d-md-none">
    <li class="nav-item text-nowrap">
      <button class="nav-link px-3 text-white" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSearch" aria-controls="navbarSearch" aria-expanded="false" aria-label="Toggle search">
        <svg class="bi"><use xlink:href="#search"/></svg>
      </button>
    </li>
    <li class="nav-item text-nowrap">
      <button class="nav-link px-3 text-white" type="button" data-bs-toggle="offcanvas" data-bs-target="#sidebarMenu" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation">
        <svg class="bi"><use xlink:href="#list"/></svg>
      </button>
    </li>
  </ul>

  <div id="navbarSearch" class="navbar-search w-100 collapse">
    <input class="form-control w-100 rounded-0 border-0" type="text" placeholder="Search" aria-label="Search">
  </div>
</header>

<div class="container-fluid">
  <div class="row">
    <div class="sidebar border border-right col-md-3 col-lg-2 p-0 bg-body-tertiary">
      <div class="offcanvas-md offcanvas-end bg-body-tertiary" tabindex="-1" id="sidebarMenu" aria-labelledby="sidebarMenuLabel">
        <div class="offcanvas-header">
          <h5 class="offcanvas-title" id="sidebarMenuLabel">肥狗超商</h5>
          <button type="button" class="btn-close" data-bs-dismiss="offcanvas" data-bs-target="#sidebarMenu" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body d-md-flex flex-column p-0 pt-lg-3 overflow-y-auto">
          <ul class="nav flex-column">
            <li class="nav-item">
              <a class="nav-link d-flex align-items-center gap-2 active" aria-current="page" >
                <router-link to="/dashboard/product">
                  <svg class="bi"><use xlink:href="#house-fill"/></svg>
                  後台產品列表
                </router-link>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link d-flex align-items-center gap-2" >
                <router-link to="/">
                  <svg class="bi"><use xlink:href="#file-earmark"/></svg>
                  後台看訂單
                </router-link>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link d-flex align-items-center gap-2">
                <router-link to="/dashboard/coupon">
                  <svg class="bi"><use xlink:href="#file-earmark"/></svg>
                  後台優惠券
                </router-link>
              </a>
            </li>
          </ul>
          <hr class="my-3">

          <ul class="nav flex-column mb-auto">
            <li class="nav-item">
              <a class="nav-link d-flex align-items-center gap-2" >
                <router-link to="/dashboard/semiOrder">
                <svg class="bi"><use xlink:href="#door-closed"/></svg>
                模擬訂單
              </router-link>
              </a>
            </li>
          </ul>

          <hr class="my-3">

          <ul class="nav flex-column mb-auto">
            <li class="nav-item">
              <a @click.prevent="logOut()" class="nav-link d-flex align-items-center gap-2">
                <svg class="bi"><use xlink:href="#door-closed"/></svg>
                Sign out
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
      <router-view></router-view>
    </main>
  </div>
</div>


</template>

<style>
  @import "@/assets/Dashboard.scss";
</style>