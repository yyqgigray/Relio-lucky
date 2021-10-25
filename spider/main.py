import spider.user.identify as identifytor
import spider.executor.spiderExecutor

global ACCESS_TOKEN

APP_KEY = '885969782'
APP_SECRET = '5e01407952b6db77c2fdfc026c4ccf56'
ACCESS_TOKEN = '2.00juzNSG0MN8xx31ad8ccb9dlrfsPB'


ACCESS_TOKEN = identifytor.main()
print ("main.py-access_token:"+ACCESS_TOKEN)

spiderExecutor = spider.SpiderExecutor(WEIBO_ID, TARGET_FILE_PATH, ACCESS_TOKEN, APP_KEY, APP_SECRET)
spiderExecutor.main()