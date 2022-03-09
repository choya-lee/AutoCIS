# -*- coding: utf-8 -*-

import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def chrome_driver():
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])  # webdriver防检测
    # option.add_argument('--headless')
    # option.add_argument('--disable-gpu')
    # option.add_argument("window-size=1920,1080")
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-dev-usage")
    # desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
    # desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
    driver = webdriver.Chrome(options=option)
    return driver


def pojie_signin():
    cookie = os.getenv('PJC')

    if cookie:
        wd = chrome_driver()
        wd.get('https://www.52pojie.cn/forum.php')
        cookie = cookie.split(';')
        for c in cookie:
            a = c.split('=')
            if a[0].strip() == 'htVC_2132_auth' or a[0].strip() == 'htVC_2132_saltkey':
                cookie_dict = {'name': a[0].strip(), 'value': a[1].strip()}
                wd.add_cookie(cookie_dict)
        wd.refresh()

        try:
            try:
                wd.find_element(By.XPATH, '//div[@id="um"]/p/strong/a')               
            except:
                raise Exception('获取用户名失败，cookie失效\n')
            wd.find_element(By.CLASS_NAME, 'qq_bind').click()
            sleep(1)
            print('Script executed successfully')           
        except Exception as e:
            print(e)
        wd.quit()


if __name__ == '__main__':

    pojie_signin()
    
