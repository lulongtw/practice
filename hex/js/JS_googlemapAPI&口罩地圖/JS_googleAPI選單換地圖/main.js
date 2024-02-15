let select = document.querySelector("select");
select.onchange = function(e){
    let tar = select[select.selectedIndex];
    let lat = parseFloat(tar.dataset.lat);
    let lng = parseFloat(tar.dataset.lng);
    let div = document.querySelector("div")
    initMap(lat,lng,div)
}