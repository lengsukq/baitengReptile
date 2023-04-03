# 佰腾数据爬取
import xlsxwriter
import json
import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
# 加载json文件并读取
def resolveJson():
    with open(r'C:\code\python-crawler\baiten.json', 'r', encoding='utf8') as fp:
        json_data = json.load(fp)

    # 输出documents数组
    return json_data['cubePatentSearchResponse']['documents']

def get_id_desAn(json_list):
    k = 0
    info_list = []
    for item in json_list:
        # 分别获取标题、申请日、授权公告日、id、desAn、
        info_list.append({
            'tittle':item['field_values']["ti"],
            'application_date': item['hl_field_values']['ad'][0],
            'announcement_Day': item['hl_field_values']['pd'][0] if len(item['hl_field_values']['apd'][0])==0 else item['hl_field_values']['pd'][0] + '({})'.format(item['hl_field_values']['apd'][0]),
            'id':item['field_values']["id"],
            'desAn':item['field_values']['desAn'],
            })
        # print('第{}次循环'.format(k+1), info_list)
    return info_list


def create_excel(info_list):
    print('数据长度', len(info_list))
    # 创建工作表
    workbook = xlsxwriter.Workbook(r'C:\code\python-crawler\baiten.xlsx')
    # 默认创建sheet1
    worksheet = workbook.add_worksheet()
    # 创建sheet2
    worksheet.write(0, 0, '标题')  # 行号和列标均是从0开始
    worksheet.write(0, 1, '申请日')
    worksheet.write(0, 2, '授权公告日')
    k = 1
    worksheet.set_column(0, 0, 40)
    worksheet.set_column(2, 2, 20)
    for item in info_list:
        worksheet.write(k, 0, item['tittle'])
        worksheet.write(k, 1, item['application_date'])
        worksheet.write(k, 2, item['announcement_Day'])
        k = k + 1
    workbook.close()
    print('代码结束')


def get_patents_info():
    print('专利信息获取')
    # 登录时需要POST的数据
    data = {'un': '13185503973',
            'pw': 'heyyi128.',}
    # 登录时表单提交到的地址（用开发者工具可以看到）
    login_url = 'https://www.baiten.cn/sso/checkuser'

    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'}
    # 构造Session
    session = requests.Session()
    print('登录状况', session)
    # 在session中发送登录请求，此后这个session里就存储了cookie
    # 可以用print(session.cookies.get_dict())查看
    resp = session.post(login_url, data)

    url = "https://www.baiten.cn/patent/detail/479706c8b89416e1bf1ec05d2d3d598e3591f56553a36d61?sc=&fq=&type=&sort=&sortField=&q=%E5%94%90%E4%BA%BA%E7%A5%9E%E9%9B%86%E5%9B%A2&rows=100#1/CN201310380651.3/worth/index"
    # headers = {
    # 'Accept':'*/*',
    # 'Accept-Encoding':'gzip, deflate, br',
    # 'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'Connection':'keep-alive',
    # 'Host':'www.baiten.cn',
    # 'Referer':'https://www.baiten.cn/patent/detail/479706c8b89416e1bf1ec05d2d3d598e3591f56553a36d61?sc=&fq=&type=&sort=&sortField=&q=%E5%94%90%E4%BA%BA%E7%A5%9E%E9%9B%86%E5%9B%A2&rows=100',
    # 'sec-ch-ua-mobile':'?0',
    # 'sec-ch-ua':'"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    # 'sec-ch-ua-platform':'"Windows"',
    # 'Sec-Fetch-Dest':'empty',
    # 'Sec-Fetch-Mode':'cors',
    # 'Sec-Fetch-Site':'same-origin',
    # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44",
    # "cookie":"yunsuo_session_verify=2eb3d7f8174e7e1d5a0927da41b9aaf1; JSESSIONID=CB1829DD7378E71F3E3697D2334635FD; zlcp202333=true; BSESSION=4df0fc142e35f61d51cc0b837a20352255ec4f68cf10dc14",
    # }
    res = session.get(url).text
    content = BeautifulSoup(res, "html.parser")
    data = content.find_all('div', attrs={'class': 'worth-part no-border'})
    print('get_patents_info', data, content)

if __name__ == '__main__':
    # print('开始解析')
    # json_list = resolveJson()
    # info_list = get_id_desAn(json_list)
    # print('写入数据', info_list)
    # create_excel(info_list)
    get_patents_info()