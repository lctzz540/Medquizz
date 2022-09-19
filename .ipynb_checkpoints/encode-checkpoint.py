import docx
from glob import glob
import os
import json


path_list = glob('./exam/'+"*.docx")
for path in path_list:
    f_name, f_ext = os.path.splitext(path)
    try:
        doc = docx.Document(path)
        data = ""
        fullText = {}
        cases_dict = {}
        cases_question = []
        for para in doc.paragraphs:
            if para.text.find("Tình huống") != -1:
                fullText[para.text] = []
            elif para.text.find(':') != -1 and para.text.find("Câu")!= -1:
                question = para.text.split(':')
                question[0] = int(''.join(filter(str.isdigit, question[0])))
                fullText[question[0]] = [question[1]]
            else:
                try:
                    if para.text != "":
                        fullText[list(fullText)[-1]].append(para.text)
                except:
                    pass
        for key in fullText.keys():
            try:
                if key.find("Tình huống") != -1:
                    cases_dict[key] = fullText[key]
                    cases_question.append(int(''.join(filter(str.isdigit, key))))
            except:
                pass
        for key in cases_dict.keys():
            fullText.pop(key)
        print(f_name)
        print(cases_dict)
        with open(f"{f_name}.json", "w") as outfile:
            json.dump(fullText, outfile)
        with open(f"{f_name+'cases'}.json", "w") as casesfile:
            json.dump(cases_dict, casesfile)
    except IOError:
        print('There was an error opening the file!')
