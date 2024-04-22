import re

response="<img id=listimg4 src=/img/t.gif data-width=310 data-height=310 data-src=https://thumbnail.imgbin.com/24/3/14/international-tea-day-tea-day-8R63bTsH_t.jpg alt=&International Tea Day Tea Day PNG& />"

parr = re.compile(r'(?<=id(?=\s))')  # 匹配图片链接和图片名字
parr2 = re.compile('id=(.*?).src=(https://thumbnail.*?).alt=&(.*?)&')
image = re.findall(parr, response)
image2 = re.findall(parr2, response)
print(image)
print(image2)