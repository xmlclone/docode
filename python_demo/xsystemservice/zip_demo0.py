import zipfile


zip_file1 = 'zipfile1.zip'
# 有密码
zip_file2 = 'zipfile2.zip'
# 有目录
zip_file3 = 'zipfile3.zip'


print(zipfile.is_zipfile(zip_file1))


# 查看压缩包内容
with zipfile.ZipFile(zip_file1) as zip:
    print(f"{zip.namelist()=}")
    # print(f"{zip.infolist()=}")

# 目录也可以查看
with zipfile.ZipFile(zip_file3) as zip:
    print(f"{zip.namelist()=}")


# 解压
with zipfile.ZipFile(zip_file3) as zip:
    # 把所有文件解压到当前目录下的path1路径下
    zip.extractall('path1')

with zipfile.ZipFile(zip_file2) as zip:
    # 解压有密码的zip包，注意要用byte
    zip.extractall('path2', pwd=b"123456")



