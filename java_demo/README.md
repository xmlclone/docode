# 命令行

```shell
# 运行java
javac demo0.java
java demo0
```

# 常用链接

1. [commons.apache.org](https://commons.apache.org/)
2. [commons-codec](https://commons.apache.org/proper/commons-codec/apidocs/overview-summary.html)

# QA

## 找不到JRE目录

如果安装完成后没有jre，可以进入jdk目录，执行`bin\jlink.exe --module-path jmods --add-modules java.desktop --output jre-18.0.1`命令，即可看见jre生成了

## 编码gbk的不可映射字符

在使用`javac XXX.java`编译的时候提示如上错误，可以通过命令行增加编码参数处理，比如`javac -encoding UTF-8 XXX.java`