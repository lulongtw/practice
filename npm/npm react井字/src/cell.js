import React from "react"

class Cell extends React.Component{
    constructor(props){
      super(props)
    }
    render(){
      let text=""
      if (this.props.st==0){
        text="O"
      }else if (this.props.st==1){
        text="X"
      }
      return <div className="cell" onClick={this.click.bind(this)}>{text}</div>
    }
    click(){
      this.props.func(this.props.index)
    }
  }

  export default Cell