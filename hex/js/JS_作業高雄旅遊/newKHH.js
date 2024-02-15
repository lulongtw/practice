let xhr = new XMLHttpRequest();
xhr.overrideMimeType("application/json");
xhr.open("get", "test.JSON", true);
//xhr.open("get","https://api.kcg.gov.tw/api/service/get/9c8e1450-e833-499c-8320-29b36b7ace5c",true);
xhr.send(null);

let data = [];//所有資料 型態為["區碼1":[{資料1},{資料2}...],"區碼2":[{資料1},{資料2}...],....]

let select = document.querySelector("select");
let firstNav = document.querySelector(".firstnav");
let distWrap = document.querySelector(".distwrap");
let secondNav = document.querySelector(".secondnav");

//刷新畫面必要的 區碼 和 第幾個到第幾個資料的索引
let z_code = "807"
let page = 8

//如果有非免費入園的資料，則讓使用者手動點選顯示
/*

*/
let ticketlst = [];//該頁非免費入園的ticket資料序列
let toBeRemoved = []//一但使用者點擊畫面，購票資訊出現在畫面上，即刻存入此list，待下次點擊移除



//取得資料，並畫上畫面
xhr.onload = function () {
  temp = JSON.parse(xhr.response).data.XML_Head.Infos.Info;
  for (let i = 0; i < temp.length; i++) {
    if (data[temp[i].Zipcode]) {
      data[temp[i].Zipcode].push(temp[i]);
    } else {
      data[temp[i].Zipcode] = Array(temp[i]);
    }
  }

  console.log(data)

  for (let key in data) {
    name = codeToName(key);
    select.innerHTML += `<option value="${key}">${name}</option>`;
  }
  addToScreen(z_code, 8);
	refreshSecondNav(z_code)//頁數導覽頁刷新，因為頁數是要照資料長度，所以要等資料出來後才能處理
};

select.onchange = function (e) {
	page=8;
  z_code = e.target.value;
  addToScreen(z_code, page);
  refreshSecondNav(z_code);
};

firstNav.addEventListener("click", (e) => {
	page=8
  if (e.target.className == "hotnavs") {
    z_code = e.target.dataset.idx;
    addToScreen(z_code, page);
    refreshSecondNav(z_code);
  }
});

secondNav.addEventListener("click",(e)=>{
	if (e.target.dataset.step=="minus"){
		page-=16;
		if (page<8){
			alert("first page")
			page=8;
		}	
	}else if(e.target.dataset.step=="plus"){
		page+=8;
    if (page>(data[z_code].length+8)){
      page-=8;
      alert("last page");
      return
    }
	}else if(e.target.className=="page"){
		page = e.target.dataset.page;
	}
	addToScreen(z_code,page)

})


distWrap.onclick = function(e){
  if (e.target.className=="des4"){
  let show = ticketlst[e.target.dataset.idx]
   show.style.top = e.pageY + 'px';
   show.style.left = e.clientX + "px";
   document.body.appendChild(show);
   toBeRemoved.push(show);
  }
}

distWrap.onmouseup = function(){
  if (toBeRemoved.length!=0){ //即使是空list[]也不會false 超奇怪
    document.body.removeChild(toBeRemoved[0]);
    toBeRemoved.splice(0,1)
  }
}


function refreshSecondNav(code){
	let pageWrap = document.querySelector(".pagewrap");
  pageWrap.innerHTML = ""
	let amount = Math.ceil(data[code].length/8);

	for (let i=0;i<amount;i++){
		pageWrap.innerHTML+=`<div class="page" data-page=${(i+1)*8}>${i+1}</div>`
	}

}




function addToScreen(code, num) {
  distWrap.innerHTML = "";
  let distName = document.querySelector(".distname");
  distName.textContent = codeToName(code);
  let name = codeToName(code);
  let choosed = data[code];

  for (let i = num - 8; i < choosed.length && i < num; i++) {
		let ticket = choosed[i].Ticketinfo;

		if (ticket=="" || ticket=="免費參觀"){
			ticket = "免費參觀";
		}else{
			ticket = "更多資訊";
		}
		//傻眼沒寫.innerHTML

    distWrap.innerHTML += `
		<div class="attr">

			<div class="attrpic" style="background-image:url(${choosed[i].Picture1})">
					<div class=attrname>${choosed[i].Name}</div>
					<div>${name}</div>
			</div>

			<div class="attrcnt">
					<img src="./assets/icons_clock.png" alt=""><div class="des1">${choosed[i].Opentime}</div>
					<img src="./assets/icons_pin.png" alt=""><div class="des2">${choosed[i].Add}</div>
					<img src="./assets/icons_phone.png" alt=""><div class="des3">${choosed[i].Tel}</div>
					<img src="./assets/icons_tag.png" alt=""><div class="des4">${ticket}</div>
			</div>

		</div>
		`
		if (ticket=="更多資訊"){
      
      let des4 = document.querySelectorAll(".des4");
			let showBlock = document.createElement("div");
			showBlock.classList.add("showblock");
			showBlock.textContent = choosed[i].Ticketinfo;	
      ticketlst.push(showBlock);//在每次迭代內  在ticklst內新增非免費資料
      des4[i%8].dataset.idx = ticketlst.length-1//將該筆資料的index設為該元素的data 方便之後獲取
      /*
      console.log(des4[i%8]);
      des4[i%8].onclick = function(){
        console.log("sad")
      }
        為啥無法上事件監聽
      */ 
     
		}
  }
	
}



function codeToName(code) {
  switch (true) {
    case code == "800":
      return "新興區";
    case code == "801":
      return "前金區";
    case code == "802":
      return "苓雅區";
    case code == "803":
      return "鹽埕區";
    case code == "804":
      return "鼓山區";
    case code == "805":
      return "旗津區";
    case code == "806":
      return "前鎮區";
    case code == "807":
      return "三民區";
    case code == "811":
      return "楠梓區";
    case code == "812":
      return "小港區";
    case code == "813":
      return "左營區";
    case code == "814":
      return "仁武區";
    case code == "815":
      return "大社區";
    case code == "817":
      return "東沙群島";
    case code == "819":
      return "南沙群島";
    case code == "820":
      return "岡山區";
    case code == "821":
      return "路竹區";
    case code == "822":
      return "阿蓮區";
    case code == "823":
      return "田寮區";
    case code == "824":
      return "燕巢區";
    case code == "825":
      return "橋頭區";
    case code == "826":
      return "梓官區";
    case code == "827":
      return "彌陀區";
    case code == "828":
      return "永安區";
    case code == "829":
      return "湖內區";
    case code == "830":
      return "鳳山區";
    case code == "831":
      return "大寮區";
    case code == "832":
      return "林園區";
    case code == "833":
      return "鳥松區";
    case code == "840":
      return "大樹區";
    case code == "842":
      return "旗山區";
    case code == "843":
      return "美濃區";
    case code == "844":
      return "六龜區";
    case code == "845":
      return "內門區";
    case code == "846":
      return "杉林區";
    case code == "847":
      return "甲仙區";
    case code == "848":
      return "桃源區";
    case code == "849":
      return "那瑪夏區";
    case code == "851":
      return "茂林區";
    case code == "852":
      return "茄萣區";
    default:
      console.log(code);
  }
}
