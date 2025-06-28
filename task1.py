# 练习1：数据类型判断
x = 10
y = "10"
z = True
print("练习1输出：")
print(f"变量 x 的类型是：{type(x)}")
print(f"变量 y 的类型是：{type(y)}")
print(f"变量 z 的类型是：{type(z)}")

# 练习2：用户输入与圆面积计算
π = 3.14  # π 定义为常量 3.14
radius_str = input("请输入圆的半径：")
try:
    radius = float(radius_str)
    area = π * (radius ** 2)
    print("练习2输出：")
    print(f"圆的面积是：{area:.2f}")
except ValueError:
    print("输入错误：半径必须是数字！")

# 练习3：类型转换与差异观察
original_str = "3.14"
float_num = float(original_str)
int_num = int(float_num)
print("\n练习3输出：")
print(f"原始字符串：'{original_str}'")
print(f"转换为浮点数：{float_num}（类型：{type(float_num)}）")
print(f"再转换为整数：{int_num}（类型：{type(int_num)}）")
print(f"观察差异：浮点数 {float_num} 转整数后，小数部分丢失，结果为 {int_num}。")