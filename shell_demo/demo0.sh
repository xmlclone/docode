#!/bin/bash

# 表示如果有命令执行失败，则停止脚本的执行
# 比如cat一个不存在的文件，如果文件不存在并且有没有set -e，那么后续代码是可以继续执行的；设置set -e后则不会继续执行
set -e

# ${varname:=2}表示如果varname这个变量存在就用其本身的值，如果不存在则赋值
a=1
echo ${a:=2} #输出1
echo ${b:=2} #输出2

# comments
echo "hello"

# 等号前后不能有空格
var1=0
echo $var1

# read -p "输入任意内容:" var2
# echo "你输入的内容是: "$var2
# # 双引号可以解析$变量，单引号当成普通字符串处理
# echo "你输入的内容是: $var2"
# echo '你输入的内容是: $var2'
# # 也可以不用引号，就当成普通输出，$var2也会被解析
# echo 你输入的内容是: $var2

echo '$$(进程号)=' $$
echo '$0(进程名/执行文件名)=' $0
echo '$#(参数数量)=' $#
echo '$*(参数内容)=' $*
echo '$1(参数1)=' $1
echo '$2(参数2)=' $2
echo '$?(上一条命令执行状态)=' $?

# ``会把包含内容当成命令执行
echo "ls result `ls`"


a=10
(
    # 子shell执行，不影响当前进程变量
    a=20
)
echo $a

{
    # 当前shell执行，影响当前进程变量
    a=30
}
echo $a


# test xxx 和 [ xxx ] 是测试命令，其中[]前后需要有空格
# 文件测试 -e(存在?) -d(目录?) -f(文件?) -r(可读？) -w -x -s(非空？) -L -c -b
# 字符串 =(相等) !=(不等) -z(空？) -n(非空?)  ${#strname}--->字符串长度
# 数值 -eq -ne -gt -ge -lt -le
# && || 都是短路计算； -a -o !
test -e demo1.sh
echo $? #0
[ -e demo1.sh ]
echo $? #0
[ -e adfdsfadfa.sh ]
echo $? #1
strvar1="abcdef"
[ -n $strvar1 ]
echo $? #0
echo ${#strvar1} #6
[ 1 -eq 2 ]
echo $? #1
# 注意 -a -o 和 && || 使用的区别
test 1 -eq 2 || test 2 -eq 2
echo $? #0
[ 1 -lt 2 ] && [ 2 -lt 3 ]
echo $? #0
# 注意 -a -0 和 && || 使用的区别
[ 1 -eq 2 -o 1 -lt 2 ]
echo $? #0


read -p "请输入数字: " var3
if [ $var3 -lt 0 ]; then
    echo "输入内容: $var3 < 0"
elif [ $var3 -gt 0 ]; then
    echo "输入内容: $var3 > 0"
else
    echo "输入内容: $var3 = 0"
fi


# 注意，如果不用declare -i的方式把变量i和sum强制设置为int型，后面使用+会当成字符串进行处理，导致结果不正确
declare -i i=0
declare -i sum=0
for (( i=0; i<10; i++ ))
do
    sum=$sum+$i
    # sum=sum+i 效果一致，即使用declare -i后，在处理运算时$可以忽略(如果使用了declare -i推荐使用此方式)
done
echo "sum=$sum"


# for的另外一种形式
for file in `ls`
do
    echo $file
done

declare -i max=10
declare -i loop=0
while [ $max -gt $loop ]
do
    echo $loop
    loop+=1
    # $loop+=1 不能使用此方式了，此方式会被解释成0+=1，loop变量永远不会变化
done


# 定义函数时，不需要参数，函数内部使用$0 $1方式获取传递的参数
# 如果函数在其它文件定义，需要在使用函数的文件内部使用 source xxx.sh 引入使其生效
f1 () {
    echo "函数1"
}

function f2 () {
    echo "函数2，参数有$#个，分别是:"
    for i in $*
    do
        echo $i
    done
    echo "当然也可以使用$1 $2方式获取" # $0仍是是文件名
}

f1
f2
f2 0 1 2