import douban
import requests
import xlsxwriter
import time

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}


def get_all_list():
    page = 1
    list = []
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
        list = list + (douban.get_poster_url(res))
        page += 1
        time.sleep(1)

    return list


if __name__ == '__main__':

    dataList = get_all_list()

    print(dataList)
    # 创建工作表
    workbook = xlsxwriter.Workbook('test.xlsx')
    # 默认创建sheet1
    worksheet = workbook.add_worksheet()
    # 创建sheet2
    # worksheet = workbook.add_worksheet('sheet2')
    worksheet.write(0, 0, '图片名')  # 行号和列标均是从0开始
    worksheet.write(0, 1, '链接')
    worksheet.write(0, 2, '图片')
    k = 1
    worksheet.set_column(0, 0, 20)
    worksheet.set_column(1, 1, 50)
    worksheet.set_column(2, 2, 100)
    # set_row(row, height, ceel_format, options)
    # 为一行单元格设置属性。
    # 参数：
    # row(int) - 工作表行(索引从0开始计数)
    # height(float) - 行高
    # cell_format(Format) - 可选的格式对象
    # options(dict) - 可选的行参数：hidden, level, collapsed
    # worksheet.set_row(1, 100)
    # ws.set_column(0, 3, 40)  # 设定第1到4列的列宽为40
    for item in dataList:
        worksheet.set_row(k, 300)
        worksheet.write(k, 0, item.split('/')[7].split('.')[0])
        worksheet.write(k, 1, item)
        worksheet.insert_image(k, 2, r'.\景甜Pic\{}'.format(item.split('/')[7]))
        k = k + 1
    workbook.close()
