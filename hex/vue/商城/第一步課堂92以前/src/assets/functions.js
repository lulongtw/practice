function noCatch(asFn){
  return asFn.catch(res=>{
    console.log("shit",res)
  })
}



export {noCatch}