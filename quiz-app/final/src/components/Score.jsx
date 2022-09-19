import React from "react"

const Score = (props) => {
  return (
    <div>
				<div className='score-section' style={{paddingBottom:"50px"}}>
					You scored {props.score} out of {props.numberOfQuestions}. Let's' check your wrong answer below
				</div>
          {props.wrongAnswer.map((element) => (
          <div className='log-section'>
          <hr/>
            <span>{element[0]} : </span><div style={{color: "green"}}>Correct answer is: {element[1]}</div> <br></br>
          </div>
          ))}
    </div>
  )
}

export default Score
