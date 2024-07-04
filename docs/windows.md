# 增加命令别名

比如增加一个`ls`命令

1. 打开`cmd`输入`regedit`打开注册表
2. 找到`HKEY_CURRENT_USER\SOFTWARE\Microsoft\Command Processor`
3. 新建一个`bat`文件，里面增加如下代码:

```bat
@doskey ls=dir $*
```

4. 编辑或新增类型为`REG_EXPAND_SZ`的key，key名称为`AutoRun`，值为上面定义的`bat`文件路径