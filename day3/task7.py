import numpy as np
import matplotlib.pyplot as plt

# 创建数据点：从-2到2生成200个等间距点
x = np.linspace(-2, 2, 200)
y = x ** 3  # 计算立方值

# 创建画布和坐标轴
plt.figure(figsize=(8, 6))  # 设置图像大小
plt.axhline(y=0, color='black', linewidth=0.5)  # 绘制x轴
plt.axvline(x=0, color='black', linewidth=0.5)  # 绘制y轴
plt.plot(x, y, 'b-', linewidth=2, label='$y = x^3$')  # 绘制曲线，并添加LaTeX公式标签

# 添加标签和标题
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Cubic Function: $y = x^3$', fontsize=14)
plt.legend()  # 显示图例

# 显示网格线
plt.grid(True, linestyle='--', alpha=0.7)

# 设置坐标轴范围
plt.xlim(-2, 2)
plt.ylim(-8, 8)

# 显示图像
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# 修正1：创建包含20个年份的数组（原代码只有1个年份）
year = np.full(20, '2019')  # 创建20个'2019'

# 生成随机月份和日期
month = np.random.randint(1, 13, size=20).astype(str)
day = np.random.randint(1, 31, size=20).astype(str)

date = np.array([])
for i in range(20):
    # 修正2：正确拼接日期字符串
    b = f"{year[i]}/{month[i]}/{day[i]}"
    date = np.append(date, b)

sales = np.random.randint(500, 2000, size=len(date))

plt.figure(figsize=(12, 6))
plt.xticks(
    range(0, len(date), 2),
    [f'日期:{d}' for d in date][::2],
    rotation=45,
    color='red'
)
plt.plot(date, sales, marker='o')
plt.tight_layout()  # 自动调整布局
plt.show()