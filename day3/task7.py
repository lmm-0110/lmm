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