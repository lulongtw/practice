import "./a.css";
import imgPath from "./assets/pic.png";

let img = new Image();
img.src = imgPath;

let div = document.querySelectorAll("div");
div[0].appendChild(img);