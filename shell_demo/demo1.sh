set -e

# 一个经典的处理命令行参数的demo

# 初始化username，如果前面username已经定义则用其值，否则初始化为空
username=${username:=}
isweb=${isweb:=0}

while [ $# -gt 0 ]; do
    case $1 in
        --username)
            username=$2 #命令类似 --username lin，故要用$2，而不是$1
            shift #相当于是把$1左移
            ;;
        --isweb)
            isweb=1 #开关命令，类似 --isweb，故不需要使用$1 还是 $2
            ;;
        --*)
            echo "Unrecognized option $1"
            ;;
    esac
    shift $(( $# > 0 ? 1 : 0 ))
done

echo "username=${username}, isweb=${isweb}"