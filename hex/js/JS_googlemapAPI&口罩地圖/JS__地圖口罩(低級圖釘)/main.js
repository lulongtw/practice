let xhr = new XMLHttpRequest();
//xhr.overrideMimeType("application/json");
xhr.open("get", "https://raw.githubusercontent.com/kiang/pharmacies/master/json/points.json", true);
xhr.send(null);

let county = document.querySelector("[id='county']");
let town = document.querySelector("[id='town']");
let pharmacyList = document.querySelector(".pharmacyList");
let main = document.querySelector("main");


let obj = {};//obj是之後要用的資料
let markerList = [];//顯示在.pharmacyList裡面的藥局們的座標


  /*
  做成  物件>物件>序列
{
  acounty:{a1town:[醫院,醫院,醫院],
          a2town:[醫院,醫院,醫院]},
  bcounty:[a1town:[醫院,醫院,醫院],
          a2town:[醫院,醫院,醫院]}
}
*/


xhr.onload = function () {

  let data = JSON.parse(xhr.response).features;

  for (let i = 0; i < data.length; i++) {
    if (obj[data[i].properties.county]) {//先檢查obj是否已經建立縣市
      if (obj[data[i].properties.county][data[i].properties.town]) {//在檢查是否已經建立區鎮鄉
        obj[data[i].properties.county][data[i].properties.town].push(//若有就push
          data[i]
        );
      } else {//不然就建立 :縣市:區鄉鎮:[data]
        obj[data[i].properties.county][data[i].properties.town] = Array(
          data[i]
        );
      }
    } else {
      if (!(data[i].properties.county)){//如果沒有資料
        obj.沒有縣市資料 = {};//重點要先{} 不然第一個資料會混再一起
        obj.沒有縣市資料[data[i].properties.town] = Array(data[i])
      }else{//如果沒有此縣市，建立空集合，在復職
        obj[data[i].properties.county] = {}; 
        obj[data[i].properties.county][data[i].properties.town] = Array(data[i])
      }
    }
  }

  for (let key in obj) {//畫縣市select的option
    county.innerHTML += `
    <option value="${key}">${key}</option>
    `;
  }
  refreshTown()//畫區鄉鎮select的option
  markerList = getCurrentPharmacyList()//取得目前應該顯示的醫院座標
  refreshList();//畫應該出現在.pharmacyList裡的醫院
  initMap(markerList);//畫地圖
  //console.log(markerList)
};


county.addEventListener("change",()=>{refreshTown()});

town.addEventListener("change",()=>{
  refreshList();
  markerList = getCurrentPharmacyList();
  initMap(markerList);
})

pharmacyList.addEventListener("click",(e)=>{
  getRightDataSet(e)
})

function getRightDataSet(e){
  /*
  這跟之前在父元素設事件監聽取出子元素的dataset不太樣，
  因為這個有dataset的子元素中也有許多子元素，
  要馬每個子元素設dataset  要馬在每個phatmacy設事件觸發e.currentTarget
  都要批次作業
  最後找到這個  
  用.parentNode找父元素，
  如果父元素沒有dataset 就用while找到父元素為止
  我真屌
  */ 
  if (e.target.className!='pharmacyList'){
    let currentElement = e.target;
    if (currentElement.className!="pharmacy"){
      while(!currentElement.dataset.lat){
        currentElement = currentElement.parentNode;
      }
    }
    let lat = parseFloat(currentElement.dataset.lat);
    let lng = parseFloat(currentElement.dataset.lng);
    refreshMarker(lat,lng,markerList);
  }
}
/*
技術難題  因為不知道怎麼直接把map zoom 所以整個重劃
連帶marker也要重劃  跟initMap基本一樣  
只是在畫marker時，會檢查座標是否跟帶入的參數座標一樣
一樣就帶入icon
檢查
*/ 
async function refreshMarker(lat,lng,lst){
  console.log(lat,lng,lst)
  let currentCounty = county.value;
  let currentTown = town.value;
  let {Map} = await google.maps.importLibrary("maps");
  let map = new Map(main,{
    center:{lat:lat,lng:lng},
    zoom:18,
  });

  for (let i=0;i<lst.length;i++){
    //if (JSON.stringify(lst[i])==JSON.stringify([lng,lat])){ //lst之間比較要這樣搞
   if (lst[i][1]==lat && lst[i][0]==lng){
  
      new google.maps.Marker({
        title:obj[currentCounty][currentTown][i].properties.name,
        icon:"head-side-mask-solid.svg",
        position:{lat:lat,lng:lng},
        map:map,
      })
    }else{
      new google.maps.Marker({
        position:{lat:lst[i][1],lng:lst[i][0]},//也打成lat 造成全部都在一個點上 所以才回只會看到同一個也是最後一個title
        map:map,
        title:obj[currentCounty][currentTown][i].properties.name,
      })

    }
  }
}




