# 安装

## docker

> https://registry.hub.docker.com/_/jenkins

```sh
# 访问8080端口即可
# 可以通过docker logs -f jenkins查看安装需要的initpassword
docker run --rm -itd -p 8080:8080 -p 50000:50000 jenkins
docker run --itd --name myjenkins -p 8080:8080 -p 50000:50000 -v /your/home:/var/jenkins_home jenkins
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

可以使用脚本模板的方式，把groovy脚本放置到`$JENINS_HOME/email-templates`目录下，如果不存在则自己创建，假设文件名为`rf_email_template.groovy`，则在`Default Content`里面填入内容为: `${SCRIPT, template="rf_email_template.groovy"}`，groovy部分脚本参考如下:

```groovy
<%  
    import java.text.DateFormat  
    import java.text.SimpleDateFormat
    import  hudson.model.Result
%>  
    <!-- Robot Framework Results -->  
<%  
    def robotResults = false  
    def actions = build.actions // List<hudson.model.Action>  
    def _build = build // hudson.model.FreeStyleBuild
    // def _env = env
    // def _params = params
    // def _currentBuild = currentBuild
    def _workspace = workspace
    // def _tool = tool

    // def cls = build.class
    // def methods = cls.getDeclaredMethods() 
    // def fields = cls.getDeclaredFields()

    actions.each() { //1
        // https://javadoc.jenkins.io/    (api doc)
        // https://javadoc.jenkins.io/plugin/robot/allclasses.html   (rf plguin api doc)
        // 文档里面大部分是getXXX()，脚本里面可以使用 .XXX 属性的方式访问
        action ->  if( action.class.simpleName.equals("RobotBuildAction") ) { // hudson.plugins.robot.RobotBuildAction   //2
            robotResults = true
%>

<%
    def cause = ""
    for (cause_ in build.causes) {
        cause = cause_.shortDescription
    }
%>
    <div style="width:100%; float:left; margin-top:30px; margin-left:50px"> 
        <table cellspacing="0" cellpadding="4" border="1" align="left">  
            <thead>
                <tr bgcolor="#F3F3F3">
                    <td style="text-align:center" colspan="5"><b>【${project.name}】自动化测试汇总报告</b></td>    
                </tr>
                <tr>
                    <td bgcolor="#F3F3F3"><b>构建信息</b></td>
                    <td colspan="5">
                        <ul>
                            <li>构建编号: ${build.number}</li>
                            <li>启动时间: </li>
                            <li>构建时长: ${build.durationString}</li>
                            <li>构建时长: <%= action.result.getDuration().intdiv(360000)+"时" + (action.result.getDuration() - action.result.getDuration().intdiv(360000)*360000).intdiv(60000)+"分"+(action.result.getDuration()-action.result.getDuration().intdiv(60000)*60000).intdiv(1000)+"秒" %></li>
                            <li>触发原因: ${cause}</li>
                            <!-- <li>构建结果: <b><span style="color:<%= build.result=='SUCCESS' ? "#66CC00" : "#FF3333" %>">${build.result}</span></b></li> -->
                            <li>构建结果: <b><span style="color:<%= build.result==Result.SUCCESS ? "#66CC00" : "#FF3333" %>">${build.result}</span></b></li> 
                            <li>构建日志: <a href="${rooturl}${build.url}console">点我查看</a></li>
                            <li>报告详情: <a href="${rooturl}${build.url}robot/report/report.html">点我查看</a></li>
                            <li>日志详情: <a href="${rooturl}${build.url}robot/report/log.html">点我查看</a></li>
                        </ul>
                    </td>
                </tr>                            
                <tr bgcolor="#F3F3F3">
                    <td style="width:150px"><b>用例总数</b></td>
                    <td style="width:150px"><b>通过</b></td>
                    <td style="width:150px"><b>不通过</b></td>
                    <td style="width:150px"><b>通过率</b></td>
                    <td style="width:150px"><b>执行时长</b></td>
                </tr>
                <tr>
                    <td><%= action.result.overallTotal %></td>
                    <td><b><span style="color:#66CC00"><%= action.result.overallPassed %></span></b></td>
                    <td><b><span style="color:#FF3333"><%= action.result.overallFailed %></span></b></td>
                    <td><%= action.overallPassPercentage %>%</td>
                    <td><%= action.result.getDuration().intdiv(360000)+"时" + (action.result.getDuration() - action.result.getDuration().intdiv(360000)*360000).intdiv(60000)+"分"+(action.result.getDuration()-action.result.getDuration().intdiv(60000)*60000).intdiv(1000)+"秒" %></td>  
                </tr>
                <tr bgcolor="#F3F3F3">  
                    <td colspan="2"><b>Test Name</b></td>  
                    <td><b>Status</b></td>
                    <td><b>Elapsed Time(ms)</b></td>
                    <td><b>Detail</b></td>
                </tr>  
            </thead>  
            <tbody>  
<% 
                    def suites = action.result.allSuites  // hudson.plugins.robot.model.RobotResult  List<RobotSuiteResult>
                    suites.each() { suite ->   //3
                        def currSuite = suite  
                        def suiteName = currSuite.displayName  
                        // ignore top 2 elements in the structure as they are placeholders  
                        while (currSuite.parent != null && currSuite.parent.parent != null) {  
                            currSuite = currSuite.parent  
                            suiteName = currSuite.displayName + "." + suiteName  
                        } 
%>  
                <tr>
                    <td colspan="5"><b><%= suiteName %></b></td>
                </tr>  
<%  
                        DateFormat format = new SimpleDateFormat("yyyyMMdd HH:mm:ss")
                        def execDateTcPairs = []
                        suite.caseResults.each() { tc ->  // Collection<RobotCaseResult>
                            Date execDate = format.parse(tc.starttime)
                            execDateTcPairs << [execDate, tc]
                        }
                        // primary sort execDate, secondary displayName
                        execDateTcPairs = execDateTcPairs.sort{ a,b -> a[1].displayName <=> b[1].displayName }
                        execDateTcPairs = execDateTcPairs.sort{ a,b -> a[0] <=> b[0] }
                        execDateTcPairs.each() {//4
                            def execDate = it[0]
                            def tc = it[1]  
%>
                <tr>  
                    <td colspan="2"><%= tc.displayName %></td>  
                    <td><b><span style="color:<%= tc.isPassed() ? "#66CC00" : "#FF3333" %>"><%= tc.isPassed() ? "PASS" : "FAIL" %></span></b></td>  
                    <td><%= tc.getDuration() %></td>
                    <td><a href="${rooturl}${build.url}robot/report/log.html#<%= tc.getParent().getId() %>">点我查看日志</a></td>
                </tr>  
<% 
                            if(tc.errorMsg != null) { //5
%>
                <tr>
                    <td ><b><span style="font-size:10px;color:#FF3333">错误描述：</span></b></td>
                    <td colspan="4"><span style="font-size:10px"><%= tc.errorMsg%></span></td>
                </tr>
<%
                            } //5
%>
<%
                        } // tests  //4
                    } // suites //3
%>
            </tbody>
        </table>
        <p style="color:#AE0000;clear:both">*报告通过Jenkins自动构建生成，仅供参考。</p>
    </div>
<%
        } // robot results  //2
    }  //1
        if (!robotResults) { 
%>  
            <p>No Robot Framework test results found.</p>  
<%  
        }
