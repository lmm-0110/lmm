#第一题
def is_palindrome(num):
    """判断一个整数是否是回文数"""
    num_str = str(num)
    return num_str == num_str[::-1]

# 测试示例
print(is_palindrome(121))  # 输出: True
print(is_palindrome(123))  # 输出: False
#第二天
def calculate_average(*args):
    """计算任意数量参数的平均值"""
    if not args:
        return 0
    return sum(args) / len(args)

# 测试示例
print(calculate_average(1, 2, 3))    # 输出: 2.0
print(calculate_average(10, 20, 30, 40))  # 输出: 25.0
#第三题
def find_longest_string(*strings):
    """从任意多个字符串中返回最长的"""
    if not strings:
        return None
    return max(strings, key=len)

# 测试示例
print(find_longest_string("apple", "banana", "cherry"))  # 输出: banana
print(find_longest_string("Python", "Java", "C++"))      # 输出: Python

#第四题
def area(width, height):
    """计算矩形面积"""
    return width * height

def perimeter(width, height):
    """计算矩形周长"""
    return 2 * (width + height)
from rectangle import area, perimeter

# 计算一个5×3矩形的面积和周长
rect_area = area(5, 3)
rect_perim = perimeter(5, 3)

print(f"面积: {rect_area}")     # 输出: 面积: 15
print(f"周长: {rect_perim}")     # 输出: 周长: 16

