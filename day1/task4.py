# 第一题解答
s1 = "Python is a powerful programming language"
s2 = " Let's learn together"

# (1) 提取单词"language"
words = s1.split()  # 以空格分隔单词
last_word = words[-1]  # 取最后一个单词
print("(1) 最后一个单词:", last_word)  # 输出: language

# (2) 连接s1和s2并重复输出3次
combined = s1 + s2
print("\n(2) 连接后重复输出3次:")
print(combined * 3)  # 重复输出三次

# (3) 输出所有以p或P开头的单词
print("\n(3) 以p/P开头的单词:")
for word in words:
    if word.lower().startswith('p'):  # 不区分大小写检查
        print(word)

# 第二题解答
s3 = " Hello, World! This is a test string."

# (1) 去除字符串前后的空格
stripped = s3.strip()
print("\n(1) 去除前后空格后:", stripped)

# (2) 将所有字符转换为大写
uppered = stripped.upper()
print("(2) 转换为大写:", uppered)

# (3) 查找子串"test"的起始下标
test_index = stripped.find("test")
print("(3) 'test'起始下标:", test_index)  # 输出: 24

# (4) 将"test"替换为"practice"
replaced = stripped.replace("test", "practice")
print("(4) 替换后字符串:", replaced)

# (5) 以空格分割并用"-"连接
words_list = stripped.split()
joined = "-".join(words_list)
print("(5) 分割并连接后:", joined)

