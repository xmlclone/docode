import logging
import pandas as pd

from logger import config_logging


# 如果需要操作excel，需要提前安装: pip install openpyxl


config_logging(
    console_level=logging.DEBUG,
    convert_newline=False,
)
logger = logging.getLogger(__name__)


def printf(data, prompt='', console=True, wait=True):
    if console:
        if prompt: print(prompt)
        print(data)
        print('=' * 50)
    if wait:
        input()


if __name__ == '__main__':
    # 大部分方法有一个 inplace(默认False) 参数，表示是否直接影响原始对象
    # 比如 df.dropna inplace默认情况下是False，会创建一个新的对象返回，原始对象不受影响
    # 但如果 inplace 指定为True，则直接修改的原始对象

    # 不指定 sheet_name 默认读取第一个 sheet
    df = pd.read_excel('pandas_data.xlsx', sheet_name='Sheet2')
    printf(df, "全部原始数据：")

    printf(df.head(3), "原始数据前3行：")
    # printf(df.info(), "数据概览：", False)

    # 选择与切片
    printf(df['客户名称'], "选择单列：")
    printf(df[['客户名称', '客户地址']], "选择多列：")
    # printf(df[1])  不支持此
    printf(df[1:2], "选择第一行：")
    printf(df[2:], "选择从第2行开始到结束的行：")
    printf(df[:3], "选择从开始到第2行的数据")
    # 条件选择
    printf(df[df['地区']=='西南'], "选择地区为西南的行：")
    printf(df[df['金额']>500], "选择金额大于500的行：")
    printf(df[(df['地区'].isin(['西南', '华北'])) & (df['金额']>500)], "选择地区在西南或华北且金额大于500的行")

    # 4. 处理缺失值：填充金额列缺失值为0，缺失的数据默认是NaN
    # 演示了直接修改列的示例
    df['金额'] = df['金额'].fillna(0)
    printf(df, "处理缺失金额后：")

    # 5. 删除包含缺失值的行
    df_clean = df.dropna(subset=['客户名称'])
    printf(df_clean, "处理缺失客户后：")

    # 为了后续示例，把缺失的客户处理为字符串，默认是NaN，是float型的
    # fillna 也支持inplace=True, 但是这里不建议使用
    df['客户名称'] = df['客户名称'].fillna("")

    # 6. 数据筛选：选择金额大于500的记录
    high_value = df[df['金额'] > 500]
    printf(high_value, "筛选金额大于500的数据：")

    # 7. 添加计算列：计算含税金额（假设税率10%）
    df['含税金额'] = df['金额'] * 1.10
    printf(df, "添加一列含税金额：")

    # 8. 分组聚合：按地区统计总金额
    region_sales = df.groupby('地区')['金额'].sum().reset_index()
    printf(region_sales, "按地区统计金额聚合：")

    # 9. 数据排序：按金额降序排列
    df_sorted = df.sort_values('金额', ascending=False)
    printf(df_sorted, "按金额降序排列：")

    # 10. 数据类型转换：日期列转换
    df['订单日期'] = pd.to_datetime(df['订单日期'])
    printf(df, "转换订单日期格式：")

    # 11. 时间序列分析：按月统计销售额
    # monthly_sales = df.set_index('订单日期').resample('M')['金额'].sum()
    # printf(monthly_sales, "时间序列分析：按月统计销售额：")

    # 12. 数据透视表：各地区各产品销量
    # pivot_table = pd.pivot_table(df, values='金额', index='地区', columns='产品类别', aggfunc='sum')
    # printf(pivot_table, "数据透视表：各地区各产品销量：")

    # 13. 数据分箱：将金额分为高、中、低三档
    # bins = [0, 300, 600, float('inf')]
    # labels = ['低', '中', '高']
    # df['金额等级'] = pd.cut(df['金额'], bins=bins, labels=labels)
    # printf(df, "数据分箱：将金额分为高、中、低三档：")

    # 14. 数据合并：合并产品信息表
    # products = pd.DataFrame({
    #     '产品ID': [1,2,3],
    #     '类别': ['电子', '家具', '服饰']
    # })
    # df = pd.merge(df, products, left_on='产品类别', right_on='产品ID')
    # printf(df, "数据合并：合并产品信息表：")

    # 15. 字符串处理：提取客户省份
    df['省份'] = df['客户地址'].str.extract(r'^(.*?省)')
    printf(df, "提取客户省份：")

    # 16. 条件更新：标记重点客户
    df['重点客户'] = df['客户名称'].apply(lambda x: '是' if '集团' in x else '否')
    printf(df, "标记重点客户：")

    # 17. 删除列
    df = df.drop(columns=['重点客户'])
    printf(df, "删除重点客户：")

    # 18. 重命名列
    df = df.rename(columns={'金额': '销售额'})
    printf(df, "重命名金额为销售额：")

    # 19. 处理重复数据
    df = df.drop_duplicates(subset=['订单号'])
    printf(df, "删除重复订单号：")

    # 20. 数据抽样：随机抽取5%数据
    # sample = df.sample(frac=0.05)
    # print("处理缺失客户后：")
    # print(df)

    # 21. 保存到新Excel文件（多个sheet）
    with pd.ExcelWriter('processed_sales.xlsx') as writer:
        # index=False表示不要把df里面最前面对每行产生的索引，比如 0 1 2 写入表格
        df.to_excel(writer, sheet_name='处理数据', index=False)
        region_sales.to_excel(writer, sheet_name='地区汇总', index=False)
        # pivot_table.to_excel(writer, sheet_name='数据透视表')

    # print("\n处理完成，结果已保存到 processed_sales.xlsx")

    
