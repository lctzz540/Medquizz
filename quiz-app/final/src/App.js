import React, { useMemo, useState } from 'react'
import Quizz from './components/Quizz.jsx'
import { questions } from './data/questions.js'

export default function App() {
  const [numberOfQuestions, setNumberOfQuestions] = useState()
  const [clock, setClock] = useState()

  const handleChange = (e) => {
    setNumberOfQuestions(e.target.value)
  }
  const settime =
    numberOfQuestions === '30' ? 20 : numberOfQuestions === '60' ? 45 : 60
  const handleChangeSubject = (e) => e.target.value
  const questionList = useMemo(
    () => questions.sort(() => Math.random() - 0.5).slice(0, numberOfQuestions),
    [numberOfQuestions]
  )
  return (
    <div className='quizz'>
      {numberOfQuestions && settime && typeof clock !== 'undefined' ? (
        <Quizz questionList={questionList} time={settime * 60} clock={clock} />
      ) : (
        <div className='score-section'>
          <form>
            <h3>MedQuizz</h3>
            <select className='custom-select' onChange={handleChangeSubject}>
              <option value='Choice Subject'>Choice Subject</option>
              <option value='Phương tễ'></option>
            </select>
            <select className='custom-select' onChange={handleChange}>
              <option value='Choice'>Choice</option>
              <option value='30'>30</option>
              <option value='60'>60</option>
              <option value='90'>90</option>
            </select>
            {numberOfQuestions && (
              <div
                style={{
                  display: 'inline-flex',
                  paddingTop: '40px',
                }}
              >
                <button onClick={() => setClock(true)}>Time On</button>
                <button onClick={() => setClock(false)}>Time Off</button>
              </div>
            )}
          </form>
        </div>
      )}
    </div>
  )
}
