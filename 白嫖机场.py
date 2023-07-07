# 白嫖机场自动订阅
import os
import subprocess
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_edge_action(num=2):
    # 先切换到chrome可执行文件的路径
    # os.chdir(r"C:\Program Files (x86)\Microsoft\Edge\Application")
    # user-data-dir为路径
    # subprocess.Popen('msedge.exe --remote-debugging-port=9999 --user-data-dir="D:\AutomationProfile"')
    options = webdriver.EdgeOptions()  # 自定义加载项
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")  # 本地监听edge浏览器
    browser = webdriver.Edge(options=options)
    url = "https://xn--mesv7f5toqlp.com/#/plan/1"
    nowNum = 0

    while nowNum < num:
        browser.get(url)
        browser.implicitly_wait(120)
        browser.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[2]/div[1]/input').send_keys(
            'baipiao9356')
        browser.find_element(By.XPATH, '/html/body/div/div/main/div/div/div[2]/div[1]/button').click()
        WebDriverWait(browser, 120).until(EC.visibility_of(
            browser.find_element(By.XPATH, '/html/body/div/div/main/div/div/div[2]/div[2]/div[2]/div[2]/div[1]')))
        sleep(1)
        browser.find_element(By.XPATH, '/html/body/div/div/main/div/div/div[2]/div[2]/button').click()
        WebDriverWait(browser, 120).until(EC.visibility_of(
            browser.find_element(By.XPATH, '/html/body/div/div/main/div/div/div[1]/div[3]/div[2]/div[1]')))
        sleep(1)
        browser.find_element(By.XPATH, '/html/body/div/div/main/div/div/div[2]/div/button').click()
        WebDriverWait(browser, 120).until(EC.visibility_of(
            browser.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/div/div/div[4]/button')))
        sleep(1)
        nowNum = nowNum + 1
        print('第', nowNum, '次白嫖')


if __name__ == '__main__':
    print('开始执行')
    get_edge_action(90)
    print('结束')
