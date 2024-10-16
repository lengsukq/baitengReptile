import os
import cairosvg
import json


def svg_to_png(obj):
    svg_code = obj["show_svg"]
    font_class = obj["font_class"]
    # SVG代码转换为PNG图片，并将文件名设置为JSON对象中的font_class属性
    file_name = f"./png/{font_class}.png"
    cairosvg.svg2png(bytestring=svg_code.encode('utf-8'), write_to=file_name, scale=3.0, output_width=50, output_height=50)


def check_duplicate_filenames(data_list):
    # 保存所有文件名
    filenames = set()
    # 保存重复文件名的集合
    duplicates = set()

    for item in data_list:
        # 获取font_class属性，作为文件名（这里区分大小写）
        filename = item['font_class']

        # 检查文件名是否已经在之前见过
        if filename in filenames:
            duplicates.add(filename)
        else:
            filenames.add(filename)

    return list(duplicates)


def check_missing_files(directory, data_list):
    # 从data_list中提取所有的文件名
    expected_files = {f"{item['font_class']}.png" for item in data_list}

    # 获取目录中实际存在的所有文件名
    actual_files = set(os.listdir(directory))

    # 找出期望的文件名中哪些在目录中不存在
    missing_files = expected_files - actual_files

    return list(missing_files)


if __name__ == '__main__':
    print('开始执行')
    # 打开JSON文件并加载数据
    with open('svg.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 确保输出目录存在
    output_dir = './png'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        for index, item in enumerate(data):
            print(f"正在处理第{index + 1}个: {item['font_class']}")
            svg_to_png(item)
    except Exception as e:
        print(f"处理第{index + 1}个时发生错误: {e}")

    duplicate_filenames = check_duplicate_filenames(data)
    if duplicate_filenames:
        print("存在重复的文件名：", duplicate_filenames)
    else:
        print("所有文件名都是唯一的。")

    directory_path = "./png"  # 检查的目录路径
    missing_filenames = check_missing_files(directory_path, data)
    if missing_filenames:
        print("这些文件不存在对应的文件：", missing_filenames)
    else:
        print("所有文件名都有对应的文件。")

    print('结束')
