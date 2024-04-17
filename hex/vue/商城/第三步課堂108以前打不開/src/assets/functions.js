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
  console.log(greenToken)
    if(greenToken.length){
      let ans = greenToken[0].split("=");
      return ans[1]
    }

}


/*  更乾淨的getDot
    跟下面的區別是
    找到插入序列的規則
    作法:
    把目標變成序列並reverse 這樣才好push
    依照目標迭代成新序列
    迭代的規則是
    每個舊序列元素都先塞進去
    然後重點就是怎麼插入逗點
    在每個index為2 5 8 11 14 ....時
    都插入 
    但這邊沒有規則
    除非找到規則嘻嘻
    2 5 8 11 14
    3 6 9 12 15
    idx+1%3==0  就是插入逗號的時機  
    同時 必須符合 插入不能超過原有序列 就是不能出現  ,100,100  這種情形
    也就是不檢查最後一個idx
    
    function getDot(num){
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
      console.log(newLst)
    }
*/ 
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