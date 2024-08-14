import sqlite3
from datetime import datetime
from datetime import date as Date


db = 'test.db'


class Sqlite:
    def __init__(self) -> None:
        # 如果db文件不存在，会自动创建
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()
        self.table = "my_table"

    def init_table(self):
        sql = f"""CREATE TABLE {self.table} (
            total_round INTEGER,
            round_id INTEGER,
            date DATE,
            case_id TEXT,
            case_name TEXT,
            start_time DATETIME,
            end_time DATETIME,
            status INTEGER
        );"""
        self.execute_sql(sql)

    def drop_table(self):
        sql = f"""DROP TABLE {self.table};"""
        self.execute_sql(sql, commit=True)

    def insert(self, total_round, round_id, case_id, case_name, start_time, end_time, status, date=Date.strftime(Date.today(), "%Y-%m-%d")):
        if isinstance(date, Date):
            date = Date.strftime(date, "%Y-%m-%d")
        if isinstance(end_time, datetime):
            start_time = datetime.strftime(start_time, "%Y-%m-%d %H:%M:%S")
        if isinstance(end_time, datetime):
            end_time = datetime.strftime(end_time, "%Y-%m-%d %H:%M:%S")
        # sql = f"""INSERT INTO my_table (total_round, round_id, date, case_id, case_name, start_time, end_time, status) 
        # VALUES ({total_round}, {round_id}, "{date}", "{case_id}", "{case_name}", "{start_time}", "{end_time}", {status});"""
        sql = f"""INSERT INTO {self.table} VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""
        self.execute_sql(sql, (total_round, round_id, date, case_id, case_name, start_time, end_time, status), True)

    def get_latest_total_round(self):
        sql = f"""SELECT total_round FROM {self.table} ORDER BY total_round DESC;"""
        res = self.execute_sql(sql)
        round = res.fetchone()
        return int(round[0]) if round else 1

    def get_latest_round(self):
        sql = f"""SELECT round_id FROM {self.table} ORDER BY total_round DESC;"""
        res = self.execute_sql(sql)
        round = res.fetchone()
        return int(round[0]) if round else 1

    def execute_sql(self, sql, data=(), commit=False):
        print(sql)
        print(data)
        result = self.cursor.execute(sql, data)
        if commit:
            self.conn.commit()
        return result

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        self.conn.close()


s = Sqlite()
s.drop_table()
s.init_table()
print(s.get_latest_total_round())
s.insert(
    1,
    1,
    Date.today(),
    1,
    'name',
    datetime.now(),
    datetime.now(),
    1
)
print(s.get_latest_total_round())
