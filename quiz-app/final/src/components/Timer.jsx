import React from 'react'

const Timer = (props) => {
  const minutes = Math.floor(props.timeleft / 60)
  const seconds = props.timeleft % 60
  const minutesDigits = minutes >= 10 ? String(minutes) : '0' + String(minutes)
  const secondsDigits = seconds >= 10 ? String(seconds) : '0' + String(seconds)
  return (
    <div
      style={{
        fontWeight: 'bold',
        display: 'inline-flex',
      }}
    >
      <span style={{ color: 'red' }}>{minutesDigits}</span>
      <span style={{ color: 'red' }}> :{secondsDigits}</span>
    </div>
  )
}

export default Timer