function refreshTown(){
  town.innerHTML = "";
  let currentCounty = county.value;
  let lst = obj[currentCounty];
  for (let key in lst) {
    town.innerHTML += `
    <option value="${key}">${key}</option>
    `;
  };
  refreshList();
  markerList = getCurrentPharmacyList();
  initMap(markerList);
}



function getCurrentPharmacyList(){
  let currentCounty = county.value;
  let currentTown = town.value
  let lst = [];
  let data = obj[currentCounty][currentTown];
  for (let i=0;i<data.length;i++){
    lst.push(data[i].geometry.coordinates)
  }
  return lst;
}

function refreshList() {
  let currentCounty = county.value;
  let currentTown = town.value;
  pharmacyList.innerHTML = "";
  let lst = obj[currentCounty][currentTown];
  
    //  原本的 <div class="available" data-lat="${lst[i].geometry.coordinates[1]}" data-lng="${lst[i].geometry.coordinates[0]}" >${lst[i].properties.available}</div>
   // 是以文字呈現營業時間，getValidTime要把資料圖像化
   //先檢查每個是不是.aviable都長一樣  先用createelement 給.available設好tablecss  然後引入函式 給函式引入available參數  生成元素

   for (let i=0;i<lst.length;i++){
    let text = lst[i].properties.available;
    let table = validTimeInTable(text);
    let amount = lst[i].properties.mask_adult +lst[i].properties.mask_child;
    pharmacyList.innerHTML += `
    <div class="pharmacy" data-lat="${lst[i].geometry.coordinates[1]}" data-lng="${lst[i].geometry.coordinates[0]}">
      <div class="name">${lst[i].properties.name}</div>
      <div class="phone">${lst[i].properties.phone}</div>
      <div class="address">${lst[i].properties.address}</div>
      <div class=mask>${amount}個口罩</div>
      ${table.outerHTML}
    </div>
    ` 
    //outerHTML很屌  可以把在js create的整個元素 以變數形式放入innerHTML中  
  }
}


function validTimeInTable(text){//營業時間資料圖象化

  let valid = document.createElement("table");
  valid.innerHTML="<tr><th></th><th>一</th><th>二</th><th>三</th><th>四</th><th>五</th><th>六</th><th>日</th></tr>"
  let tr = document.createElement("tr")
  let openingTime = ["上午","下午","晚上"];
  let count = 0;
  for (let j=5;j<text.length;j+=8){
    if (text[j]=="看"){
      tr.innerHTML+=`<td class="valid"></td>`
    }else{
      tr.innerHTML+=`<td class="invalid"></td>`
    }
    if ((((j-5)/8)+1)%7==0){
      let time = document.createElement("td");
      time.textContent = openingTime[count];
      count+=1;
      tr.insertBefore(time,tr.firstChild)
      valid.innerHTML+=`${tr.outerHTML}`
      tr.innerHTML = ""//更屌的是這個,如果上面用appendChild 這行賦值""的話
      //valid.appednChild(tr) 會因為因為tr是用變數append  tr改動也會跟著連動  就做白工 所以上面要用innerHTML 上面用innHTML的話 就要用outerHTML搞
    }
  };
  return valid

}


async function initMap(lst){
  let currentCounty = county.value;
  let currentTown = town.value
  let {Map} = await google.maps.importLibrary("maps");

   let map = new Map(main,{
    center:{lat:lst[0][1],lng:lst[0][0]},
    zoom:15,
  });
  for (let i=0;i<lst.length;i++){
   let a =  new google.maps.Marker({
      position:{lat:lst[i][1],lng:lst[i][0]},
      map:map,
      title:obj[currentCounty][currentTown][i].properties.name,
    })

  }
}



