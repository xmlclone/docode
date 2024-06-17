```bat
REM 示例代码的基本功能是遍历当前目录下所有子目录并使用 git pull 更新代码
REM 关闭命令的显示，即下发的命令本身不会显示出来，只有回显会显示出来
@echo off
REM 修改当前活动页的编码为UTF-8，并输出到null，即不回显chcp 65001的回显
chcp 65001 >nul
setlocal enabledelayedexpansion

REM 创建日志文件，相当于创建了一个变量
set LOGFILE=git_pull_errors.log
REM 输出内容到%LOGFILE%变量指定的文件里面
echo Git Pull Error Log > %LOGFILE%
REM > >> 一个是覆盖，一个是追加
echo ================== >> %LOGFILE%

REM 获取当前目录，同理 %cd% 就是执行 cd 命令，并把结果存储到 BASEDIR 变量， cd 的回显就是当前路径
set BASEDIR=%cd%

REM 遍历当前目录下的所有文件夹
REM for的基本语法: for %%var in (set) do command
REM /d 希望只匹配文件夹 (*) 表示当前目录下所有文件
for /d %%D in (*) do (
    if exist "%%D\.git" (
        echo 进入仓库 %%D
        cd "%%D"
        REM 执行 git pull 命令，并记录任何异常信息
        REM 2>> 表示标准错误输出到日志文件
        git pull 2>>"%BASEDIR%\%LOGFILE%"
        REM errorlevel 是一个特殊的环境变量，表示上一个命令的执行返回状态代码
        REM 一般 0 表示成功，其它值表示发生了不同的错误
        if errorlevel 1 (
            echo 仓库 %%D 更新失败，错误已记录。
        ) else (
            echo 仓库 %%D 更新成功。
        )
        REM 返回上级目录
        cd ..
    )
)

echo 所有仓库已更新完毕。查看 %LOGFILE% 获取错误日志。

endlocal
pause
```