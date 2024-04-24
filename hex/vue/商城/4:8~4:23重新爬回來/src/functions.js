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

function getDot(num){
  if (!isNaN(num)){
    let lst = String(num).split("");
    lst = lst.reverse();
    let len = lst.length;
    let newLst = [];
    lst.forEach((item,idx)=>{
      newLst.push(item);
      if ((idx+1)%3==0&&idx+1<len){
        newLst.push(",");
      }
    })
    newLst =  newLst.reverse().join("")
    return newLst
  }else{
    return "輸入數字"
  }

}

export {getData,headAPI,myAPI,getDot}