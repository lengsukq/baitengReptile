import requests
import re
import os

url = "https://pic.netbian.com/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}

response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding

"""
. 表示除空格外任意字符（除\n外）
* 表示匹配字符零次或多次
? 表示匹配字符零次或一次
.*? 非贪婪匹配
"""

# 编译正则表达式模式，返回一个对象。可以把常用的正则表达式编译成正则表达式对象，方便后续调用及提高效率。
# re.compile(pattern, flags=0)
# pattern 指定编译时的表达式字符串
# flags 编译标志位，用来修改正则表达式的匹配方式。支持 re.L|re.M 同时匹配
parr = re.compile('src="(/u.*?)".alt="(.*?)"')  # 匹配图片链接和图片名字

# re.findall()：函数返回包含所有匹配项的列表。返回string中所有与pattern相匹配的全部字串，返回形式为数组。
image = re.findall(parr, response.text)

path = "彼岸图网图片获取"
if not os.path.isdir(path):  # 判断是否存在该文件夹，若不存在则创建
    os.mkdir(path)  # 创建

# 对列表进行遍历
for i in image:
    link = i[0]  # 获取链接
    name = i[1]  # 获取名字
    """
    在文件夹下创建一个空jpg文件，打开方式以 'wb' 二进制读写方式
    @param res：图片请求的结果
    """
    with open(path + "/{}.jpg".format(name), "wb") as img:
        res = requests.get("https://pic.netbian.com" + link)
        img.write(res.content)  # 将图片请求的结果内容写到jpg文件中
        img.close()  # 关闭操作
    print(name + ".jpg 获取成功······")
