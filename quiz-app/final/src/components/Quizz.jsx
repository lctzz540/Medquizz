import React, { useState, useEffect } from 'react'
import Score from './Score'
import Timer from './Timer'

const Quizz = (props) => {
  const questions = props.questionList
  const [currentQuestion, setCurrentQuestion] = useState(0)
  const [showScore, setShowScore] = useState(false)
  const [score, setScore] = useState(0)
  const [wrongAnswer, setWrongAnswer] = useState([])
  const [timeLeft, setTimeLeft] = useState(props.time)
  const handleAnswerOptionClick = (isCorrect) => {
    if (isCorrect) {
      setScore(score + 1)
    } else {
      setWrongAnswer(
        wrongAnswer.concat([
          [
            questions[currentQuestion].questionText,
            questions[currentQuestion].answerOptions.find(
              (element) => element.isCorrect === true
            ).answerText,
          ],
        ])
      )
    }

    const nextQuestion = currentQuestion + 1
    if (nextQuestion < questions.length) {
      setCurrentQuestion(nextQuestion)
    } else {
      setShowScore(true)
    }
  }

  useEffect(() => {
    if (timeLeft > 0 && props.clock) {
      setTimeout(() => setTimeLeft((timeLeft) => timeLeft - 1), 1000)
    } else {
      if (props.clock) setShowScore(true)
    }
  }, [timeLeft])

  return (
    <div className='quizz'>
      {showScore ? (
        <Score
          score={score}
          numberOfQuestions={questions.length}
          wrongAnswer={wrongAnswer}
        />
      ) : (
        <>
          <div className='question-section'>
            {props.clock ? <Timer timeleft={timeLeft} /> : <></>}
            <div className='question-count'>
              <span>Question {currentQuestion + 1}</span>/{questions.length}
            </div>
            <div className='question-text'>
              {questions[currentQuestion].questionText}
            </div>
          </div>
          <div className='answer-section'>
            {questions[currentQuestion].answerOptions.map((answerOption) => (
              <button
                onClick={() => handleAnswerOptionClick(answerOption.isCorrect)}
              >
                {answerOption.answerText}
              </button>
            ))}
          </div>
        </>
      )}
    </div>
  )
}

export default Quizz
