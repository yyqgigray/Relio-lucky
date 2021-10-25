import wordcloud


class WordCloudTool(object):

    def __init__(self,TARGET_DATA_PATH,TARGET_PNG_PATH):
        self.TARGET_DATA_PATH = TARGET_DATA_PATH
        self.TARGET_PNG_PATH = TARGET_PNG_PATH


    def __changeConfig(self,):
        return 0

    def __generatePng(self):
        c = wordcloud.WordCloud(background_color="white")  # 1.配置对象参数
        with open(self.TARGET_DATA_PATH, 'r',encoding='utf-8') as f:
            data = f.read()
        c.generate(data)  #2.加载词云文本
        c.to_file(self.TARGET_PNG_PATH)