import tempfile
import os


fp = tempfile.TemporaryFile()
# fp.name包含文件路径
print(f"{fp.name=}")
# 当调用close时，上面创建的文件会被删除
fp.close()

# 也可以使用with的方式自动删除
with tempfile.TemporaryFile() as fp:
    print(f"{fp.name=}")
    fp.write(b'hello')
    fp.seek(0)
    print(fp.read())



tempdir = tempfile.TemporaryDirectory()
print(f"{tempdir.name=}")
os.mkdir(os.path.join(tempdir.name, 'test'))
with open(os.path.join(tempdir.name, 'test.txt'), 'w') as fp:
    fp.write("test")
tempdir.cleanup()

# 也支持with
# ignore_cleanup_errors 参数3.10才增加的
with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tempdir:
    print(f"{tempdir}") # 注意这里不能再使用tempdir.name