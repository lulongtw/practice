let data = function(x,y){
    return x+y
}

let a = 99
let b = 1

export default data
export {a,b}
/* 
或是寫成
export {data as default,a,b}
*/