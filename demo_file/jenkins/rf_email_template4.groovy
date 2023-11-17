<%  
import java.text.DateFormat  
import java.text.SimpleDateFormat

// 触犯原因
def cause = null
for (cause_ in build.causes) {
    cause = cause_.shortDescription
}
// 构建开始时间
def formattedStartDate = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date(build.getStartTimeInMillis()))
// RobotBuildAction
def action = null
// 测试用例集合[tcinstance, tcname]
def testcaseSet = []
// 修改集合 ChangeLogSet
def changeSet = build.getChangeSet()

for (_action in build.actions) {//1 List<hudson.model.Action>  hudson.model.FreeStyleBuild
    if (_action.class.simpleName.equals("RobotBuildAction")){//2
        action = _action
        def suites = _action.result.allSuites
        for (suite in suites) {
            def currSuite = suite
            def suiteName = currSuite.displayName
            while (currSuite.parent != null && currSuite.parent.parent != null) {  
                currSuite = currSuite.parent
                suiteName = currSuite.displayName + "." + suiteName
            }
            for (tc in suite.caseResults) {
                if (tc.isPassed()) {
                    continue
                }
                testcaseSet << [tc, (suiteName + "." + tc.displayName)]
            }
        }
        break
    }
}
%>

<%
if (action == null) {
%>
    <p>No Robot Framework test results found.</p>
<%  
} else {//1
%>

<html>
    <head>
        <title>RF REPORT TEMPLATE 3</title>
        <style>
            h3 {
                color: darkgreen;
            }
            a {
                text-decoration: none;
            }
            body {
                width: 800px;
            }

            li {
                margin-top: 8px;
            }
        </style>
    </head>

    <body>
        <h3>构建信息</h3>
        <hr>
        <ul>
            <li>项目名称: ${project.name}</li>
            <li>构建编号: ${build.number}</li>
            <li>用例总数: <b>${action.result.overallTotal}</b> | 通过: <b><span style="color: #66CC00;">${action.result.overallPassed}</span></b> | 失败: <b><span style="color: #FF3333;">${action.result.overallFailed}</span></b> | 通过率: <b>${action.overallPassPercentage}%</b></li>
            <li>启动时间: ${formattedStartDate}</li>
            <li>构建时长: ${build.durationString}</li>
            <li>触发原因: ${cause}</li>
            <li>构建结果: <b><span style="color:<%= build.result==Result.SUCCESS ? "#66CC00" : "#FF3333" %>">${build.result}</span></b></li> 
            <li>构建日志: <a href="${rooturl}${build.url}console">${rooturl}${build.url}console</a></li>
            <li>报告详情: <a href="${rooturl}${build.url}robot/report/report.html">${rooturl}${build.url}robot/report/report.html</a></li>
            <li>日志详情: <a href="${rooturl}${build.url}robot/report/log.html">${rooturl}${build.url}robot/report/log.html</a></li>
        </ul>
        <h3>失败用例</h3>
        <hr>
        <ul>
<%
    for (tc in testcaseSet) {
        case_id = tc[0].getParent().getId()
        tc_name = tc[1]
%>
            <li><a href="${rooturl}${build.url}robot/report/log.html#${case_id}">${tc_name}</a></li>
<%
    }
%>
        </ul>
        <h3>最近提交</h3>
        <hr>
        <ul>
<%
    hasChangeSet = false
    for (entry in changeSet) {
        hasChangeSet = true
        changeTime = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date(entry.timestamp))
%>
            <li>${changeTime} [${entry.author}] ${entry.msg}</a></li>
<%
    }
    if (!hasChangeSet) {
%>
        <p>No Changes.</p>
<%
    }
%>
        </ul>
        <!-- <p style="color:#AE0000;clear:both">*报告通过Jenkins自动构建生成，仅供参考(jenkins链接需要进入虚拟桌面访问)。</p> -->
    </body>
</html>



<%
}//1
%>

