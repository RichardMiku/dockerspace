#coding=utf-8

import os
import re
import json
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

def getCookie():
    edge_options = EdgeOptions()
    edge_options.add_experimental_option("detach", True)

    # 设置 EdgeDriver 的路径为当前目录下的 msedgedriver.exe
    service = EdgeService(os.path.join(os.getcwd(), 'msedgedriver.exe'))

    url = "https://sso.douyin.com/?service=https://webcast.amemv.com"

    browser = webdriver.Edge(service=service, options=edge_options)
    browser.get(url)

    try:
        WebDriverWait(browser, 120).until(
            EC.url_contains('is_new_connect')
            #EC.url_contains('https://webcast.amemv.com')
        )
    except TimeoutException:
        print("Timed out waiting for page to load")

    # 登录完成后获取 Cookie
    cookies = browser.get_cookies()

    # 格式化 Cookie
    cookie_package = {}
    for cookie in cookies:
        cookie_package[cookie['name']] = cookie['value']

    # 关闭浏览器
    browser.quit()
    print(cookie_package)
    return cookie_package


def getRTMPurl(cookie_package):
    url = "https://webcast.amemv.com/webcast/room/get_latest_room/?ac=wifi&app_name=webcast_mate&version_code=2.2.9&device_platform=windows&webcast_sdk_version=1520&resolution=1920%2A1080&os_version=10.0.19043&language=zh&aid=2079&live_id=1&channel=online&device_id=3096676051989080&iid=1117559680415880"
    while True:
        data=json.loads(requests.post(url=url,cookies=cookie_package).text)
        if data["data"]["status"]==4:
            print("正在等待开播！")
        if data["data"]["status"]==1:
            return data["data"]["stream_url"]["rtmp_push_url"]
        time.sleep(3)

def reMatch(RTMPurl):
    pattern = r'(rtmp://.*?/game/)(stream-\d+\?\S+)'

    # 使用re.match进行匹配
    match = re.match(pattern, url)

    if match:
        domain = match.group(1)
        stream_params = match.group(2)
        
        print("Url:", domain)
        print("Key:", stream_params)
    else:
        print("无法匹配")

def main():
    cookie=getCookie()
    getRTMPurl(cookie)

if __name__=="__main__":
    main()