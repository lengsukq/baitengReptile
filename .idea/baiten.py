# 佰腾数据爬取
import xlsxwriter
import json
import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# 加载json文件并读取
def resolveJson():
    with open(r'C:\code\python-crawler\baiten.json', 'r', encoding='utf8') as fp:
        json_data = json.load(fp)

    return json_data['cubePatentSearchResponse']['documents']

def resolveJson2(info_list):
    with open(r'C:\code\python-crawler\my_dict.json', 'r', encoding='utf8') as fp:
        json_data2 = json.load(fp)


    key = 0
    # 两个dict合并为一个
    for item in info_list:
        item.update(json_data2['info'][key])
        key = key + 1

    return info_list

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


def create_excel(finish_info):
    print('数据长度', len(finish_info))
    # 创建工作表
    workbook = xlsxwriter.Workbook(r'C:\code\python-crawler\baiten.xlsx')
    # 默认创建sheet1
    worksheet = workbook.add_worksheet()
    # 创建sheet2
    worksheet.write(0, 0, '标题')  # 行号和列标均是从0开始
    worksheet.write(0, 1, '申请日')
    worksheet.write(0, 2, '授权公告日')
    worksheet.write(0, 3, '技术价值')
    worksheet.write(0, 4, '经济价值')
    worksheet.write(0, 5, '法律价值')
    worksheet.write(0, 6, '总分')
    k = 1
    worksheet.set_column(0, 0, 40)
    worksheet.set_column(2, 2, 20)
    for item in finish_info:
        worksheet.write(k, 0, item['tittle'])
        worksheet.write(k, 1, item['application_date'])
        worksheet.write(k, 2, item['announcement_Day'])
        worksheet.write(k, 3, item['jishu'])
        worksheet.write(k, 4, item['jingji'])
        worksheet.write(k, 5, item['falv'])
        worksheet.write(k, 6, item['countVal'])
        k = k + 1
    workbook.close()
    print('代码结束')

def get_value_info(info_list):
    for item in info_list:
        url = "https://www.baiten.cn/patent/detail/{}?sc=&fq=&type=&sort=&sortField=&q=%E5%94%90%E4%BA%BA%E7%A5%9E%E9%9B%86%E5%9B%A2&rows=100#1/{}/worth/index".format(item['desAn'], item[id])

def get_edge_action(info_list):
    options = webdriver.EdgeOptions()  # 自定义加载项
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9527") #本地监听edge浏览器
    browser = webdriver.Edge(options=options)
    url = "https://www.baiten.cn/patent/detail/479706c8b89416e1bf1ec05d2d3d598e3591f56553a36d61?sc=&fq=&type=&sort=&sortField=&q=%E5%94%90%E4%BA%BA%E7%A5%9E%E9%9B%86%E5%9B%A2&rows=100#1/CN201310380651.3/worth/index"
    browser.get(url)
    sleep(3)

    scores_info = []
    timecount = 1;
    for item in info_list:
        url = "https://www.baiten.cn/patent/detail/{}?sc=&fq=&type=&sort=&sortField=&q=%E5%94%90%E4%BA%BA%E7%A5%9E%E9%9B%86%E5%9B%A2&rows=100#1/{}/worth/index".format(item['desAn'], item['id'])
        browser.get(url)
        print('第{}次：'.format(timecount), url)
        timecount = timecount+1
        browser.implicitly_wait(60)
        all_info = browser.find_elements(By.CSS_SELECTOR, '.m-detail-worth .worth-part .part-title')
        countVal = browser.find_element(By.CSS_SELECTOR, 'body.minpix .u-worth-des p.count > span')
        scores_info.append(
            {
                'jishu': all_info[0].text.split(' ')[4],
                'jingji': all_info[1].text.split(' ')[4],
                'falv': all_info[2].text.split(' ')[4],
                'countVal': countVal.text
            })
        print(all_info[0].text.split(' ')[4], all_info[1].text.split(' ')[4], all_info[2].text.split(' ')[4], countVal.text)
        sleep(3)


    print('scores_info',scores_info)
    with open(r"C:\code\python-crawler\my_dict.json", "w") as f:
        json.dump({'info': scores_info}, f, ensure_ascii=False)
        # 关闭文件
        f.close()

def test_url():
    scores_info = []
    options = webdriver.EdgeOptions()  # 自定义加载项，如限制图片加载，不打开浏览器窗口等操作
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    browser = webdriver.Edge(options=options)
    url = "https://www.baiten.cn/patent/detail/479706c8b89416e13d2b937ebd29e224eef46516d1a48964?sc=&fq=&type=&sort=&sortField=&q=%E5%94%90%E4%BA%BA%E7%A5%9E%E9%9B%86%E5%9B%A2&rows=100#1/CN201310380852.3/worth/index"
    browser.get(url)
    print(url)
    browser.implicitly_wait(10)
    print('加载完成')
    all_info = browser.find_elements(By.CSS_SELECTOR,'.m-detail-worth .worth-part .part-title')
    countVal = browser.find_element(By.CSS_SELECTOR,'body.minpix .u-worth-des p.count > span')
    scores_info.append(
        {
            'jishu': all_info[0].text.split(' ')[4],
            'jingji': all_info[1].text.split(' ')[4],
            'falv': all_info[2].text.split(' ')[4],
            'countVal': countVal.text
        })
    print('scores_info',scores_info)

if __name__ == '__main__':
    print('开始解析')
    # 解析数据
    json_list = resolveJson()
    # 处理数据，获取所有url的必要条件
    info_list = get_id_desAn(json_list)
    # 两个json文件数据合并
    finish_info = resolveJson2(info_list)
    # get_edge_action(info_list)

    print('写入数据', finish_info)
    create_excel(finish_info)
    # test_url()
