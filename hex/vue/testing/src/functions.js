import axios from 'axios';

let headAPI = import.meta.env.VITE_headAPI;
let myAPI = import.meta.env.VITE_myAPI;

async function getData(url,method,toSend){
  let ans
  await axios[method](url,toSend).then(
    res=>{
      ans = res
    }
  ).catch(error=>{
    console.error('shit',error)
  })
  return ans
}

export {getData,headAPI,myAPI}