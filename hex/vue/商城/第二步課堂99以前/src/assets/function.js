function noCatch(asFn){
  return asFn.catch(res=>{
    console.error("shit",res)
  })
}

function getCookie(name) {
  // 將 cookies 分割成陣列
  // console.log(document.cookie)
  let cookies = document.cookie.split('; ');
  // 遍歷 cookies 陣列
  // console.log(cookies)
  for (let i = 0; i < cookies.length; i++) {
    let cookie = cookies[i].split('=');
    // 檢查當前 cookie 的名稱是否匹配所需的 cookie
    if (cookie[0] === name) {
      return cookie[1];
    }
  }
  return null;
}

function a(name){
  let cookies = document.cookie.split("; ");
  let tar =  cookies.filter(item=>{
    let cookie = item.split("=");
    let cookieName = cookie[0];
    return name === cookieName
  })
  let ans = tar[0].split("=")
  return ans[1]
}

// // 使用示例
// let token = getCookie('token');
// console.log(token); // 如果存在名為 'token' 的 cookie，則輸出其值

import {Modal} from "bootstrap"

function hideModal(){
  let modalDOM = document.querySelector("#staticBackdrop");
  let modalInstance = Modal.getOrCreateInstance(modalDOM);
  modalInstance.hide()

}





export {noCatch,getCookie,a,hideModal}