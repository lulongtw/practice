let ul = document.createElement("ul")
let contents = ["css loader","sass loader","babel loader"]
for (let i=0;i<contents.length;i++){
    let li  =document.createElement("li")
    li.textContent=contents[i]
    ul.appendChild(li)
}
export default ul