# IO编程

import os

# 获取文件夹中的文件列表
folder_path = "C:/Users/10425/Desktop/pyCode/learn-python/basic-knowledge"
file_list = os.listdir(folder_path)
for file in file_list:
    print(file)

# 检查文件夹是否存在
if os.path.exists(folder_path):
    print(f"{folder_path} 存在")
else:
    print(f"{folder_path} 不存在")

# 创建新文件夹
new_folder_path = "C:/Users/10425/Desktop/pyCode/learn-python/new_folder"
# os.makedirs(new_folder_path, exist_ok=True)

# 删除文件夹
# 注意：rmdir只能删除空文件夹，如果文件夹非空，需要先删除其中的文件和子文件夹
# os.rmdir(new_folder_path)