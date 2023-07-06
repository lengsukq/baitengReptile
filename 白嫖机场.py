# 白嫖机场自动订阅
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def get_edge_action():
    options = webdriver.EdgeOptions()  # 自定义加载项
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")  # 本地监听edge浏览器
    browser = webdriver.Edge(options=options)
    url = "https://xn--mesv7f5toqlp.com/#/plan/1"
    browser.get(url)
    sleep(3)
    browser.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[2]/div[1]/input').send_keys('baipiao9356')
    browser.find_element(By.XPATH, '/html/body/div/div/main/div/div/div[2]/div[1]/button').click()
    sleep(3)
    browser.find_element(By.XPATH, '/html/body/div/div/main/div/div/div[2]/div[2]/button').click()
    sleep(5)
    browser.find_element(By.XPATH, '/html/body/div/div/main/div/div/div[2]/div/button').click()

if __name__ == '__main__':
    print('开始执行')
    get_edge_action()
    print('结束')