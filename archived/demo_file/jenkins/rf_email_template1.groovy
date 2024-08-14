<%  
    import java.text.DateFormat  
    import java.text.SimpleDateFormat
%>  
    <!-- Robot Framework Results -->  
<%  
    def robotResults = false  
    def actions = build.actions // List<hudson.model.Action>  hudson.model.FreeStyleBuild

    actions.each() { //1
        action ->  if( action.class.simpleName.equals("RobotBuildAction") ) { // hudson.plugins.robot.RobotBuildAction   //2
            robotResults = true
%>

<%
    def cause = ""
    for (cause_ in build.causes) {
        cause = cause_.shortDescription
    }
    def formattedStartDate = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date(build.getStartTimeInMillis()))
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
                            <li>启动时间: ${formattedStartDate}</li>
                            <li>构建时长: ${build.durationString}</li>
                            <li>触发原因: ${cause}</li>
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