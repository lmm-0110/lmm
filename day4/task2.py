import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 整理后的完整数据集示例
data = {
    "地区": ["北京", "上海", "深圳", "广州", "天津", "重庆", "成都", "武汉", "杭州", "南京", "青岛", "长沙", "宁波", "郑州", "西安"] * 3,
    "年份": [2015]*15 + [2016]*15 + [2017]*15,
    "国内生产总值": [
        # 2015年
        23014.59, 25123.45, 17502.86, 18100.41, 16538.19, 15717.27, 10801.16, 10905.6, 10050.21, 9720.77, 9300.07, 8510.13, 8003.61, 7311.52, 5801.2,
        # 2016年
        25669.13, 28178.65, 19492.6, 19547.44, 17885.39, 17740.59, 12170.23, 11912.61, 11313.72, 10503.02, 10011.29, 9455.36, 8686.49, 8025.31, 6257.18,
        # 2017年
        28014.94, 30632.99, 22490.06, 21503.15, 18549.19, 19424.73, 13889.39, 13410.34, 12603.36, 11715.1, 11037.28, 10535.51, 9842.1, 9130.2, 7469.85
    ]
}
df = pd.DataFrame(data)

# 计算各城市三年平均GDP
gdp_avg = df.groupby('地区')['国内生产总值'].mean().sort_values(ascending=False)
gdp_total = gdp_avg.sum()

# 准备饼图数据（前8大城市+其他城市合并）
top8 = gdp_avg.head(8)
other = pd.Series([gdp_avg[8:].sum()], index=['其他城市'])

# 设置美观的颜色方案
colors = plt.cm.Paired(np.linspace(0, 1, 9))

# 创建饼图
plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(
    pd.concat([top8, other]),
    labels=pd.concat([top8, other]).index,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    pctdistance=0.85,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1}
)

plt.title('主要城市GDP占比（2015-2017平均）', fontsize=16, pad=20)
plt.axis('equal')  # 保持正圆形
plt.tight_layout()
plt.show()
# 筛选GDP最高的6个城市用于柱状图
top_cities = gdp_avg.head(6).index

# 创建多系列柱状图
plt.figure(figsize=(12, 7))
bar_width = 0.25
index = np.arange(len(top_cities))

for i, year in enumerate([2015, 2016, 2017]):
    year_data = df[df['年份'] == year]
    values = [year_data[year_data['地区'] == city]['国内生产总值'].values[0]
              for city in top_cities]

    plt.bar(index + i * bar_width, values, bar_width,
            label=f'{year}年', alpha=0.9)

plt.xlabel('主要城市', fontsize=12)
plt.ylabel('GDP（亿元）', fontsize=12)
plt.title('主要城市GDP年度变化（2015-2017）', fontsize=16, pad=15)
plt.xticks(index + bar_width, top_cities)
plt.legend(title='年份')
plt.grid(axis='y', alpha=0.3)

# 添加数值标签
for city in top_cities:
    for year in [2015, 2016, 2017]:
        value = df[(df['地区'] == city) & (df['年份'] == year)]['国内生产总值'].values[0]
        x_loc = index[list(top_cities).index(city)] + [0, bar_width, 2 * bar_width][year - 2015]
        plt.text(x_loc, value + 500, f'{value / 10000:.1f}万亿' if value > 20000 else f'{value:.0f}亿',
                 ha='center', fontsize=9)

plt.ylim(0, 35000)
plt.tight_layout()
plt.show()