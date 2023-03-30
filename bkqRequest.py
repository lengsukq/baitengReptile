from bs4 import BeautifulSoup
import requests
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}
url = 'https://bj.ke.com/ershoufang/co32/'
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')

# 获取全部房源 所在的节点
sellList = soup.find(class_="sellListContent")
# 获取全部房源节点列表
lis = sellList.find_all('li', class_="clear")
# 选取第一个房源节点
div = lis[0].find('div', class_="info clear")
# 采集房源名称
title = div.find('div', class_="title")
print(title.text, 'div:', div)
