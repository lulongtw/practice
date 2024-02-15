import React from "react"


let cnts = ["css-loader","scss-loader","react-loader","babel-loader"]
let son = cnts.map((item,index)=>{
    return <li className="li" key={index}>{item}</li>
})

export default son