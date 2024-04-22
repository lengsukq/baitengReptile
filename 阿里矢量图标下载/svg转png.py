import os
import cairosvg
import json

def svg_to_png(obj, index):
    # 假设show_svg字段是一个序列化的JSON字符串
    # 对其进行反序列化以获取SVG代码
    svg_code = obj["show_svg"]
    font_class = obj["font_class"]
    # SVG代码转换为PNG图片，并将文件名设置为JSON对象中的font_class属性
    file_name = f"./png/{font_class}.png"
    cairosvg.svg2png(bytestring=svg_code.encode('utf-8'), write_to=file_name)

if __name__ == '__main__':
    print('开始执行')
    # 打开JSON文件并加载数据
    with open('svg.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 确保输出目录存在
    output_dir = './png'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for index, item in enumerate(data):
        print(f"正在处理 {index}: {item['font_class']}{item['show_svg']}")
        svg_to_png(item, index)
    # data现在是一个列表，每个元素是一个字典，对应JSON文件中的一个对象
    print('结束')
