import React from "react"

class Svg extends React.Component{
    constructor(props){
      super(props)
    }
    render(){
      let x1 = this.props.start%3
      let y1 = Math.floor(this.props.start/3)
      let x2 = this.props.end%3
      let y2 = Math.floor(this.props.end/3)
      return <svg className="svg"><line x1={x1*100+50} y1={y1*100+50} x2={x2*100+50} y2={y2*100+50} strokeWidth="10px" stroke="red"/></svg>
    }
  }

  export default Svg