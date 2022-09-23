from fastapi import FastAPI, File, UploadFile
import uvicorn
import docx
import io
import json

app = FastAPI()

@app.get("/")
def hello():
    return 'This app is running'

@app.post("/upload-file")
async def create_upload_file(files: list[UploadFile]):
    global doc
    for file in files:
        if file.content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = docx.Document(io.BytesIO(await file.read()))
    # return json.dumps({"content": files[0].content_type}, indent=4, ensure_ascii=False)
    return {"content_type": doc.paragraphs[0].text}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
