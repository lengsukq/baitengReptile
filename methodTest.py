import re

response="<img id=listimg4 src=/img/t.gif data-width=310 data-height=310 data-src=https://thumbnail.imgbin.com/24/3/14/international-tea-day-tea-day-8R63bTsH_t.jpg alt=&International Tea Day Tea Day PNG& />"

parr = re.compile(r'data-width=(.*?)data-height.src=(https://thumbnail.*?).alt=&(.*?)&')  # 匹配图片链接和图片名字

image = re.findall(parr, response)
print(image)