import os.path
import time

import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}


# url = 'https://movie.douban.com/celebrity/1275432/photos/'
# res = requests.get(url, headers=headers).text
# print('res', res)
# 是一个可以从HTML或XML文件中提取数据的Python库.
# 它能够通过你喜欢的转换器实现惯用的文档导航,查找,修改文档的方式.
# （官方）beautifulsoup是一个解析器，可以特定的解析出内容，省去了我们编写正则表达式的麻烦。
# soup=beautifulsoup(解析内容,解析器)
# 常用解析器：html.parser,lxml,xml,html5lib
# content = BeautifulSoup(res, "html.parser")
# print('content', content)
# find_all会将所有满足条件的值取出，组成一个list
# 获取全部符合规则的节点列表
# 使用attrs获取class等于cover的标签
# data = content.find_all('div', attrs={'class': 'cover'})
# print('data', data[0])
# print(data[0].find('img'))
# picture_list = []


# for d in data:
#     plist = d.find('img')['src']
#     # print('d.find(img)', d.find('img'))
#     picture_list.append(plist)
# print(picture_list)


def request_douban():
    page = 1
    # range(start, stop[, step])，分别是起始、终止和步长。
    for i in range(0, 904, 30):
        print('开始爬取第 %s 页' % page)

        # format是python2新增的一个格式化字符串的方法，相对于老版的 % 格式方法，它有很多优点。
        # 不需要理会数据类型的问题，在 % 方法中 % s只能替代字符串类型
        # 单个参数可以多次输出，参数顺序可以不相同
        # 填充方式十分灵活，对齐方式十分强大
        # 官方推荐用的方式， % 方式将会在后面的版本被淘汰

        url = 'https://movie.douban.com/celebrity/1275432/photos/?type=C&start={}&sortby=like&size=a&subtype=a'.format(
            i)
        res = requests.get(url, headers=headers).text
        data = get_poster_url(res)
        download_picture(data)
        page += 1
        time.sleep(1)


# 封装每一页获取图片的函数
def get_poster_url(res):
    content = BeautifulSoup(res, "html.parser")
    data = content.find_all('div', attrs={'class': 'cover'})
    picture_list = []
    for d in data:
        plist = d.find('img')['src']
        picture_list.append(plist)
    return picture_list


# 下载图片
def download_picture(pic_l):
    if not os.path.exists(r'景甜Pic'):
        os.mkdir(r'景甜Pic')
    for i in pic_l:
        pic = requests.get(i, headers=headers)
        p_name = i.split('/')[7]
        with open('景甜Pic\\' + p_name, 'wb') as f:
            f.write(pic.content)


if __name__ == '__main__':
    request_douban()
