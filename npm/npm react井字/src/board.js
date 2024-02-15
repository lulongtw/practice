import React from "react"
import Cell from "./cell.js"
import Svg from "./svg.js"


class Board extends React.Component{
    constructor(props){
      super(props)
      this.state={
        turn:0,
        marks:[-1,-1,-1,-1,-1,-1,-1,-1,-1],
        winner:null
      }
    }
    render(){
      let cells = []
      for (let i=0;i<this.state.marks.length;i++){
        cells.push(<Cell key={i} index={i} st={this.state.marks[i]} func={this.updt.bind(this)}/>)
      }
      if (this.state.winner==null){
        return <>
            <div className="board">{cells}</div>
          <div className="re" onClick={this.re.bind(this)}>REFRESH</div>
        </>
      }else{
        return <>
            <div className="board">{cells}
          <Svg start={this.state.winner.start} end={this.state.winner.end}/></div>
          <div className="re" onClick={this.re.bind(this)}>REFRESH</div>
          <div style={{fontSize:"50px",transform:"translate(300px,0px)"}}>winner is {this.state.winner.side}</div>
        </>
      }    
    }
    re(){
        this.setState({
            turn:0,
            marks:[-1,-1,-1,-1,-1,-1,-1,-1,-1],
            winner:null
        })
    }
    updt(idx){
        if (this.state.winner==null && this.state.marks[idx]==-1){
            this.setState((prest)=>{
                prest.marks[idx] = prest.turn%2
                prest.turn++
                return {
                    turn:prest.turn,
                    marks:prest.marks,
                    winner:this.winner(prest.marks)
                }
            })
        }
    }
    winner(mrks){
        let sd
        for (let x=0;x<3;x++){
          if (mrks[x*3]!=-1 && mrks[x*3]==mrks[x*3+1] && mrks[x*3+1]==mrks[x*3+2]){
            if (mrks[x*3]==0){
              sd=true}
            return {start:x*3 ,end:x*3+2 ,side:sd?"O":"X"}
          }
        }
        for (let y=0;y<3;y++){
          if (mrks[y]!=-1 && mrks[y]==mrks[y+3] && mrks[y+3]==mrks[y+6]){
            if (mrks[y*3]==0){
              sd=true}
            return {start:y , end:y+6 , side:sd?"O":"X"}
          }
        }
        if (mrks[0]!=-1 && mrks[0]== mrks[4] && mrks[4]==mrks[8]){
          if (mrks[0]==0){
              sd=true}
          return {start:0 , end:8 , side:sd?"O":"X"}
        }else if (mrks[2]!=-1 && mrks[2]==mrks[4] && mrks[4]==mrks[6]){
          if (mrks[2]==0){
              sd=true}
          return {start:2 , end:6 , side:sd?"O":"X"}
        } 
        return null
      }
    
    re(){
        this.setState((prest)=>{
            return{
                turn:0,
                marks:[-1,-1,-1,-1,-1,-1,-1,-1,-1],
                winner:null                
            }
        })
    }
  }

  export default Board
