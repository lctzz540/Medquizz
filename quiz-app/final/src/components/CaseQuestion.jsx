import React, { useState } from "react"
import giaibieu_cases from '../data/Giải biểu_cases_question.json'

const cases_question = giaibieu_cases
const [currentCase, setCurrentCase] = useState(0)
const [numberofanswered, setNumberOfAnswered] = useState(0)

const handleAnswerOptionClick = (isCorrect) => {
  if (isCorrect) {
			setScore(score + 1);
      setNumberOfAnswered(numberofanswered + 1)
		}else {
      setWrongAnswer(wrongAnswer.concat([[questions[currentQuestion].questionText,
        questions[currentQuestion].answerOptions.find((element) => element.isCorrect === true).answerText]]
      )
      )
    }

		if (numberofanswered < cases_question.length) {
			setCurrentCase(currentCase +1);
		} else {
			setShowScore(true);
		}
}

const CaseQuestion = () => {
  return (
    <div>
      <div className='question-section'>
				<div className='question-count'>
					<span>Case {currentCase + 1}</span>/{cases_question.length}
						</div>
        <div className='question-text'>{cases_question[currentCase].question_group_text}</div>
          {cases_question[currentCase].map(
                  (question) => (
                    <>
                      <div className='question-text'>{question.question_text}</div>
                      <div className='answer-section'>
						              {question.answerOptions.map((answerOption) => (
							              <button onClick={() => handleAnswerOptionClick(answerOption.isCorrect)}>{answerOption.answerText}</button>
						                  )
                            )
                          }
					            </div>
                    </>
                  )
                )
              }
					</div>
    </div>
  )
}

export default CaseQuestion