%>


<div>
    <h1>其它数据</h1>
    <ul>
        <!-- https://github.com/jenkinsci/email-ext-plugin/blob/master/docs/templates/jenkins-matrix-email-html.template -->
        <li>build: ${build.class}</li>
        <li>build.builtOnStr: ${build.builtOnStr}</li>
        <li>build.result: ${build.result}</li>
        <li>build.url: ${build.url}</li>
        <li>build.description: ${build.description}</li>
        <%
            for (case in build.cases){
        %>
        <li>build.cases: ${case.shortDescription}</li>
        <%
            }
        %>
        <li>build.changeSet: ${build.changeSet}</li>
        <li>runs: ${runs}</li>
        <li>result_img: ${result_img}</li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li>project: ${project.class}</li>
        <li>project.name: ${project.name}</li>
        <li></li>
        <li>it.timestampString: ${it.timestampString}</li>
        <li></li>
        <li>rooturl: ${rooturl}</li>
        <li></li>
    </ul>
</div>

<!--

-->
```

# QA

## Opening Robot Framework report failed

Dashboard -> Manage Jenkins -> Script Console 执行下面的脚本:

```groovy
System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")
System.setProperty("hudson.model.DirectoryBrowserSupport.CSP","sandbox allow-scripts; default-src 'none'; img-src 'self' data: ; style-src 'self' 'unsafe-inline' data: ; script-src 'self' 'unsafe-inline' 'unsafe-eval' ;")
```

# 参考链接

* [RF日志文件无法打开(Opening Robot Framework log failed)](https://plugins.jenkins.io/robot/#plugin-content-log-file-not-showing-properly)


