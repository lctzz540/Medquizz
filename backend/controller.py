import io
import json
import docx
import re
from models import case_class, question_class, answer_class

async def processFileUpload(files):
    global doc, fullText
    for file in files:
        if file.content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = docx.Document(io.BytesIO(await file.read()))
        try:
            fullText = []
            cases_dict = {}
            cases_list = []
            case_in = False
            case_ques_in = False
            case_end = -1
            true_answer = None
            case_list_out = []
            case_temp = 0
            for para in doc.paragraphs:
                try:
                    if (case_end + 1) == cases_list[-1].questionID:
                        case_ques_in = False
                except: pass
                try:
                    if case_in:
                        cases_dict[list(cases_dict)[-1]] = para.text
                        case_list_out.append(case_class([int(c) for c in case_temp], para.text))
                        case_in = False
                        case_ques_in = True
                        continue
                    if para.text.find("Tình huống lâm sàng") != -1:
                        case = re.findall(r"\d+",para.text)
                        cases_dict[str(case)] = 0
                        case_temp = case
                        case_in = True
                        case_end = case[-1]
                    elif para.text.find(':') != -1 and para.text.find("Câu") != -1 and case_ques_in == False:
                        question = para.text.split(':')
                        question[0] = int(''.join(filter(str.isdigit, question[0])))
                        fullText.append(question_class(question[1], question[0]))
                    elif para.text.find(':') != -1 and para.text.find("Câu") != -1 and case_ques_in == True:
                        question = para.text.split(':')
                        question[0] = int(''.join(filter(str.isdigit, question[0])))
                        cases_list.append(question_class(question[1], question[0]))
                        case_list_out[-1].ques.append(question_class(question[1], question[0]))
                    else:
                        try:
                            if para.text != "" and para.text != " " and case_ques_in == False:
                                fullText[-1].answerOptions.append(answer_class(para.text, False).__dict__)
                                for run in para.runs:
                                    if run.bold:
                                        fullText[-1].answerOptions[-1]['isCorrect'] = True
                                        break
                            if para.text != "" and para.text != " " and case_ques_in == True:
                                case_list_out[-1].ques[-1].answerOptions.append(answer_class(para.text, False).__dict__)
                                for run in para.runs:
                                    if run.bold:
                                        case_list_out[-1].ques[-1].answerOptions[-1]['isCorrect'] = True
                                        break
                        except:
                            pass
                except: print(para.text)

            for i in range(len(fullText)):
                fullText[i] = fullText[i].__dict__
           
            for i in range(len(cases_list)):
                cases_list[i] = cases_list[i].__dict__
            for i in range(len(case_list_out)):
                case_list_out[i] = case_list_out[i].__dict__
                for j in range(len(case_list_out[i]['ques'])):
                    case_list_out[i]['ques'][j] = case_list_out[i]['ques'][j].__dict__
        except:
            pass

        return json.dumps(fullText, ensure_ascii=False) 
