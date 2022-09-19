import docx
from glob import glob
import os
import json
import re
import pandas as pd


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

path_list = glob('./exam-question/'+"*.docx")
for path in path_list:
    f_name, f_ext = os.path.splitext(path)
    answer_correct = pd.read_excel(f_name+'.xlsx' , header=None) 
    answer_correct[1] = answer_correct[1].map({'A':0,'B':1,'C':2,'D':3})
    try:
        doc = docx.Document(path)
        data = ""
        fullText = []
        cases_dict = {}
        cases_list = []
        cases_question = {}
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
                    true_answer = answer_correct[1][question[0] - 1]
                elif para.text.find(':') != -1 and para.text.find("Câu") != -1 and case_ques_in == True:
                    question = para.text.split(':')
                    question[0] = int(''.join(filter(str.isdigit, question[0])))
                    cases_list.append(question_class(question[1], question[0]))
                    case_list_out[-1].ques.append(question_class(question[1], question[0]))
                    true_answer = answer_correct[1][question[0] - 1]
                else:
                    try:
                        if para.text != "" and para.text != " " and case_ques_in == False:
                            fullText[-1].answerOptions.append(answer_class(para.text, False).__dict__)
                            if len(fullText[-1].answerOptions) - 1 == true_answer:
                                fullText[-1].answerOptions[-1]['isCorrect'] = True
                        if para.text != "" and para.text != " " and case_ques_in == True:
                            case_list_out[-1].ques[-1].answerOptions.append(answer_class(para.text, False).__dict__)
                            if len(case_list_out[-1].ques[-1].answerOptions) - 1 == true_answer:
                                case_list_out[-1].ques[-1].answerOptions[-1]['isCorrect'] = True
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
            

        with open(f"./quiz-app/final/src/data/{f_name}.json", "w") as outfile:
            json.dump(fullText, outfile, indent=4, ensure_ascii=False)
        with open(f"./quiz-app/final/src/data/{f_name+'_cases_question'}.json", "w") as cases_questionsfile:
            json.dump(case_list_out, cases_questionsfile, indent=4, ensure_ascii=False)   
    except:
        pass
