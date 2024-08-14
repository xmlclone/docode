"""
pip install mysql-connector-python

docker pull mysql
docker run --rm -itd --network mysql --ip 172.18.0.2 -e MYSQL_ROOT_PASSWORD=123456 -v 3306:3306 mysql
"""


import mysql.connector

# 连接MySQL数据库
db_connection = mysql.connector.connect(
    host="192.168.56.1",  # 数据库主机地址
    user="root",  # 数据库用户名
    password="123456"  # 数据库密码
)

# 创建数据库
def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE demo")  # 创建数据库demo
        print("Database created successfully.")
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))

# 创建用户信息表
def create_table(cursor):
    try:
        cursor.execute("USE demo")  # 使用数据库demo
        cursor.execute("CREATE TABLE users ("
                       "id INT AUTO_INCREMENT PRIMARY KEY,"
                       "username VARCHAR(255),"
                       "age INT,"
                       "email VARCHAR(255))")  # 创建表users
        print("Table created successfully.")
    except mysql.connector.Error as err:
        print("Failed creating table: {}".format(err))

# 插入示例数据
def insert_data(cursor):
    try:
        cursor.execute("USE demo")  # 使用数据库demo
        sql = "INSERT INTO users (username, age, email) VALUES (%s, %s, %s)"
        val = [
            ('John', 30, 'john@example.com'),
            ('Emma', 25, 'emma@example.com'),
            ('Michael', 35, 'michael@example.com')
        ]
        cursor.executemany(sql, val)  # 执行插入操作
        db_connection.commit()  # 提交事务
        print(cursor.rowcount, "record(s) inserted.")
    except mysql.connector.Error as err:
        print("Failed inserting data: {}".format(err))
        db_connection.rollback()  # 回滚事务

if __name__ == "__main__":
    cursor = db_connection.cursor()
    create_database(cursor)
    create_table(cursor)
    insert_data(cursor)
    cursor.close()
    db_connection.close()