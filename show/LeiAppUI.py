import tkinter as tk
import checkerUI
import spiderUI


class basedesk():
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title("小雷专属工具箱V2.0")
        self.root.geometry('1280x720')
        initface(self.root)



class initface():
    def __init__(self, master):
        self.master = master

        mebubar = tk.Menu(self.master)

        # 设置menu1属性
        menu1 = tk.Menu(self.master, tearoff=0)
        handler1 = lambda: self.openFrame('checker')
        menu1.add_command(label="打开", command=handler1)

        # 设置menu2属性
        menu2 = tk.Menu(self.master, tearoff=0)
        handler2 = lambda: self.openFrame('spider')
        menu2.add_command(label="打开", command=handler2)

        # 添加菜单
        mebubar.add_cascade(label="专属校验器", menu=menu1)
        mebubar.add_cascade(label="专属词云生成器", menu=menu2)

        self.master.config(menu=mebubar)
        # 基准界面initface
        self.initface = tk.Frame(self.master, )
        self.initface.pack()

    def openFrame(self,toolName):
        top = tk.Toplevel()

        if(toolName == 'checker'):
            top.title('小雷专属校验器')
            checkerUI.CheckerUI(top)
        elif(toolName == 'spider'):
            top.title('小雷专属爬虫')
            spiderUI.spiderUI(top)



if __name__ == '__main__':
    root = tk.Tk()
    basedesk(root)
    root.mainloop()
