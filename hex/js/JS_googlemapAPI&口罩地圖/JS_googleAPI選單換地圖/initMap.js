let map;


async function initMap(lat,lng,div) {
  //@ts-ignore

  const { Map } = await google.maps.importLibrary("maps");

  map = new Map(div, {
    center: { lat: lat, lng: lng },
    zoom: 15,
  });

    new google.maps.Marker(
        {
            position:{ lat: lat, lng: lng },
            map:map,
            title:"fsdf",
            
        }
    )
        




}


