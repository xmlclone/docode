# 安装

## docker

> https://registry.hub.docker.com/_/jenkins

```sh
# 访问8080端口即可
# 可以通过docker logs -f jenkins查看安装需要的initpassword
docker run --rm -itd -p 8080:8080 -p 50000:50000 jenkins
docker run -itd --name myjenkins -p 8080:8080 -p 50000:50000 -v /your/home:/var/jenkins_home jenkins
# 假设在windows下挂载
docker run -itd --name jenkins -p 8080:8080 -p 50000:50000 -v D:\dockermount\jenkins:/var/jenkins_home jenkins
```

# 常用命令

> 在`Dashboard -> 系统管理 -> 工具和动作 -> Script Console`下

```sh
# 重启jenkins
Jenkins.instance.restart()
```

# 变量

```sh
# 可以用空格代替下划线
$PROJECT_NAME
$BUILD_NUMBER
$BUILD_STATUS
$BUILD_URL
${WORKSPACE}


# Email Extension相关
$DEFAULT_CONTENT
$DEFAULT_PRESEND_SCRIPT
```

> 可以通过`http://[jenkins]/env-vars.html/`访问jenkins的内置环境变量，注意替换`[jenkins]`为你的jenkins地址

# 配置

## 构建命令

```sh
# 如果某条命令失败，默认情况下后续命令不会继续执行，如果需要继续执行，需要在命令后面加  || true，比如
robot --nostatusrc --output 2_output.xml --log 2_log.html --report 2_report.html -R 1_output.xml . || true
```

## 定时构建

```sh
# MINUTE(0–59) HOUR(0–23) DOM(1–31) MONTH(1–12) DOW (0–7)
# *   M-N  M-N/X  */X  A,B,...,Z

# 每日凌晨构建
0 0 * * * # 不建议，建议使用下面方式
H H * * *

# 表示每日0:00-7:59点之间构建
H H(0-7) * * *

# 每隔15分钟构建一次
H/15 * * * *

# 每个小时的前30分钟内，间隔10分钟构建一次
H(0-29)/10 * * * *
```

## 邮件配置

1. Dashboard -> Manage Jenkins -> System Configuration -> System -> Jenkins Location -> 系统管理员邮件地址(配置邮箱)
2. Dashboard -> Manage Jenkins -> System Configuration -> System -> 邮件通知(配置邮件通知服务)

# 插件

## Email Extension

https://plugins.jenkins.io/email-ext/

配置位置: Project的Configuration -> 构建后操作 -> Editable Email Notification

### Pre-send Script

位置: Project的Configuration -> 构建后操作 -> Editable Email Notification -> Advanced Settings -> Pre-send Script

https://plugins.jenkins.io/email-ext/#plugin-content-pre-send-scripts-and-post-send-scripts

```groovy
// 打印日志，这个会出现在构建日志里面
logger.print("hahahaha")

// 设置邮件内容
// https://javaee.github.io/javamail/docs/api/
msg.setText("This is new email content.")
```

### Default Content

可以使用脚本模板的方式，把groovy脚本放置到`$JENKINS_HOME/email-templates`目录下，如果不存在则自己创建，假设文件名为`rf_email_template.groovy`，则在`Default Content`里面填入内容为: `${SCRIPT, template="rf_email_template.groovy"}`，groovy脚本可以参考`demo_file/jenkins`下相关脚本文件。

# API

1. `groovy`里面可以直接使用`.`的方式替代`java`的`getXXX`，比如`https://javadoc.jenkins.io/plugin/robot/hudson/plugins/robot/model/RobotResult.html#getAllSuites()`这个方法，在`groovy`里面可以直接使用`allSuites`获取到。

# QA

## Opening Robot Framework report failed

Dashboard -> Manage Jenkins -> Script Console 执行下面的脚本:

```groovy
System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")
System.setProperty("hudson.model.DirectoryBrowserSupport.CSP","sandbox allow-scripts; default-src 'none'; img-src 'self' data: ; style-src 'self' 'unsafe-inline' data: ; script-src 'self' 'unsafe-inline' 'unsafe-eval' ;")
```

## 553 Mail from must equal authorized user

在测试邮件通知时，出现`553 Mail from must equal authorized user`错误，并不是smtp或密码配置问题，而是系统管理员邮件没有配置导致的

在`Dashboard -> 系统管理 -> System -> 系统管理员邮件地址`配置和发送人一样的地址后即可。

## 构建时间问题

1. 首先查询`Dashboard 系统管理 System Information` 查看`user.timezone`配置时区是否正确
2. 如果需要修改，进入`Dashboard 系统管理 Script Console`，输入`System.setProperty('user.timezone', 'Asia/Shanghai')`应用即可

> 注意确保服务器的时区也正确

# 参考链接

* [RF日志文件无法打开(Opening Robot Framework log failed)](https://plugins.jenkins.io/robot/#plugin-content-log-file-not-showing-properly)
* [Jenkins API](https://javadoc.jenkins.io/index.html)


