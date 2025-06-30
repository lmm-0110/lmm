import time
import random
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# 搜索关键词列表
keywords = [
    "基于视觉信息的煤矸识别分割定位方法",
    "基于YOLO11的无人机航拍图像小目标检测算法",
    "AA-GM-YOLO：基于改进YOLO的机加工切屑监测方法",
    "轻量化输电线路缺陷检测方法",
    "基于关键点检测的服装尺寸测量方法",
    "基于YOLO的小目标检测算法研究"
]


# 随机延时函数
def random_delay(min_t=1, max_t=5):
    time.sleep(random.uniform(min_t, max_t))


# 初始化浏览器设置
def init_browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")

    # 修复：添加无头模式选项，减少资源消耗
    # chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    # 隐藏自动化控制标识
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    return driver


# 模拟人类浏览行为
def human_like_interaction(driver):
    print("模拟人类浏览行为...")
    window_size = driver.get_window_size()
    for _ in range(3):
        x = random.randint(0, window_size['width'] - 100)
        y = random.randint(0, window_size['height'] - 100)
        driver.execute_script(f"window.scrollTo({x}, {y})")
        random_delay(0.5, 1.5)

    # 模拟随机点击空白处
    body = driver.find_element(By.TAG_NAME, 'body')
    for _ in range(2):
        body.click()
        random_delay(0.8, 1.8)


# 生成BibTeX引用键
def generate_citekey(authors, year, title):
    # 提取姓氏（取第一作者）
    if authors and "等" not in authors:
        first_author = re.split(r',|，|、|\s', authors)[0]
        surname = re.sub(r'[\s\W]+', '', first_author.split()[-1] if ' ' in first_author else first_author)
    else:
        surname = "unknown"

    # 简化标题
    short_title = title[:20].replace(' ', '').replace(':', '').replace('-', '')
    short_title = re.sub(r'[\W\s]', '', short_title)

    # 构建引用键
    citekey = f"{surname}{year}{short_title}"[:40]
    return citekey.lower()


# 生成BibTeX条目
def generate_bibtex_entry(article):
    # 生成唯一引用键
    citekey = generate_citekey(article['作者'], article['年份'], article['标题'])

    # 处理作者格式
    authors = article['作者']
    if authors and "等" not in authors:
        # 处理中文作者格式
        authors = authors.replace(',', ' and ').replace('，', ' and ').replace('、', ' and ')
        authors = re.sub(r'\s+', ' ', authors)
        author_list = authors.split(' and ')
        formatted_authors = " and ".join([author.strip() for author in author_list])
    else:
        formatted_authors = "佚名"

    # 构建BibTeX条目
    bibtex_entry = f"@article{{{citekey},\n"
    bibtex_entry += f"  title = {{{article['标题']}}},\n"
    bibtex_entry += f"  author = {{{formatted_authors}}},\n"
    bibtex_entry += f"  journal = {{{article['来源']}}},\n"
    bibtex_entry += f"  year = {{{article['年份']}}},\n"

    # 添加摘要作为注释
    if article['摘要']:
        bibtex_entry += f"  note = {{{article['摘要']}}}\n"
    else:
        bibtex_entry += f"  note = {{摘要不可用}}\n"

    bibtex_entry += "}\n\n"
    return bibtex_entry


