const path = require("path")
module.exports = {
    mode:"development",
    entry:"./asrc/aindex.js",
    output:{
        filename:"amain.js",
        path:path.resolve(__dirname,"adist")
    }
}