<script setup>
	import {ref,onMounted,inject,watch} from "vue";
  import {headAPI,myAPI,getData,getDot} from "@/functions.js";
  import {useRouter} from "vue-router";
	import {Modal} from "bootstrap";
	import seeMoreModal from "@/modal/seeMoreModal.vue";

	let data = ref([]);
	let currentPage = ref(1);
	let toggleLoading = inject('toggleLoading');
	let seeMoreItem = ref({});


	onMounted(async()=>{
		await getProduct()
	});

	function seeMore(item){
		seeMoreItem.value = item;
		let htmlDOM = document.querySelector("#seeMoreModal");
	//	console.log(htmlDOM)
		let modalDOM = Modal.getOrCreateInstance(htmlDOM)
		modalDOM.show();

	}

	async function getProduct(){
		toggleLoading()
		let url = `${headAPI}/api${myAPI}/products?page=${currentPage.value}`;
		let method = 'get';
		let res = await getData(url,method);
		if (res.data.success){
			data.value = res.data.products;
		}
		toggleLoading()
	}
</script>
<template>
	<seeMoreModal :fromDad="seeMoreItem"></seeMoreModal>
	<div class="buyerWrap">
		<div class="product" v-for="(item,idx) in data">
			<div class="pic">
				<img :src="item.imageUrl" alt="">
			</div>

			<div class="wordWrap">
				<div class="title">{{item.title}}</div>
				<div class="unit">{{item.category}}</div>
				<div class="content">{{item.content}}</div>
				<div class="originPrice">{{item.origin_price}}</div>
				<div class="price">{{item.price}}</div>
				<div class="buttons">
					<button @click="seeMore(item)" type="button" class="btn btn-outline-warning btn-sm"  
					style="--bs-btn-padding-y: .35rem; --bs-btn-padding-x: .5rem; --bs-btn-font-size: .8rem;">see more</button>
					
					<button type="button" class="btn btn-outline-info btn-sm " style="--bs-btn-padding-y: .35rem; --bs-btn-padding-x: .5rem; --bs-btn-font-size: .8rem;">to cart</button>
				</div>
			</div>

		</div>
	</div>
		
	
</template>
<style scoped>
	.buyerWrap{
		width:min(90%,800px);
		margin:50px auto;
	
		justify-content: center;
		display: flex;
		flex-wrap:wrap;
		gap:10px;
		align-items:stretch;
	}
	.product{
		width:30%;
		border:1px solid black;
		display: grid; 
  	grid-template-rows: auto 1fr; 

	}
	.wordWrap{
		display:grid;
		grid-template-columns:6fr 4fr;
		padding:5px;
		row-gap:10px;
	
		/* height:200px; */

	}
	.pic{
		background-color: red;
	}

	img{
		width:100%;
		height:140px;
		object-fit: cover;
	}
	.unit,.price{
		text-align:right;
	}
	.originPrice{
		grid-column:1
	}
	.buttons{
		grid-column:span 2;
		display:flex;
		background-color: rgb(75, 0, 0);
		padding:5px;
		gap:10px;
		justify-content: space-between;
	}


</style>