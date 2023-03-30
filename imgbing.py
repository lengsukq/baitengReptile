import requests
from bs4 import BeautifulSoup
import os
import re
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44"
}

url = 'https://imgbin.com/'
r = requests.get(url, headers=headers)
r.encoding = r.apparent_encoding

parr = re.compile('src="(https://thumbnail.imgbin.com/.*?)".alt="(.*?)"')
image = re.findall(parr, r.text)
path = "imgbing图片"
print(r.text)
# if not os.path.isdir(path):  # 判断是否存在该文件夹，若不存在则创建
#     os.mkdir(path)  # 创建
#
# for i in image:
#     link = i[0]  # 获取链接
#     name = i[1]  # 获取名字
#
#     with open(path + "/{}.jpg".format(name), "wb") as img:
#         res = requests.get(link)
#         img.write(res.content)  # 将图片请求的结果内容写到jpg文件中
#         img.close()  # 关闭操作
#     print(name + ".jpg 获取成功······")