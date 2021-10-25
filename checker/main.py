# -*- coding: utf-8 -*-
# author:xl

import function as fun
import paramSet as param
import string
from tkinter import filedialog
import inputMod as inputM



def writeInput(content):
    textInputWindow.insert(1.0,content)

def getTextInput():
    result = textInputWindow.get("1.0","end")    #获取文本框输入的内容
    print(result)
    return result


def replaceMain():
    inputContent = getTextInput()
    replaceResult = fun.replaceContent(inputContent,param.replaceArr,param.regdict)
    replaceOutputWindow.delete(1.0, "end")
    replaceOutputWindow.insert(1.0, replaceResult)

def findMain():
    inputContent = getTextInput()
    findOutputWindow.tag_config("errTag", foreground='white', background='red')
    findOutputWindow.delete(1.0, "end")
    start = 0
    for i in range(len(inputContent)):
        if (string.punctuation).find(inputContent[i]) >= 0:
            findOutputWindow.insert(tk.END,inputContent[start:i])
            findOutputWindow.insert(tk.END,"【标点>"+inputContent[i]+"<错误】","errTag")
            start = i


def importFile():
    fileContent = inputM.importFile(filedialog)
    writeInput(fileContent)


