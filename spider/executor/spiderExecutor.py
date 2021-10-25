import requests
import time
import random



class SpiderExecutor(object):
    APP_KEY = ''
    APP_SECRET = ''
    def __init__(self, WEIBO_ID, TARGET_FILE_PATH, ACCESS_TOKEN, APP_KEY, APP_SECRET):
        self.WEIBO_ID = WEIBO_ID
        self.TARGET_FILE_PATH = TARGET_FILE_PATH
        self.ACCESS_TOKEN = ACCESS_TOKEN
        SpiderExecutor.APP_KEY = APP_KEY
        SpiderExecutor.APP_SECRET = APP_SECRET

    def main(self):
        return self.getAllComments(self.WEIBO_ID, self.TARGET_FILE_PATH)


    def getAllComments(self,ID,DATA_PATH):
        OAUTH_URL1 = 'https://api.weibo.com/2/comments/show.json?access_token=%s&id=%s' % (SpiderExecutor.ACCESS_TOKEN, ID)

        print("spiderExecutor.py-url:"+OAUTH_URL1)
        COMMENT_REQ = requests.get(url=OAUTH_URL1)
        COMMENT_REQ1 = COMMENT_REQ.json()
        PAGE_TOTAL = COMMENT_REQ1['total_number']//100
        print("######总共需要抓取的页码数："+str(PAGE_TOTAL)+"######")
        i=1
        self.__clearData(DATA_PATH)
        while i <= PAGE_TOTAL:
            SpiderExecutor.__sleepApp()
            try:
                print("######循环抓取第：" + str(i) + "页######")
                OAUTH_URL = 'https://api.weibo.com/2/comments/show.json?access_token=%s&id=%s&count=100&page=%s' % (SpiderExecutor.ACCESS_TOKEN, ID, i)
                COMMENTS_LIST = self.__getComments(OAUTH_URL)
                self.__writeComments(COMMENTS_LIST, DATA_PATH)
                i = i + 1
            except():
                print(i + "page未抓取到")
                i = i + 1
        return 0

    def __getComments(self, URL):
        print("######开始抓取" +URL+ "链接的数据######")
        COMMENT_REQ = requests.get(url=URL)
        COMMENT_REQ1 = COMMENT_REQ.json()
        COMMENT_LIST = COMMENT_REQ1['comments']
        print("######抓取到" + str(len(COMMENT_LIST)) + "条数据######")
        return COMMENT_LIST


    def __writeComments(self, COMMENT_LIST, DATA_PATH):
        print("######开始写入数据######")
        with open(DATA_PATH, 'a',encoding='utf-8') as f:  ##追加的方式写入评论
            for comm in COMMENT_LIST:
                f.write(comm['text']) ##记录评论到文件中
                f.write('\n')
            f.close()
        print("######写入结束######")

    def __clearData(self, DATA_PATH):
        print("######开始清理文件数据######")
        with open(DATA_PATH, 'w', encoding='utf-8') as f:
            f.write('')
        f.close()
        print("######清理结束######")

    def __sleepApp(self):
        number = random.randint(1,4)
        time.sleep(number)
        print("sleep:"+ str(number) +"s")

