


async function initMap(idx,crds) {
  // 官網不是importLibrary
  //而是使用方法??
  //let map = await new google.maps.Map(document.getEL........)
  //等於是const{Map}和let map那行融合  但是這樣只有最後一個才有地圖 = =

  const { Map } = await google.maps.importLibrary("maps");
  
  let map = new Map(document.getElementById(`m${idx}`), {
    center: { lat: crds[1], lng: crds[0] },
    zoom: 15,
  });

    new google.maps.Marker(
        {
            position:{ lat: crds[1], lng: crds[0] },
            map:map,
            title:"fsdf",
            
        }
    );
    await new google.maps.StreetViewPanorama(
      document.getElementById(`v${idx}`),
      {
        position: { lat: crds[1], lng: crds[0] },
        pov: { heading: 165, pitch: 0 },
        zoom: 1,
      },
    );
}
//以前長這樣
// async function initMap(idx,crds) {
//   //@ts-ignore

//   const { Map } = await google.maps.importLibrary("maps");
  
//   let map = new Map(document.getElementById(`m${idx}`), {
//     center: { lat: crds[1], lng: crds[0] },
//     zoom: 15,
//   });

//     new google.maps.Marker(
//         {
//             position:{ lat: crds[1], lng: crds[0] },
//             map:map,
//             title:"fsdf",
            
//         }
//     )
// }



// async function view(idx,crds) {

//  await new google.maps.StreetViewPanorama(
//     document.getElementById(`v${idx}`),
//     {
//       position: { lat: crds[1], lng: crds[0] },
//       pov: { heading: 165, pitch: 0 },
//       zoom: 1,
//     },
//   );
// }




