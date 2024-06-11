from robot.version import VERSION

# VERSION 是一个纯字符串的，比如 6.1.1

version_info = tuple((int(i) for i in VERSION.split('.')))

print(version_info)

print(version_info >= (6, 0))
print(version_info >= (7, 0))