大部分语句以`sqlite`举例

# 调整列顺序

*** 注意提前备份数据，防止意外 ***

```sql
-- 原始表格
CREATE TABLE table_1 (
    token TEXT,
    last DATETIME,
    user Text
);

-- 想把 last 和 user 列调整顺序
CREATE TABLE table_1_new (
    token TEXT,
    user Text,
    last DATETIME
);

-- 导入旧表数据
INSERT INTO table_1_new (token, user, last) SELECT token, user, last FROM table_1;
-- 也可以不需要指定新表的列
INSERT INTO table_1_new SELECT token, user, last FROM table_1;

-- 删除旧表后重命名新表
DROP TABLE IF EXISTS table_1;
ALTER TABLE table_1_new RENAME TO table_1;
```