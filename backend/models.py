
from typing import List
from typing import Any
from dataclasses import dataclass
@dataclass
class AnswerOption:
    answerText: str
    isCorrect: bool

    @staticmethod
    def from_dict(obj: Any) -> 'AnswerOption':
        _answerText = str(obj.get("answerText"))
        _isCorrect = obj.get("isCorrect")
        return AnswerOption(_answerText, _isCorrect)

@dataclass
class Root:
    questionText: str
    answerOptions: List[AnswerOption]
    questionID: int

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _questionText = str(obj.get("questionText"))
        _answerOptions = [AnswerOption.from_dict(y) for y in obj.get("answerOptions")]
        _questionID = int(obj.get("questionID"))
        return Root(_questionText, _answerOptions, _questionID)

class answer_class:
    def __init__(self, answerText, isCorrect):
        self.answerText = answerText
        self.isCorrect = isCorrect
class question_class:
    def __init__(self, questionText, questionID):
        self.questionText = questionText
        self.answerOptions = []
        self.questionID = questionID
class case_class:
    def __init__(self, question_group, question_group_text):
        self.question_group = question_group
        self.question_group_text = question_group_text
        self.ques = []


# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
