import {ref} from "vue"

function noCatch(asFn){
  return asFn.catch(error=>{
    console.log('shit',error)
  })
};


export {noCatch}