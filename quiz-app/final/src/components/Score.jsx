import React from 'react'

const Score = (props) => {
  return (
    <div>
      <div className='score-section' style={{ paddingBottom: '50px' }}>
        You scored {props.score} out of {props.numberOfQuestions}. Let's' check
        your wrong answer below
      </div>
      {props.wrongAnswer.map((element) => (
        <div
          className='log-section'
          style={{ border: '1px solid', padding: '10px', margin: '10px' }}
        >
          <div style={{ maxWidth: '100%' }}>{element[0]} : </div>
          <div style={{ display: 'grid', gridTemplateColumns: '50% 50%' }}>
            <div
              style={{
                color: 'red',
                margin: '20px',
              }}
            >
              Your choice: {element[2]}
            </div>
            <div
              style={{
                color: 'green',
                margin: '20px',
              }}
            >
              Correct answer is: {element[1]}
            </div>
          </div>
          <br></br>
        </div>
      ))}
    </div>
  )
}

export default Score
