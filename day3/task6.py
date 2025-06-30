import pandas as pd
import numpy as np

# 1. 创建包含指定数据的DataFrame
data = {
    'Student_ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', None, 'David', 'Eva'],
    'Score': [92.5, 88.0, np.nan, 76.5, 95.0],
    'Grade': ['A', 'B+', 'B', 'C+', 'A']
}

df = pd.DataFrame(data)

# 使用to_csv()创建初始CSV文件
df.to_csv('students.csv', index=False)

# 2. 读取CSV文件并打印前3行
students = pd.read_csv('students.csv')
print("前3行数据：")
print(students.head(3))

# 3. 填充缺失值
score_mean = students['Score'].mean()  # 计算Score列平均分
students_cleaned = students.fillna({
    'Score': score_mean,      # 用平均分填充Score缺失值
    'Name': 'Unknown'        # 用Unknown填充Name缺失值
})

# 4. 保存处理后的DataFrame到新文件
students_cleaned.to_csv('students_cleaned.csv', index=False)

print("\n缺失值处理结果：")
print(students_cleaned)
print(f"\n文件已保存为 students_cleaned.csv，平均分={score_mean:.2f}")