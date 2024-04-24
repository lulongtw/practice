import axios from "axios";


let headAPI = import.meta.env.VITE_headAPI;
let myAPI = import.meta.env.VITE_myAPI;

function noCatch(asFn){
  return asFn.catch(err=>{
    console.log('shit',err)
  })
}
function getUrl(url){
  let ans = headAPI + url;
  ans = ans.replace('/:api_path',myAPI);
  return ans
}

async function getData(url,method,toSend){
  let res = await noCatch(axios[method](url,toSend));
  return res
}




export {getData,getUrl}
