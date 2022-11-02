import docx 
document = docx.Document('./exam-question/Đại cương.docx')

for para in document.paragraphs:
    for run in para.runs:
        if run.bold:
            print(para.text)
            break
