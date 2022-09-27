from fastapi import FastAPI, UploadFile
import uvicorn
from controller import processFileUpload

app = FastAPI()

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


@app.get("/")
def hello():
    return 'This app is running'

@app.post("/upload-file")
async def create_upload_file(files: list[UploadFile]):
   return await processFileUpload(files)
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
