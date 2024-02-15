let data = {};
let sel = document.querySelector("select");

let temp =  await getData();
refreshSelect(temp);


sel.onchange = (e) => {
  initMap(e.target.value);
};



async function getData() {
  try {
    let ans = await axios.get("./temp.js");
    return ans.data
    
  } catch (error) {
    console.error("shit", error);
  }
}

function refreshSelect(temp) {
  for (let item of temp) {
    if (data[item.properties.cunli]) {
      data[item.properties.cunli].push(item);
    } else {
      data[item.properties.cunli] = [];
      data[item.properties.cunli].push(item);
    }
  }

  for (let key in data) {
    sel.innerHTML += `
    <option value='${key}'>${key}</option>
  `;
  }
}




  async function initMap(val) {
    let wrap = document.querySelector(".wrap");
    let map;
    const position = {
      lat: data[val][0].geometry.coordinates[1],
      lng: data[val][0].geometry.coordinates[0],
    };
    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerView } = await google.maps.importLibrary("marker");

    map = new Map(wrap, {
      zoom: 16,
      center: position,
      mapId: "DEMO_MAP_ID",
    });

    for (let item of data[val]) {
      const marker = new AdvancedMarkerView({
        map: map,
        position: {
          lat: item.geometry.coordinates[1],
          lng: item.geometry.coordinates[0],
        },
        title: item.properties.name,
      });
    }
  }


