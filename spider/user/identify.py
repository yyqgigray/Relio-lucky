import requests
from selenium import webdriver
import re
APP_KEY = '885969782'
APP_SECRET = '5e01407952b6db77c2fdfc026c4ccf56'
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'  # 回调授权页面，用户完成授权后返回的页面


def identifyOauth():
    global browser
    OAUTH_URL = 'https://api.weibo.com/oauth2/authorize?client_id=%s&response_type=code&redirect_uri=%s' % (APP_KEY,CALLBACK_URL)
    print ("********访问授权页面**********"+OAUTH_URL)
    browser = webdriver.Chrome()
    browser.get(OAUTH_URL)
    pattern = "code="
    m = -1
    while(m == -1):
        OAUTH_URL = browser.current_url
        m = OAUTH_URL.find(pattern)

    print("********授权页面回调**********"+OAUTH_URL)
    userCode = OAUTH_URL[m+5:]
    print("********CODE值：**********" + userCode)
    ACCESS_TOKEN = getTokenCode(userCode)
    browser.close()
    return ACCESS_TOKEN

def getTokenCode(Code):
    OAUTH_URL = 'https://api.weibo.com/oauth2/access_token'

    postData = {
        'client_id' : APP_KEY,
        'client_secret' : APP_SECRET,
        'grant_type' : 'authorization_code',
        'redirect_uri' : CALLBACK_URL,
        'code' : Code
    }
    ACCESS_TOKEN_REQ = requests.post(url=OAUTH_URL ,data = postData)
    ACCESS_TOKEN = ACCESS_TOKEN_REQ.json()['access_token']
    print ("identify.py-access_token:"+ACCESS_TOKEN)
    return ACCESS_TOKEN


def main():
    return identifyOauth()

if __name__=='__main__':
    main()