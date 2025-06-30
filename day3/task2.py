import os
import requests
from lxml import etree


def download_images():
    url = "http://pic.netbian.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        # 创建图片保存目录
        os.makedirs('d:/images', exist_ok=True)

        # 获取网页内容
        rs = requests.get(url, headers=headers)
        rs.encoding = 'gbk'
        body = rs.text

        # 解析图片链接
        html = etree.HTML(body)
        listImg = html.xpath("//ul[@class='clearfix']/li/a/span/img/@src")
        print("发现图片数量:", len(listImg))

        # 下载图片
        for i, img_src in enumerate(listImg):
            # 构建完整图片URL
            img_url = url.rstrip('/') + img_src
            print(f"正在下载: {img_url}")

            try:
                img_data = requests.get(img_url, headers=headers).content
                # 从URL中提取正确的文件扩展名
                img_name = os.path.basename(img_src)
                save_path = f'd:/images/{i}_{img_name}'

                with open(save_path, 'wb') as f:
                    f.write(img_data)
                print(f"已保存: {save_path}")

            except Exception as e:
                print(f"下载失败 {img_url}: {str(e)}")

        print("下载完成")

    except Exception as e:
        print(f"操作失败: {str(e)}")


if __name__ == "__main__":
    download_images()