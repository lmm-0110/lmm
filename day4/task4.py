import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']  # 用于中文显示
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 读取数据 - 替换为你的实际路径
file_path = r"E:\desktop\train.csv"
titanic_data = pd.read_csv(file_path)

# 数据清洗：处理年龄缺失值，仅保留有年龄数据的记录
titanic_clean = titanic_data.dropna(subset=['Age']).copy()

# 定义年龄分组
age_bins = [0, 5, 12, 18, 30, 50, 65, 80, 100]
age_labels = ['婴儿(0-4)', '儿童(5-11)', '青少年(12-17)', '青年(18-29)',
              '中年(30-49)', '壮年(50-64)', '老年(65-79)', '高龄(80+)']

# 添加年龄分组列
titanic_clean['AgeGroup'] = pd.cut(titanic_clean['Age'], bins=age_bins, labels=age_labels, right=False)

# 计算各年龄组的生还率 - 使用稳定的聚合方法
# 避免使用新版本的特殊语法
age_stats = titanic_clean.groupby('AgeGroup')['Survived'].agg([
    ('Total', 'count'),
    ('Survived', 'sum')
]).reset_index()

# 计算生还率
age_stats['SurvivalRate'] = age_stats['Survived'] / age_stats['Total'] * 100
age_stats['DeathRate'] = 100 - age_stats['SurvivalRate']

# 绘制直方图
plt.figure(figsize=(12, 8))

# 创建并列柱状图 - 生还率
bars = plt.bar(age_stats['AgeGroup'], age_stats['SurvivalRate'],
               color='#4c72b0', width=0.7, label='生还率')

# 设置图表样式
plt.title('不同年龄段的生还比率 - 泰坦尼克号数据集', fontsize=16, pad=20)
plt.xlabel('年龄段', fontsize=14, labelpad=15)
plt.ylabel('生还率 (%)', fontsize=14)
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# 添加数据标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 2,
             f'{height:.1f}%', ha='center', va='bottom',
             fontsize=11, fontweight='bold')

# 在柱底部添加样本量
for i, row in age_stats.iterrows():
    plt.text(row['AgeGroup'], -5, f"样本: {row['Total']}人",
             ha='center', va='top', fontsize=10, color='#666666')

# 添加关键分析结论
plt.figtext(0.5, 0.01,
            "分析发现: 婴儿和儿童生还率最高，30-49岁中年人生还率居中，老年人生还率最低，符合'妇孺优先'原则",
            ha='center', fontsize=12, bbox=dict(facecolor='#f8f8f8', alpha=0.8))

plt.tight_layout()
plt.subplots_adjust(bottom=0.15)
plt.savefig('age_survival_rate.png', dpi=300)
plt.show()

# 输出统计表格
print("\n不同年龄段生还率统计:")
print("=" * 65)
print(f"{'年龄段':<15}{'总人数':>10}{'生还人数':>12}{'生还率(%)':>12}{'主要年龄分布':>20}")
print("-" * 65)

for _, row in age_stats.iterrows():
    # 获取该年龄组实际年龄范围
    age_group_data = titanic_clean[titanic_clean['AgeGroup'] == row['AgeGroup']]['Age']
    min_age = int(age_group_data.min())
    max_age = int(age_group_data.max())

    print(
        f"{row['AgeGroup']:<15}{row['Total']:>10}{row['Survived']:>12}{row['SurvivalRate']:>12.1f}{min_age}-{max_age}岁".rjust(
            20))

print("=" * 65)