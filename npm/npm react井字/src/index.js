import "./style.scss"
import ReactDOM from "react-dom/client"
import Board from "./board.js"
import React from "react"



let con = document.getElementById("a")
let rt = ReactDOM.createRoot(con)
rt.render(<Board/>)