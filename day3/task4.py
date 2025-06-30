import pandas as pd

# 读取CSV文件 - 改用逗号分隔符
file_path = r"C:\Users\86158\Desktop\drinks.csv"
df = pd.read_csv(file_path)  # 默认使用逗号作为分隔符

# 1. 哪个大陆平均消耗的啤酒更多？
continent_beer = df.groupby('continent')['beer_servings'].mean()
most_beer_continent = continent_beer.idxmax()
print(f"1. 平均消耗啤酒最多的大陆是: {most_beer_continent}\n")

# 2. 打印每个大陆红酒消耗的描述性统计值
wine_stats = df.groupby('continent')['wine_servings'].describe()
print("2. 各大陆红酒消耗的描述性统计:")
print(wine_stats)
print("\n")

# 3. 打印每个大陆每种酒类别的消耗平均值
alcohol_types = ['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']
mean_by_continent = df.groupby('continent')[alcohol_types].mean()
print("3. 各大陆每种酒类别的平均消耗量:")
print(mean_by_continent)
print("\n")

# 4. 打印每个大陆每种酒类别的消耗中位数
median_by_continent = df.groupby('continent')[alcohol_types].median()
print("4. 各大陆每种酒类别的消耗中位数:")
print(median_by_continent)