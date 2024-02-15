
let wrap = document.createElement("div");

for (let i=0;i<data.length;i++){
    let name = data[i].properties.name;
    let phone = data[i].properties.phone;
    let address = data[i].properties.address;
    let valid = data[i].properties.available;
    let coords = [data[i].geometry.coordinates[0],data[i].geometry.coordinates[1]];
    wrap.innerHTML+=`
    <div class="name">${name}</div>
    <div class="phone">${phone}</div>
    <div class="address">${address}</div>
    <div class="valid">${valid}</div>
    <div class="map" id="#a${i}"></div>
    `
    initMap(i,coords)//丟id和座標近畫地圖程式 注意 data和程式的經緯度是相反的
    // 一定要傳入i 讓initmap用getId的方式獲取元素
    //不能在這邊使用querySelectorAll，再[i] 直接把目標元素丟進參數裡
    //即使在initmap 得出  目標元素  === getEleById 完全相等
    //不能用就是不能用
}


document.body.appendChild(wrap)
