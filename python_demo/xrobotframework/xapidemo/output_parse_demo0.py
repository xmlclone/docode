from robot.version import VERSION
from robot.api import ExecutionResult
from robot.result.executionresult import Result
from robot.model.statistics import Statistics


# 本文演示版本为: RF 6.1.1
version_info = tuple((int(i) for i in VERSION.split('.')))


def attrs(obj):
    for attr in dir(obj):
        if attr.startswith('_') or attr.endswith('_'):
            continue
        print(attr, getattr(obj, attr))


# 可以传递多个 output.xml 文件
# 可以使用 merge = True 合并多个 output.xml 文件
result: Result = ExecutionResult('output.xml')


# configure <bound method Result.configure of <robot.result.executionresult.Result object at 0x000002242A15A660>>
# errors No execution errors
# generated_by_robot True
# handle_suite_teardown_failures <bound method Result.handle_suite_teardown_failures of <robot.result.executionresult.Result object at 0x000002242A15A660>>
# return_code 1
# rpa False
# save <bound method Result.save of <robot.result.executionresult.Result object at 0x000002242A15A660>>
# set_execution_mode <bound method Result.set_execution_mode of <robot.result.executionresult.Result object at 0x000002242A15A660>>
# source output.xml
# statistics <robot.model.statistics.Statistics object at 0x000002242795F2F0>
# suite Testcases
# visit <bound method Result.visit of <robot.result.executionresult.Result object at 0x000002242A15A660>>
attrs(result)
print('-' * 100)




# suite <robot.model.suitestatistics.SuiteStatistics object at 0x0000027E80BB34A0>
# tags <robot.model.tagstatistics.TagStatistics object at 0x0000027E80BB36B0>
# total <robot.model.totalstatistics.TotalStatistics object at 0x0000027E807AF980>
# visit <bound method Statistics.visit of <robot.model.statistics.Statistics object at 0x0000027E808D72F0>>
statis: Statistics = result.statistics
attrs(statis)
print('-' * 100)
