import json

# 读取 JSON 文件
with open('font.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# 提取 font_class 字段
font_class_list = [item['font_class'] for item in json_data if 'font_class' in item]

# 将结果保存到新的 JSON 文件
with open('font_class_list.json', 'w', encoding='utf-8') as output_file:
    json.dump(font_class_list, output_file, ensure_ascii=False, indent=4)

print("font_class 字段已成功保存到 font_class_list.json 文件中。")