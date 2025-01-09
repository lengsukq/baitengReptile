import os
import json


def get_png_files(folder_path):
    # 获取文件夹内所有文件
    files = os.listdir(folder_path)

    # 过滤出所有以 .png 结尾的文件
    png_files = [file[:-4] for file in files if file.endswith('.png')]

    return png_files


def save_to_json(data, folder_path, json_filename='png_files.json'):
    # 构建JSON文件的完整路径
    json_path = os.path.join(folder_path, json_filename)

    # 将数据保存为JSON文件
    with open(json_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"JSON文件已保存到: {json_path}")


if __name__ == "__main__":
    # 输入文件夹路径
    folder_path = input("请输入文件夹路径: ")

    # 获取所有PNG文件名（不带后缀）
    png_files = get_png_files(folder_path)

    # 将文件名数组保存为JSON文件
    save_to_json(png_files, folder_path)