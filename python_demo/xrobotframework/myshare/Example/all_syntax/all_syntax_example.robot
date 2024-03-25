*** Comments ***
This is Comments section.
从RF6.0开始，块应该使用复数形式，比如Settings，7.0开始不在支持单数形式


*** Settings ***
Documentation    Robotframework syntax example.
Metadata    Version    1.0
Metadata    Author    linlei
Suite Setup    Log    File suite setup.
Suite Teardown    Log    File suite teardown.
Test Setup    Log    File test setup.
Test Teardown    Log    File test teardown.
Test Timeout    10s
Test Tags    all
Library    Collections
Library    String
Library    pylib1.py
Variables    pyvar.py
Resource    vars.resource
Resource    keywords.resource


*** Variables ***
${NAME}    Robotframework
${VERSION}    1.0
${ROBOT}    ${NAME} ${VERSION}
@{BOOKS}    Python    Java
&{RATE}    python=100    java=200


*** Test Cases ***
Case1
    [Documentation]    演示关键字调用的几种方式，包括默认值、命名参数、列表字典方式调用
    [Tags]    case1
    [Timeout]    15s
    [Setup]    Log    Case setup.
    [Teardown]    Log    Case teardown.
    ${rel1}    Add Values    1    2
    Should Be Equal    ${rel1}    ${6}
    ${rel2}    Add Values    1    2    4
    Should Be Equal    ${rel2}    ${7}
    ${rel3}    Add Values    arg1=1    arg3=2
    Should Be Equal    ${rel3}    ${5}
    
Case2
    [Documentation]    演示列表、FOR IN、FOR IN ENUMRATE、FOR IN RANGE操作
    [Tags]    case2
    # 从7.0版本开始，Create List 和 Create Dictionary(包括Set Variable, Set Test Variable, Set Suite Variable and Set Global Variable)建议使用VAR语法
    @{list_var1}    Create List    1    2    3
    Log    ${list_var1}[0]
    # VAR支持指定作用域，可选的有LOCAL(默认值) TEST TASK SUITE GLOBAL
    VAR    @{args1}    11    22    33    scope=LOCAL
    # 列表的部分操作，注意下面通过下标方式访问，需要使用$符号而不是@符号
    Log    ${args1}[1]
    Log    ${args1}[1:]
    Log Many    @{args1}[1:]
    ${rel1}    Add Values    @{args1}
    Should Be Equal    ${rel1}    ${66}
    FOR    ${i}    IN    @{args1}
        Log    ${i}
    END
    FOR    ${idx}    ${val}    IN ENUMERATE    @{args1}
        # 下面演示了几种列表的访问方式
        Log    args1[${idx}] = ${val}, ${args1}[${idx}]
    END
    FOR    ${i}    IN RANGE    1    10    2
        Log    ${i}
    END
    # 修改列表的值
    ${args1}[0]    Set Variable    100
    Log Many    @{args1}

Case3
    [Documentation]    演示字典的操作，对于列表和字典，注意在不同的应用场景下使用 $ 还是 @or&
    [Tags]    case3
    # 字典的部分操作
    VAR    &{args1}    arg1=11    arg3=4
    # 注意这里需要使用$，而不是&
    Log    ${args1}[arg1]
    Log    ${args1.arg1}
    ${rel1}    Add Values    &{args1}
    Should Be Equal    ${rel1}    ${17}
    FOR    ${key}    ${val}    IN    &{args1}
        Log    args1[${key}] = ${val}
    END
    FOR    ${idx}    ${key}    ${val}    IN ENUMERATE    &{args1}
        Log    args1[${key}] = ${val}, index is ${idx}
    END
    # 修改字典的值
    ${args1.arg1}    Set Variable    100
    ${args1}[arg3]    Set Variable    200
    Log Many    &{args1}

Case4
    [Documentation]    演示直接调用python库的几种方式
    [Tags]    case4
    Wait Until Keyword Succeeds    10x    1s    Add Random Values    ${1}

Case5
    [Documentation]    演示部分内置变量、环境变量的访问
    [Tags]    case5
    # 环境变量
    Log    %{JAVA_HOME}
    # 如果环境变量不存在，还可以设置默认值
    Log    %{DEFAULT_ENV=10}

    # 其它内置变量
    Log    ${CURDIR}    # 脚本文件的路径
    Log    ${TEMPDIR}
    Log    ${EXECDIR}    # 即命令是在哪个路径下执行的

Case6
    [Documentation]    演示自定义变量，可以通过命令行参数动态改变变量
    [Tags]    case6
    # 当使用命令行 robot -i case6 all_syntax_example.robot 时ROBOT变量的值是: Robotframework 1.0
    # 当使用命令行 robot -i case6 -v ROBOT:"Robotframework 2.0" all_syntax_example.robot 时ROBOT变量的值是: Robotframework 2.0
    Log    ${ROBOT}
    
    # py定义的变量
    Log    ${OBJ_VAR}
    Log    ${OBJ_VAR.name}
    Log    ${INT_VAR}

Case7
    [Documentation]    直接执行表达式
    [Tags]    case7
    ${var1}    Set Variable

*** Keywords ***
Add Values
    [Documentation]    Keyword documentation
    [Arguments]    ${arg1}    ${arg2}=2    ${arg3}=3
    ${ret}    Evaluate    ${arg1} + ${arg2} + ${arg3}
    RETURN    ${ret}

Add Random Values
    [Arguments]    ${arg1}
    # 演示直接调用python库的几种方式
    Should Be Equal    ${arg1}    ${{random.randint(0, 1)}}
    ${rel1}    Evaluate    random.randint(0, 1)
    Should Be Equal    ${arg1}    ${rel1}
    ${rel2}    Evaluate    random.randint(0, 1)    modules=random
    Should Be Equal    ${arg1}    ${rel2}
    # 下面的方式不支持，即使用了modules，在调用的时候必须要给定模块名
    # ${rel3}    Evaluate    randint(0, 1)    modules=random
    # Should Be Equal    ${arg1}    ${rel3}