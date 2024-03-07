import axios from "axios";

async function getData(method,url,info=null){
  try{
    let temp = await axios[method](url,info);
    return temp
  }catch(res){
    console.log("shit",res)
  }
}

export {getData}