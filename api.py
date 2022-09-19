from fastapi import FastAPI, File, UploadFile
import uvicorn
import docx

app = FastAPI()

@app.get("/")
def hello():
    return 'This app is running'

@app.post("/upload-file")
async def create_upload_file(file: UploadFile = File(...)):
    docx.Document(file.file)
    return {"Name": file.filename}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
