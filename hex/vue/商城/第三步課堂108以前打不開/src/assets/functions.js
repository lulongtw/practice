function noCatch(asFn){

    return asFn.catch(res=>{
      console.log("shit",res)
    })
  
}

function getCookie(name){
  let cookies = document.cookie.split("; ")
  let greenToken = cookies.filter(item=>{
    item = item.split("=");
    return item[0]===name
  })
  let ans = greenToken[0].split("=");
  return ans[1]
}

function getDot(str) {
  str = String(str).split("")
  let len = str.length;
  let newOne = []
  let numberOfDot = Math.floor(len / 3);
  if (len % 3 == 0) {
    numberOfDot -= 1;
  }
  len += numberOfDot;
  while (len >= 4) {
    len -= 4
    newOne.push(len);
  }
  newOne.reverse();
  for (let i = 0; i < newOne.length; i++) {
    str.splice(newOne[i], 0, ",")
  }
  str = str.join("")
  return str
}

export {noCatch,getCookie,getDot}