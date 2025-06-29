# 题目1：输出1-100的素数
def find_primes():
    print("1到100之间的所有素数：")
    for num in range(2, 101):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
    print("\n" + "-"*40)

find_primes()

# 题目2：计算斐波那契数列前20项
def fibonacci_sequence():
    fib = [0, 1]
    for _ in range(18):
        fib.append(fib[-1] + fib[-2])

    print("斐波那契数列前20项：")
    for i in range(0, 20, 5):
        print(fib[i:i + 5])
    print("-" * 40)
fibonacci_sequence()

# 题目3：计算满足条件的数之和
def conditional_sum():
    total = 0
    num = 1
    count = 0

    while num <= 10000:
        if (num % 3 == 0 or num % 5 == 0) and num % 15 != 0:
            total += num
            count += 1
        num += 1

    print(f"1-10000之间满足条件的数共有 {count} 个")
    print(f"它们的和是：{total}")
    print("-" * 40)
conditional_sum()