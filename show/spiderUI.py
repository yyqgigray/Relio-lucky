import re
import tkinter as tk
from tkinter.filedialog import askdirectory


import spider.user.identify as identifyFunc
import spider.executor.spiderExecutor

class spiderUI():
    def __init__(self,parent):
        self.ACCESS_TOKEN = ''
        self.APP_KEY = '885969782'
        self.APP_SECRET = '5e01407952b6db77c2fdfc026c4ccf56'
        self.weiboID = ''
        self.TARGET_FILE_PATH = tk.StringVar()

        ButtonFrame = tk.Frame(parent,bg='gray',width='30',padx=5,pady=10)
        MsgFrame = tk.Frame(parent,bg='#b3b5b7',width='30',padx=5,pady=10,relief=tk.SUNKEN)
        TextFrame = tk.Frame(parent, bg='white', width='30', padx=5, pady=10)

        self.loginText = tk.Label(MsgFrame, text='未认证，请点击按钮进行认证' , background = 'red')

        loginButton = tk.Button(ButtonFrame, text="授权登录微博", command=self.identifyHandler, width=15)
        weiboIdInputButton = tk.Button(ButtonFrame, text="解析微博ID", command=self.getWeiboId, width=15)
        pathInputButton = tk.Button(ButtonFrame, text="评论存储路径选择", command=self.selectPath, width=15)
        getCommentsButton = tk.Button(ButtonFrame, text="爬取微博评论", command=self.getComments, width=15)

        weiboIdLabel = tk.Label(TextFrame, width=25, text='请在此处输入微博ID或者微博网址:')
        self.weiboIdInput = tk.Text(TextFrame, height=8)  # 微博链接输入框


        self.logWindow = tk.Text(TextFrame, height=20)  # 日志框

        ##  pack位置调整

        MsgFrame.pack(fill='x')
        ButtonFrame.pack(side=tk.LEFT,fill='y')
        TextFrame.pack(fill='x')

        loginButton.pack(pady=5)
        weiboIdInputButton.pack(pady=5)
        pathInputButton.pack(pady=5)
        getCommentsButton.pack(pady=5)
        self.loginText.pack(padx=5)

        weiboIdLabel.pack(fill='x')

        self.weiboIdInput.pack()
        self.logWindow.pack()
        parent.mainloop()


    def identifyHandler(self):
        self.ACCESS_TOKEN = identifyFunc.main()
        res = self.checkInput()
        self.showMsg(res)
        self.writelog("您已认证登录")


    def getWeiboId(self):
        weiboLink = self.weiboIdInput.get('0.0', 'end')
        pattern = re.compile(r'\d+')
        self.weiboID = pattern.findall(weiboLink)[0]
        res = self.checkInput()
        self.showMsg(res)
        self.writelog("解析出的微博ID为："+self.weiboID)


    def selectPath(self):
        path_ = askdirectory()
        self.TARGET_FILE_PATH.set(path_)
        res = self.checkInput()
        self.showMsg(res)
        self.writelog("爬取到的评论将存放在："+path_)


    def getComments(self):
        spiderExecutor = spider.SpiderExecutor(self.weiboID, self.TARGET_FILE_PATH, self.ACCESS_TOKEN, self.APP_KEY, self.APP_SECRET)
        spiderExecutor.main()

    def checkInput(self):
        checkRes = {
            'code': 0,
            'msg': '您已在正确的轨道上',
            'msgColor': 'green'
        }
        if(self.ACCESS_TOKEN == ''):
            checkRes['code'] = 1
            checkRes['msg'] = '未授权，请点击按钮进行授权登录'
            checkRes['msgColor'] = 'red'
            return checkRes

        if(len(self.weiboID) == 0):
            checkRes['code'] = 2
            checkRes['msg'] = '请输入微博ID或者链接'
            checkRes['msgColor'] = 'red'
            return checkRes

        if(len(self.TARGET_FILE_PATH.get()) == 0):
            checkRes['code'] = 3
            checkRes['msg'] = '请选择评论存储位置'
            checkRes['msgColor'] = 'red'
            return checkRes

        return checkRes

    def showMsg(self,checkRes):
        self.loginText.configure(text= "当前消息："+ checkRes['msg'], background = checkRes['msgColor'])

    def writelog(self,log):
        self.logWindow.insert(tk.INSERT, log+"\n")