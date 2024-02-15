let select = document.querySelector("select");
let wrap = document.querySelector(".wrap")


let data = []
for (let i=0;i<temp.length;i++){
    if (data[temp[i].properties.cunli]){
        data[temp[i].properties.cunli].push(temp[i]);
    }else{
        data[temp[i].properties.cunli] = Array(temp[i]);
    }
};

select.innerHTML = ""
for (let key in data){
    select.innerHTML+=`<option value="${key}">${key}</option>`
}

//console.log(data)

select.onchange = function(e){
    wrap.innerHTML = ''
    let cunli = select[select.selectedIndex].value;
    //let cunli = e.target.value;
    for (let i=0;i<data[cunli].length;i++){
        wrap.innerHTML += `
        <div class="name">${data[cunli][i].properties.name}</div>
        <div class="address">${data[cunli][i].properties.address}</div>
        <div class="amask">${data[cunli][i].properties.mask_adult}</div>
        <div class="cmask">${data[cunli][i].properties.mask_child}</div>
        <div class="m" id="m${i}"></div>
        <div class="v" id="v${i}"></div>
        `
        let crds = data[cunli][i].geometry.coordinates
        //console.log(crds)
        initMap(i,crds)
        //之前把街景生成view(idx,crds)分開法
        //await也沒用 
        //媽的我五告ㄎ一ㄠˋ把view的內容放進initMap
        //這樣就可以了  為啥嗎
        //我想是不能wait兩個異步程式??
        //所以把兩個異步放起讓他等
    }
}


