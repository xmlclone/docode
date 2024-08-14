"""
1. create_engine函数: https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.create_engine
"""


import json

from sqlalchemy import create_engine
from sqlalchemy import text


print('-' * 100)
DB_URI = "sqlite+pysqlite:///:memory:"
ECHO = False
engine = create_engine(
    DB_URI, 
    echo=ECHO,  # 输出 sqlalchemy 日志

    # ---------------更多参数---------------
    # 隐藏sql语句参数
    hide_parameters=False,

    # json序列化和反序列化
    json_deserializer=json.loads,
    json_serializer=json.dumps,

    # 指定连接池数量
    pool_size=5,
    # 连接池相关日志
    echo_pool=False,
    # 连接池溢出最大值
    max_overflow=10,
    # 连接池回收时间, -1 表示不回收
    pool_recycle=-1,
)


with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())
print('-' * 100)


# engine.connect如果对数据库有增删改操作，需要调用commit()主动提交事务
# 可以使用 with engin.begin() 的模式， engin.begin() 会自动完成事务提交，即不用在代码内调用commit
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    # 参数化，在sql里面值使用:p代替
    # 值字段可以是列表表示多条数据，比如下面的insert插入多条数据
    # 值字段也可以是字典，比如下面的 select 查询条件
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
    )
    conn.commit()

    # [(2, 4)]
    result = conn.execute(text('select * from some_table where x>:x'), {'x': 1})
    print(result.all())

    result = conn.execute(text("select * from some_table"))
    # result.all() 返回的是一个列表，每个元素是元组
    # [(1, 1), (2, 4)]
    print(result.all())

    # 还可以直接通过for遍历result，并且通过列名访问数据
    # ** 注意 result是一个类型迭代器的对象，只能使用一次，即上面 result.all() 后前面的result数据就被遍历完成
    # 如果需要重新使用需要重新选择数据(当然也可以通过转为List永久使用，但是不建议)
    result = conn.execute(text("select * from some_table"))
    for row in result:
        print(f"{row.x=}, {row.y=}")

    # 另外一种遍历方式
    result = conn.execute(text("select * from some_table"))
    for x, y in result:
        print(f"{x=}, {y=}")

    # 另外一种遍历方式
    result = conn.execute(text("select * from some_table"))
    for row in result:
        print(f"{row[0]=}, {row[1]=}")

    result = conn.execute(text("select * from some_table where x=3"))
    # 如果选择数据不存在，返回的是空列表
    # 注意不能通过 result 来判断是否有返回，result一定不是假，即if result永远为真
    # <sqlalchemy.engine.cursor.CursorResult object at 0x0000027F89051940> []
    print(result, result.all())

    result = conn.execute(text("select x from some_table"))
    # 就算只选择一列数据，返回的列表的元素仍是元组类型的
    # [(1,), (2,)]
    print(result.all())
print('-' * 100)