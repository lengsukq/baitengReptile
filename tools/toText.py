import os
import mobi
from bs4 import BeautifulSoup

# 获取当前目录
current_directory = os.getcwd()

# 获取当前目录下的所有 MOBI 文件
mobi_files = [f for f in os.listdir(current_directory) if f.endswith('.mobi')]
total_files = len(mobi_files)

# 如果没有找到 MOBI 文件，给出提示
if total_files == 0:
    print("没有找到任何 MOBI 文件。")
else:
    print(f"找到 {total_files} 个 MOBI 文件，开始转换...")

    # 遍历所有 MOBI 文件
    for index, filename in enumerate(mobi_files, start=1):
        mobi_file_path = os.path.join(current_directory, filename)
        text_file_path = os.path.splitext(mobi_file_path)[0] + '.txt'

        try:
            # 解压 MOBI 文件
            mobi_content = mobi.extract(mobi_file_path)

            # mobi.extract 返回一个元组 (html, text)
            if isinstance(mobi_content, tuple):
                html_content = mobi_content[0]  # 提取 HTML 内容
            else:
                html_content = mobi_content  # 如果直接返回字符串

            # 解析 HTML 内容
            soup = BeautifulSoup(html_content, 'html.parser')
            text = soup.get_text()

            # 写入文本文件
            with open(text_file_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text)

            print(f"[{index}/{total_files}] 转换成功: {filename} -> {text_file_path}")
        except Exception as e:
            print(f"[{index}/{total_files}] 转换失败: {filename}, 错误: {e}")

    print("转换完成！")
