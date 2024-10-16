import os
import re

# 项目目录
PROJECT_PATH = './project'  # 请替换为你的项目路径

# 扫描并修改所有 .vue 文件
def scan_and_modify_files():
    for root, dirs, files in os.walk(PROJECT_PATH):
        for file in files:
            if file.endswith(".vue"):
                file_path = os.path.join(root, file)
                modify_file(file_path)

# 修改文件内容
def modify_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 开始逐条替换
    content = replace_locale_provider(content)
    content = remove_tag_after_close(content)
    content = update_form_model(content)
    content = update_html_attributes(content)
    content = update_render_slots(content)
    content = update_scoped_slots(content)
    content = flatten_props(content)
    content = update_sync_to_v_model(content)

    # 保存修改后的文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Modified: {file_path}")

# 移除 LocaleProvider，替换为 ConfigProvider
def replace_locale_provider(content):
    return content.replace('LocaleProvider', 'ConfigProvider')

# 移除 Tag 的 afterClose 属性
def remove_tag_after_close(content):
    return re.sub(r'(\s*)afterClose={.*?}', '', content)

# 合并 FormModel 和 Form 的处理
def update_form_model(content):
    return content.replace('FormModel', 'Form')

# 更新一些 HTML 属性为小写
def update_html_attributes(content):
    html_attrs = ['tabIndex', 'maxLength', 'readOnly', 'autoComplete', 'autoFocus']
    for attr in html_attrs:
        content = re.sub(fr'{attr}=', f'{attr.lower()}=', content)
    return content

# 处理 xxxRender, renderXxxx 为单参数
def update_render_slots(content):
    render_patterns = [
        'itemRender', 'renderItem', 'customRender', 'dropdownRender',
        'dateCellRender', 'dateFullCellRender', 'monthCellRender',
        'monthFullCellRender', 'renderTabBar'
    ]
    for pattern in render_patterns:
        content = re.sub(fr'{pattern}=\{{(.*?),', fr'{pattern}={{', content)
    return content

# 替换 scopedSlots 为 slots
def update_scoped_slots(content):
    return content.replace('scopedSlots', 'slots')

# 扁平化处理 props 和 on 配置
def flatten_props(content):
    content = re.sub(r'props\s*:\s*\{(.*?)\},\s*on\s*:\s*\{(.*?)\}', lambda match: flatten_props_on(match), content, flags=re.DOTALL)
    return content

def flatten_props_on(match):
    props_content = match.group(1).strip()
    on_content = match.group(2).strip()

    # 替换 on 事件格式
    on_flattened = re.sub(r'(\w+)\s*:', r'on\1', on_content)

    return f"{props_content}, {on_flattened}"

# 替换 xxx.sync 为 v-model:xxx
def update_sync_to_v_model(content):
    # 处理各个组件的 v-model 替换
    v_model_patterns = {
        'CheckableTag|Checkbox|Switch': 'v-model:checked',
        'Radio|Mentions|CheckboxGroup|Rate|DatePicker|Select': 'v-model:value',
        'Tag|Popconfirm|Popover|Tooltip|Modal|Dropdown': 'v-model:visible',
        'Collapse|Tabs': 'v-model:activeKey',
        'Steps': 'v-model:current',
        'Menu': 'v-model:selectedKeys'
    }

    for components, v_model in v_model_patterns.items():
        content = re.sub(fr'v-model\s*=\s*"(\w+)"', fr'{v_model}="\1"', content)

    return content

if __name__ == '__main__':
    scan_and_modify_files()
