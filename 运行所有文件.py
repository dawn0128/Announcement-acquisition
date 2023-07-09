import os
import subprocess


ordered_files = [
    '公告主页下载.py',
    '下载模块页面数据.py',
    '查看新公告.py'
]
# 获取当前项目的根目录路径
project_root = os.getcwd()

# 遍历项目目录下的所有文件和子目录
for file in ordered_files:
    file_path = os.path.join(project_root, file)

    # 运行 .py 文件
    subprocess.run(['python', file_path])

