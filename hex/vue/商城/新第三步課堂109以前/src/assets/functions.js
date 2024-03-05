import {Modal} from "bootstrap";

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


export {noCatch,modalAct}