# 主爬虫函数
def cnki_crawler():
    driver = init_browser()
    driver.get("https://www.cnki.net")

    all_results = []

    try:
        # 关闭初始弹窗（如果存在）
        try:
            close_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.closebtn"))
            )
            close_btn.click()
            print("关闭了初始弹窗")
            random_delay(1, 2)
        except:
            pass

        for keyword in keywords:
            print(f"\n开始搜索关键词: {keyword}")
            random_delay(2, 4)

            # 定位搜索框并输入关键词 - 改进的选择器
            try:
                # 尝试第一种选择器
                search_box = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "input.search-input"))
                )
            except:
                try:
                    # 尝试备用选择器
                    search_box = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='输入关键词']"))
                    )
                except Exception as e:
                    print(f"无法定位搜索框: {str(e)}")
                    driver.save_screenshot("search_box_error.png")
                    continue

            search_box.clear()

            # 模拟人类输入速度
            for char in keyword:
                search_box.send_keys(char)
                time.sleep(random.uniform(0.1, 0.3))

            random_delay(0.5, 1.5)
            search_box.send_keys(Keys.RETURN)
            print("已提交搜索...")

            # 等待结果加载 - 改进的等待条件
            try:
                WebDriverWait(driver, 15).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, ".title"))
                )
                print("搜索结果已加载")
            except Exception as e:
                print(f"等待结果超时: {str(e)}")
                driver.save_screenshot("results_timeout.png")
                continue

            # 随机等待更长时间
            random_delay(3, 8)
            human_like_interaction(driver)

            # 解析搜索结果 - 更健壮的选择器
            try:
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                results = soup.select("div.result-item, div.list-item")

                if not results:
                    print(f"未找到关键词'{keyword}'的搜索结果")
                    continue

                print(f"找到{len(results)}条结果")

                # 获取结果
                for i, result in enumerate(results):
                    try:
                        # 标题
                        title_elem = result.select_one(".title")
                        if not title_elem:
                            title_elem = result.select_one("a.fz14")
                        title = title_elem.get_text(strip=True) if title_elem else "N/A"

                        # 作者
                        authors_elem = result.select("a.author, span.author a")
                        if not authors_elem:
                            authors_elem = result.select("span.author > a")
                        authors = ", ".join([a.get_text(strip=True) for a in authors_elem]) if authors_elem else "N/A"

                        # 来源
                        source_elem = result.select_one(".source")
                        if not source_elem:
                            source_elem = result.select_one("span.source")
                        source = source_elem.get_text(strip=True) if source_elem else "N/A"

                        # 年份
                        year_elem = result.select_one(".year")
                        if not year_elem:
                            year_elem = result.select_one("span.date")
                        year = year_elem.get_text(strip=True) if year_elem else "N/A"

                        # 摘要
                        abstract_elem = result.select_one(".abstract")
                        if not abstract_elem:
                            abstract_elem = result.select_one("p.abstract")
                        abstract = abstract_elem.get_text(strip=True)[3:] if abstract_elem else "N/A"  # 移除"摘要:"

                        # 保存结果
                        article_data = {
                            "关键词": keyword,
                            "标题": title,
                            "作者": authors,
                            "来源": source,
                            "年份": year,
                            "摘要": abstract
                        }

                        all_results.append(article_data)
                        print(f"结果{i + 1}: {title[:40]}...")

                    except Exception as e:
                        print(f"解析结果时出错: {str(e)}")

                    random_delay(1, 3)

            except Exception as e:
                print(f"解析结果列表时出错: {str(e)}")
                driver.save_screenshot("parse_error.png")

            # 随机等待后返回首页
            random_delay(5, 10)
            driver.get("https://www.cnki.net")

    except Exception as e:
        print(f"爬取过程中出错: {str(e)}")
    finally:
        driver.quit()
        print("\n爬取结束")

    return all_results


# 生成BibTeX文件
def create_bibtex_file(results, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for result in results:
            bibtex_entry = generate_bibtex_entry(result)
            f.write(bibtex_entry)
    print(f"已生成BibTeX文件: {filename}")


# 执行爬虫并保存结果
if __name__ == "__main__":
    print("知网爬虫启动...")
    results = cnki_crawler()

    if results:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        bib_filename = f"cnki_results_{timestamp}.bib"

        # 生成BibTeX文件
        create_bibtex_file(results, bib_filename)

        # 同时保存为CSV以便查看
        import csv

        csv_filename = f"cnki_results_{timestamp}.csv"
        with open(csv_filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
            fieldnames = ['关键词', '标题', '作者', '来源', '年份', '摘要']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for res in results:
                writer.writerow(res)

        print(f"共爬取 {len(results)} 条文献记录")
        print(f"BibTeX文件: {bib_filename}")
        print(f"CSV格式文件: {csv_filename}")
    else:
        print("未爬取到数据")