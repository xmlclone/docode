import os


path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(path)

# scandir只会遍历当前目录，不会递归进入子目录
with os.scandir(path) as entries:
    for entry in entries:
        print(entry, entry.path)
print('=======')


# 删除空目录
def remove_empty_directories(directory):
    # 判断目录是否存在
    if not os.path.isdir(directory):
        return

    # 遍历当前目录下的所有子目录和文件
    with os.scandir(directory) as entries:
        for entry in entries:
            # 如果是目录，则递归调用函数
            if entry.is_dir():
                remove_empty_directories(entry.path)

    # 重新遍历目录，检查是否为空目录
    with os.scandir(directory) as entries:
        # 如果目录中没有子目录和文件，则删除该目录
        if not any(entries):
            print(directory)
            # os.rmdir(directory)

remove_empty_directories(path)