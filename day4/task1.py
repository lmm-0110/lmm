import numpy as np
import matplotlib.pyplot as plt

# 国家列表
countries = ['挪威', '德国', '中国', '美国', '瑞典']

# 奖牌数据
gold_medal = np.array([16, 12, 9, 8, 8])       # 金牌个数
silver_medal = np.array([8, 10, 4, 10, 5])     # 银牌个数
bronze_medal = np.array([13, 5, 2, 7, 5])       # 铜牌个数

# 设置图表坐标
x = np.arange(len(countries))  # 生成国家索引
plt.xticks(x, countries)      # 设置x轴国家标签

# 绘制分组柱状图
plt.bar(x - 0.2, gold_medal, width=0.2, color="gold", label="金牌")
plt.bar(x, silver_medal, width=0.2, color="silver", label="银牌")
plt.bar(x + 0.2, bronze_medal, width=0.2, color="saddlebrown", label="铜牌")

# 添加数据标签（移除代码中的字母"I"）
# 金牌标签
for i in x:
    plt.text(i - 0.2, gold_medal[i], gold_medal[i],
             va='bottom', ha='center', fontsize=8)
# 银牌标签
for i in x:
    plt.text(i, silver_medal[i], silver_medal[i],
             va='bottom', ha='center', fontsize=8)
# 铜牌标签
for i in x:
    plt.text(i + 0.2, bronze_medal[i], bronze_medal[i],
             va='bottom', ha='center', fontsize=8)

plt.legend()  # 显示图例
plt.title("各国冬奥会奖牌数量分布")  # 添加标题（建议补充）
plt.ylabel("奖牌数量")              # 添加y轴标签（建议补充）
plt.tight_layout()  # 自动调整布局
plt.show()