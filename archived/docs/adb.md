```sh
adb devices

adb shell
# 进入指定的device
adb -s "you device id" shell

adb shell pm list packages

pm list packages
pm list packages | grep "chrome"

adb logcat
# 根据tag过滤
adb logcat -s tag
# 根据日志级别过滤
adb logcat *:W
adb logcat *:D
adb logcat *:E

# 查看正在运行的app
dumpsys activity activities

# 查看app信息
adb shell dumpsys package packagename
dumpsys package
```