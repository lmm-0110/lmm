class Car:
    def __init__(self, brand, speed=0):
        """初始化汽车实例"""
        self.brand = brand  # 品牌
        self.speed = speed  # 速度（初始值0）

    def accelerate(self, m):
        """加速方法：增加m次速度，每次增加10"""
        self.speed += 10 * m
        return self.speed

    def brake(self, n):
        """刹车方法：减少n次速度，每次减少10，不低于0"""
        self.speed = max(0, self.speed - 10 * n)
        return self.speed

    def __str__(self):
        return f"{self.brand}汽车，当前速度: {self.speed}km/h"

# 创建Car实例
my_car = Car("小米")

# 测试加速
print("加速测试:")
my_car.accelerate(3)  # 加速3次
print(my_car)  # 丰田汽车，当前速度: 30km/h

# 测试刹车
print("\n刹车测试:")
my_car.brake(2)  # 刹车2次
print(my_car)  # 丰田汽车，当前速度: 10km/h
my_car.brake(2)  # 尝试刹车（将归零）
print(my_car)  # 丰田汽车，当前速度: 0km/h

#定义ElectricCar子类
class ElectricCar(Car):
    def __init__(self, brand, speed=0, battery=100):
        """初始化电动汽车实例"""
        super().__init__(brand, speed)
        self.battery = min(battery, 100)  # 电量（不超过100%）

    def charge(self):
        """充电方法：电量增加20%，不超过100%"""
        self.battery = min(self.battery + 20, 100)
        return self.battery

    def __str__(self):
        return f"{self.brand}电动汽车，当前速度: {self.speed}km/h，电量: {self.battery}%"

# 测试ElectricCar子类
my_ev = ElectricCar("特斯拉", battery=80)

# 测试充电
print("\n电动车充电测试:")
print(my_ev)  # 特斯拉电动汽车，当前速度: 0km/h，电量: 80%
my_ev.charge()
print(f"充电后电量: {my_ev.battery}%")  # 充电后电量: 100%
print(my_ev)  # 特斯拉电动汽车，当前速度: 0km/h，电量: 100%

# 测试电动车加速
print("\n电动车加速测试:")
my_ev.accelerate(4)
print(my_ev)  # 特斯拉电动汽车，当前速度: 40km/h，电量: 100%

# 测试电量不足边界
print("\n电量不足测试:")
low_ev = ElectricCar("比亚迪", battery=5)
print(f"初始电量: {low_ev.battery}%")
low_ev.charge()
print(f"充电后电量: {low_ev.battery}%")  # 充电后电量: 25%