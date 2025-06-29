#第一题
even_numbers = [num for num in range(1, 101) if num % 2 == 0]
print("1-100之间的所有偶数：")
for i in range(0, len(even_numbers), 10):
    print(*even_numbers[i:i+10])
#第二题
original_list = [3, 2, 1, 2, 4, 3, 5, 1, 6, 4]
unique_list = list(dict.fromkeys(original_list))
print(f"原始列表: {original_list}")
print(f"去重后的列表: {unique_list}")
#第三题
keys = ["a", "b", "c"]
values = [1, 2, 3]
result_dict = dict(zip(keys, values))
print("合并后的字典：")
for key, value in result_dict.items():
    print(f"{key}: {value}")
keys = ["a", "b", "c"]
values = [1, 2, 3]
result_dict = dict(zip(keys, values))
print("合并后的字典：")
for key, value in result_dict.items():
    print(f"{key}: {value}")

# 第四题
student_info = ("张三", 18, 92.5)
name, age, score = student_info
print("学生信息：")
print(f"姓名: {name}")
print(f"年龄: {age}岁")
print(f"成绩: {score}分")