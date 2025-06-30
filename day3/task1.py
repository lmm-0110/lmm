import requests
from bs4 import BeautifulSoup
import random
import time
import json


def get_douban_top10():
    # 使用API接口替代直接网页爬取，更稳定
    api_url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_top250/items"

    # 精心设计的请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Host": "m.douban.com",
        "Origin": "https://movie.douban.com",
        "Referer": "https://movie.douban.com/top250",
        "X-Requested-With": "XMLHttpRequest"
    }

    # API参数
    params = {
        "start": "0",
        "count": "10",  # 只获取前10部
        "items_only": "1"
    }

    try:
        # 随机延迟防止高频请求
        time.sleep(random.uniform(1.5, 3.5))

        # 发送API请求
        response = requests.get(
            api_url,
            headers=headers,
            params=params,
            timeout=20
        )

        # 检查响应状态
        if response.status_code == 200:
            data = response.json()
            movies = data["subject_collection_items"]

            # 提取前10部电影名称
            top10 = [movie["title"] for movie in movies]
            return top10

        else:
            print(f"请求失败，状态码: {response.status_code}")
            print(f"响应内容: {response.text[:200]}")  # 显示部分响应内容帮助调试
            return []

    except Exception as e:
        print(f"发生错误: {str(e)}")
        return []


# 获取并打印结果
if __name__ == "__main__":
    print("正在从豆瓣获取电影信息，请稍候...")
    top10_movies = get_douban_top10()

    print("\n豆瓣电影Top10:")
    if top10_movies:
        for idx, title in enumerate(top10_movies, 1):
            print(f"{idx}. {title}")
    else:
        print("未能获取电影信息，可能是反爬机制加强或网络问题")
        print("请尝试以下解决方案:")
        print("1. 等待一段时间后重试")
        print("2. 更换网络环境（如切换WiFi/4G）")
        print("3. 使用VPN或代理服务器")