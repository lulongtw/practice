import {Modal} from "bootstrap";
import axios from "axios";

function noCatch(asFn){
  return asFn.catch(res=>{
    console.log("shit",res)
  })
}



function modalAct(act,id){
  let modalDOM = document.querySelector(`#${id}`);
  let modalInstance = Modal.getOrCreateInstance(modalDOM);
  if (act=="show"){
    modalInstance.show()
  }else if (act=="hide"){
    modalInstance.hide()
  }
}

async function getData(act,url,info=null){
  let data
  try{
    await axios[act](url,info)
      .then(res=>{
        data = res
    })
  }catch(error){
    console.log("shit",error)
  }
  return data
}


export {noCatch,modalAct,getData}