import pandas as pd
import numpy as np
import os
import re

# 1. 读取并合并数据（修复编码问题）
file_paths = [
    r"C:\Users\86158\Desktop\2015年国内主要城市年度数据.csv",
    r"C:\Users\86158\Desktop\2016年国内主要城市年度数据.csv",
    r"C:\Users\86158\Desktop\2017年国内主要城市年度数据.csv"
]

dfs = []
encodings = ['utf-8']  # 尝试多种可能的编码

for path in file_paths:
    # 从文件名提取年份 - 更健壮的方法
    match = re.search(r'(\d{4})年', path)
    if match:
        year = int(match.group(1))
    else:
        continue  # 跳过无法识别年份的文件

    # 尝试不同编码读取文件
    for encoding in encodings:
        try:
            df = pd.read_csv(path, encoding=encoding)
            print(f"成功读取: {path} (编码: {encoding})")
            break  # 成功读取则跳出编码循环
        except UnicodeDecodeError:
            continue  # 尝试下一个编码

    df['年份'] = year  # 添加年份列
    dfs.append(df)

# 纵向合并数据
merged_df = pd.concat(dfs, ignore_index=True)

# 2. 处理缺失值 (填充为0) - 检查数字列
numeric_cols = merged_df.select_dtypes(include=np.number).columns
merged_df[numeric_cols] = merged_df[numeric_cols].fillna(0)

# 3. 按年份聚合计算全国GDP总和
# 检查列名 - 因为不同年份文件列名可能不同
gdp_col = [col for col in merged_df.columns if '生产总' in col][0]  # 寻找包含"生产总"的列名
retail_col = [col for col in merged_df.columns if '零售' in col][0]  # 寻找包含"零售"的列名
hospital_col = [col for col in merged_df.columns if '医院' in col or '卫生院' in col][0]  # 医疗资源列

yearly_gdp = merged_df.groupby('年份')[gdp_col].sum().reset_index()
yearly_gdp.columns = ['年份', '全国GDP总和(万元)']

# 4. 计算每个城市的GDP年均增长率
# 创建城市GDP透视表
gdp_pivot = merged_df.pivot_table(index='地区', columns='年份', values=gdp_col)


# 计算复合年均增长率 (CAGR)
def calculate_cagr(row):
    try:
        # 确保有2015和2017年数据
        if 2015 in row.index and 2017 in row.index:
            gdp_2015 = row[2015]
            gdp_2017 = row[2017]
            if gdp_2015 > 0 and gdp_2017 > 0:
                return (gdp_2017 / gdp_2015) ** (1 / 2) - 1
        return np.nan
    except Exception as e:
        print(f"计算增长率出错: {e}")
        return np.nan


gdp_pivot['CAGR'] = gdp_pivot.apply(calculate_cagr, axis=1)
growth_rates = gdp_pivot['CAGR'].dropna().sort_values()

# 获取增长率最高和最低的五个城市
top_5 = growth_rates.nlargest(5).reset_index()
top_5.columns = ['城市', '年均增长率']
bottom_5 = growth_rates.nsmallest(5).reset_index()
bottom_5.columns = ['城市', '年均增长率']


# 5. 医疗资源归一化处理 (按年份)
def min_max_normalize(df):
    min_val = df[hospital_col].min()
    max_val = df[hospital_col].max()
    if max_val > min_val:
        df[f'标准化{hospital_col}'] = (df[hospital_col] - min_val) / (max_val - min_val)
    else:
        df[f'标准化{hospital_col}'] = 0
    return df


normalized_df = merged_df.groupby('年份', group_keys=False).apply(min_max_normalize)

# 6. 提取四个特大城市数据
cities = ['北京', '上海', '广州', '深圳']
selected_cities = merged_df[merged_df['地区'].isin(cities)]
selected_cols = selected_cities[['地区', '年份', gdp_col, retail_col]]

# 保存结果 - 使用新方法防止编码错误
try:
    # 尝试用Excel保存
    with pd.ExcelWriter(r'C:\Users\86158\Desktop\城市数据分析结果.xlsx') as writer:
        yearly_gdp.to_excel(writer, sheet_name='年度GDP总和', index=False)
        top_5.to_excel(writer, sheet_name='增长率最高城市', index=False)
        bottom_5.to_excel(writer, sheet_name='增长率最低城市', index=False)
        normalized_df.to_excel(writer, sheet_name='归一化医疗资源', index=False)
        selected_cols.to_excel(writer, sheet_name='四大城市数据', index=False)

    # 额外保存四个城市数据为CSV
    selected_cols.to_csv(r'C:\Users\86158\Desktop\四大城市经济数据.csv',
                         index=False,
                         encoding='gb18030',  # 使用更现代的编码
                         errors='replace')  # 替换无法编码的字符

    print("处理完成！结果已保存到桌面")
except Exception as e:
    print(f"保存文件时出错: {e}")
    # 创建目录保存文件
    output_dir = os.path.join(os.environ['USERPROFILE'], 'Desktop', '城市分析结果')
    os.makedirs(output_dir, exist_ok=True)

    # 分多个小文件保存
    yearly_gdp.to_csv(os.path.join(output_dir, '年度GDP总和.csv'), index=False)
    top_5.to_csv(os.path.join(output_dir, '增长率最高城市.csv'), index=False)
    bottom_5.to_csv(os.path.join(output_dir, '增长率最低城市.csv'), index=False)
    normalized_df.to_csv(os.path.join(output_dir, '归一化医疗资源.csv'), index=False)
    selected_cols.to_csv(os.path.join(output_dir, '四大城市经济数据.csv'), index=False)

    print(f"结果已保存到目录: {output_dir}")

# 打印关键信息摘要
print("\n===== 分析结果摘要 =====")
print(f"> 合并数据总行数: {len(merged_df)}")
print(f"> 覆盖年份: {merged_df['年份'].unique()}")
print(f"> 包含城市数量: {merged_df['地区'].nunique()}")
print(f"> 最高增长率的5个城市:\n{top_5.to_string(index=False)}")
print(f"\n> 最低增长率的5个城市:\n{bottom_5.to_string(index=False)}")
print(f"\n> 四大城市数据已保存")
print("=" * 30)