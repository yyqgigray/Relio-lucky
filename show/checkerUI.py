# -*- coding: utf-8 -*-
# author:xl

import tkinter as tk

class CheckerUI():

    def __init__(self, parent):

        textInputWindow=tk.Text(parent,height=20,undo=1)       #文本输入框
        replaceOutputWindow=tk.Text(parent,height=20)   #替换文本输出框
        findOutputWindow=tk.Text(parent,height=20)      #校验错误输出框

        s1 = tk.Scrollbar(parent,command=textInputWindow.yview, orient="vertical")
        s2 = tk.Scrollbar(parent,command=replaceOutputWindow.yview, orient="vertical")
        s3 = tk.Scrollbar(parent,command=findOutputWindow.yview, orient="vertical")

        labelInput = tk.Label(parent,text="请在此粘贴需要处理的文本：")
        labelReplace = tk.Label(parent,text="替换过后的文本：")
        labelFind = tk.Label(parent,text="其他错误字符校验如下：",pady=10)

        btnReplace = tk.Button(parent, text="替换英文标点符号", command='')
        btnFind = tk.Button(parent, text="发现英文错误标点符号", command='')
        btnImport = tk.Button(parent, text="导入文件", command='')


        labelInput.grid(row=0,column=0,sticky=tk.W)
        labelReplace.grid(row=0,column=2,sticky=tk.W)
        labelFind.grid(row=4,column=0,sticky=tk.W)

        textInputWindow.grid(row=1,column=0)
        replaceOutputWindow.grid(row=1,column=2)
        findOutputWindow.grid(row=5,column=0)

        s1.grid(row=1, column=1, sticky="ns")
        s2.grid(row=1, column=3, sticky="ns")
        s3.grid(row=5, column=1, sticky="ns")

        btnImport.grid(row=3,column=0,sticky=tk.W)  # 显示按钮
        btnReplace.grid(row=3,column=2,sticky=tk.W)  # 显示按钮
        btnFind.grid(row=6,column=0,sticky=tk.W)  # 显示按钮


        textInputWindow.config(yscrollcommand=s1.set)
        replaceOutputWindow.config(yscrollcommand=s2.set)
        findOutputWindow.config(yscrollcommand=s3.set)



