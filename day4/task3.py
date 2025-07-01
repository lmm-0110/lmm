import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 1. 读取数据
file_path = "E:\\desktop\\train.csv"  # 注意Windows路径使用双反斜杠
titanic_data = pd.read_csv(file_path)

# 2. 按乘客等级分组计算统计量
class_group = titanic_data.groupby('Pclass')['Survived']
result = pd.DataFrame({
    'Total_Passengers': class_group.count(),
    'Survived_Count': class_group.sum(),
})
result['Survived_Rate'] = result['Survived_Count'] / result['Total_Passengers']
result['Not_Survived_Rate'] = 1 - result['Survived_Rate']

# 3. 重置索引并添加中文标签
result.reset_index(inplace=True)
result['Class_Label'] = result['Pclass'].map({1: '头等舱', 2: '二等舱', 3: '三等舱'})

# 4. 打印统计结果
print("乘客等级生还率统计表:")
print("================================")
print(f"{'舱位等级':<10}{'总乘客数':<10}{'生还人数':<10}{'生还率':<10}")
for _, row in result.iterrows():
    print(
        f"{row['Class_Label']:<10}{row['Total_Passengers']:<10}{row['Survived_Count']:<10}{row['Survived_Rate'] * 100:.2f}%")

# 5. 创建堆叠柱状图
plt.figure(figsize=(10, 6))
colors = ['#1f77b4', '#ff7f0e']  # 蓝色和橙色

# 绘制生还部分（底部）
bars = plt.bar(result['Class_Label'], result['Survived_Rate'],
               color=colors[0], label='生还者')

# 绘制遇难部分（堆叠在生还部分之上）
plt.bar(result['Class_Label'], result['Not_Survived_Rate'],
        bottom=result['Survived_Rate'], color=colors[1], label='遇难者')

# 6. 添加数据标签
for i, bar in enumerate(bars):
    surv_rate = result.loc[i, 'Survived_Rate']
    not_surv_rate = result.loc[i, 'Not_Survived_Rate']
    total = result.loc[i, 'Total_Passengers']

    # 在生还部分标注生还率
    plt.text(bar.get_x() + bar.get_width() / 2,
             surv_rate / 2,
             f'{surv_rate * 100:.1f}%',
             ha='center', va='center', color='white', fontsize=12, fontweight='bold')

    # 在遇难部分标注遇难率
    plt.text(bar.get_x() + bar.get_width() / 2,
             surv_rate + not_surv_rate / 2,
             f'{not_surv_rate * 100:.1f}%',
             ha='center', va='center', color='white', fontsize=12, fontweight='bold')

    # 在柱顶标注总人数
    plt.text(bar.get_x() + bar.get_width() / 2,
             surv_rate + not_surv_rate + 0.02,
             f'总人数: {total}',
             ha='center', va='bottom', fontsize=10)

# 7. 美化图表
plt.title('泰坦尼克号乘客等级与生还率关系', fontsize=16, fontweight='bold')
plt.ylabel('比例', fontsize=12)
plt.ylim(0, 1.1)  # 为顶部标注留出空间
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1.0))  # y轴显示百分比
plt.legend(loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 8. 添加分析结论
plt.figtext(0.5, -0.1,
            "分析结论：头等舱乘客生还率(62.96%)显著高于二等舱(47.28%)和三等舱(24.24%)，"
            "表明乘客等级对生还机会有重大影响",
            ha="center", fontsize=12, fontstyle='italic', wrap=True)

plt.tight_layout()
plt.subplots_adjust(bottom=0.2)  # 为底部文本留空间
plt.savefig('titanic_survival_by_class.png', dpi=300, bbox_inches='tight')
plt.show()