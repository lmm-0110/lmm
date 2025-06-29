#第一题
import numpy as np

# 创建3x4二维数组
array_2d = np.arange(1, 13).reshape(3, 4)
print("原始数组:")
print(array_2d)
print()

# 任务1：打印数组属性
print("任务1 - 数组属性:")
print("形状 (shape):", array_2d.shape)
print("维度 (ndim):", array_2d.ndim)
print("数据类型 (dtype):", array_2d.dtype)
print()

# 任务2：数组元素乘以2
array_doubled = array_2d * 2
print("任务2 - 元素乘以2结果:")
print(array_doubled)
print()

# 任务3：重塑为4x3数组
array_reshaped = array_2d.reshape(4, 3)
print("任务3 - 重塑后数组 (4x3):")
print(array_reshaped)

#第二题
array = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]])
row_2 = array[1, :]
print("任务1 - 第2行所有元素:")
print(row_2)

# 任务2: 提取第3列所有元素 (第3列对应索引2)
col_3 = array[:, 2]
print("\n任务2 - 第3列所有元素:")
print(col_3)

# 任务3: 提取子数组(第1-2行，第2-3列) (第1-2行对应索引0:2，第2-3列对应索引1:3)
sub_array = array[0:2, 1:3]
print("\n任务3 - 子数组(第1-2行，第2-3列):")
print(sub_array)

# 任务4: 将大于10的元素替换为0
modified_array = array.copy()  # 创建副本避免修改原始数组
modified_array[modified_array > 10] = 0
print("\n任务4 - 修改后的数组(大于10的元素替换为0):")
print(modified_array)

#第三题
import numpy as np

# 创建数组A (3x2)
A = np.arange(1, 7).reshape(3, 2)
print("数组A:")
print(A)

# 创建数组B (一维数组)
B = np.array([10, 20])
print("\n数组B:")
print(B)

# 任务1：逐元素相加（广播）
addition = A + B
print("\n任务1 - A和B逐元素相加:")
print(addition)

# 任务2：逐元素相乘（广播）
multiplication = A * B
print("\n任务2 - A和B逐元素相乘:")
print(multiplication)

# 任务3：A的每一行与B的点积
dot_products = np.dot(A, B)
print("\n任务3 - A的每一行与B的点积:")
print(dot_products)