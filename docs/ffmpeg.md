# 基础命令

```shell
# mp4转y4m
ffmpeg -i input.mp4 -pix_fmt yuv420p output.y4m
```

```shell
# 把本地视频推到rtmp服务器，循环读取推送
# -i 读取原始视频
# -f 对输出有效，强制输出为flv格式，输出到rtmp://127.0.0.1 (注意flv可以理解为rtmp的http版本，通过ffmpeg -formats看见有flv，没有rtmp，所以这里用flv即可)
# -c codec name，指定为copy，表示直接使用输入文件的编解码格式即可，对输出有效，节省时间(因为输入的时候已经进行了一次编解码了，输出的时候直接用)
# 针对上面的copy，其实在很多地方都有应用
# -stream_loop 针对输入有效，即循环次数，后面的-1(注意是数字1，不是小写的L)
# -re即-readrate 1的缩写，针对输入有效，表示读取速率，1表示正常速率
ffmpeg -re -stream_loop -1 -i disco.mp4 -c copy -f flv rtmp://127.0.0.1

# 拉取远程流保存到本地
ffmpeg -f flv -i rtmp://127.0.0.1 output.mp4
```

```shell
# 建议查看帮助文档
ffmpeg -h long > ffmpeg.txt
# 更详细的帮助文档，重定向输出后打开方便查找
ffmpeg -h full > ffmpeg.txt

# 命令基本格式
# 其中可以理解以-i作为输入和输出的区分，-i前面的都是对输入进行处理，-i后面的都是对输出进行处理
ffmpeg [options] [[infile options] -i infile]... {[outfile options] outfile}...
ffmpeg [全局参数] {[输入文件参数] -i 输入文件地址} ... {[输出文件参数] 输出文件地址} ...

# 查看支持的格式
ffmpeg -formats
# 查看支持的编解码格式
ffmpeg -codecs

# -i用于输入，可以是文件、管道、网络流、设备等
ffmpeg -i xxx
# -f用于强制指定输入、输出的格式
ffmpeg -f fmt
```

# 参考链接

1. [官方文档](https://ffmpeg.org/documentation.html)
1. [利用ffmpeg实现rtmp推流](https://www.jianshu.com/p/c141fc7881e7)
2. [FFmpeg命令大全](https://zhuanlan.zhihu.com/p/482599405)
3. [FFMPEG命令入门到提高，一篇文章就够了](https://zhuanlan.zhihu.com/p/117523405)
4. [个人总结](https://github.com/xmlclone/archived/blob/main/0mybook/AV.md)