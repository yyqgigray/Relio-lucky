import re
import tkinter as tk
import spider.user.identify as identifyFunc
import spider.executor.spiderExecutor

class spiderUI():
    def __init__(self,parent):
        self.ACCESS_TOKEN = ''
        self.APP_KEY = '885969782'
        self.APP_SECRET = '5e01407952b6db77c2fdfc026c4ccf56'


        ButtonFrame = tk.Frame(parent,bg='gray',width='30',padx=5,pady=10)
        TextFrame = tk.Frame(parent, bg='white', width='30', padx=5, pady=10)

        self.loginText = tk.Label(ButtonFrame, width=25, text='未认证，请点击按钮进行认证' , background = 'red')
        loginButton = tk.Button(ButtonFrame, text="授权登录微博", command=self.identifyHandler, width=10)
        weiboIdInputButton = tk.Button(ButtonFrame, text="爬取微博评论关键词", command=self.getWeiboId, width=15)

        weiboIdLabel = tk.Label(TextFrame, width=25, text='请在此处输入微博ID或者微博网址:')
        self.weiboIdInput = tk.Text(TextFrame, height=10)  # 微博链接输入框

        findOutputWindow = tk.Text(TextFrame, height=20)  # 校验错误输出框

        ##  pack位置调整
        ButtonFrame.pack(fill='x')
        TextFrame.pack(fill='x')

        loginButton.pack(side=tk.LEFT,ipadx=5,padx=5)
        weiboIdInputButton.pack(side=tk.LEFT,ipadx=5)
        self.loginText.pack(side=tk.RIGHT,ipadx=5,padx=5)

        weiboIdLabel.pack(fill='x')

        self.weiboIdInput.pack()
        findOutputWindow.pack()
        parent.mainloop()


    def identifyHandler(self):
        self.ACCESS_TOKEN = identifyFunc.main()
        if(self.ACCESS_TOKEN == ''):
            self.loginText.configure(text='未认证，请点击按钮进行认证', background='red')
        else:
            self.loginText.configure(text='已认证', background='green')

    def getWeiboId(self):
        weiboLink = self.weiboIdInput.get('0.0','end')
        if(len(weiboLink)==0):
            tk.messagebox.showinfo('请输入微博ID或者链接')
            return 0
        else:
            pattern = re.compile(r'\d+')
            weiboID = pattern.findall(weiboLink)[0]
            print(weiboID)

    def getComments(self,weiboID):
        spiderExecutor = spider.SpiderExecutor(weiboID, TARGET_FILE_PATH, self.ACCESS_TOKEN, self.APP_KEY, self.APP_SECRET)
