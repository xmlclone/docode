# sqlite3

```sh
# sqlite
sqlite3 xxxx.db
# 注意命令结尾是否有;
.tables
.schema mg_tg_caserunrecord

# 查找失败用例
select * from mg_tg_caserunrecord where status!=1 and date="2023-12-19";
# 查询当日执行了多少轮
select max(round_id) from mg_tg_caserunrecord where date="2023-12-19";
```