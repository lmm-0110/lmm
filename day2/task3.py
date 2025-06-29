import os
import re

# Windows自然排序键生成器
def windows_natural_sort_key(filename):
    """
    生成Windows资源管理器风格的自然排序键
    示例: File1.txt, File2.txt, File10.txt (而不是File1, File10, File2)
    """
    # 将数字部分转换为固定长度字符串，确保数值顺序正确
    convert = lambda text: text.zfill(8) if text.isdigit() else text.lower()
    return [convert(t) for t in re.split(r'(\d+)', filename)]


def natural_sort_key(s):
    """实现特定排序规则：数字按自然���序，但带前导零的数字排在相同值的数字之前"""
    def convert(text):
        if text.isdigit():
            num_val = int(text)
            # 如果是以0开头的数字，返回一个特殊的元组使其排在普通数字之前
            if text.startswith('0') and len(text) > 1:
                return (num_val - 0.5, text)
            return (num_val, text)
        return text.lower()

    return [convert(p) for p in re.split('([0-9]+)', s)]

def rename_images():
    # 定义路径 - 使用原始路径
    txt_path = r"C:\Users\86158\Desktop\names.txt"
    image_folder = r"C:\Users\86158\Desktop\新建文件夹"

    # 步骤1: 读取文本文档中的名字
    with open(txt_path, 'r', encoding='utf-8') as f:
        names = [name.strip() for name in f.readlines() if name.strip()]

    # 步骤2: 获取图片文件列表
    files = os.listdir(image_folder)

    # 步骤3: Windows自然排序（按文件名中的数字顺序排列）
    # 使用Windows资源管理器式的自然排序算法
    files.sort(key=natural_sort_key)

    # 步骤4: 只处理图片文件（保留原有扩展名）
    image_files = [f for f in files if os.path.isfile(os.path.join(image_folder, f))
                   and f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # 步骤5: 重命名图片文件
    for i, name in enumerate(names):
        # 确保索引在范围内
        if i >= len(image_files):
            break

        old_filename = image_files[i]
        # 获取原文件扩展名
        extension = os.path.splitext(old_filename)[1]

        # 构建完整路径
        old_path = os.path.join(image_folder, old_filename)
        new_path = os.path.join(image_folder, f"{name}{extension}")

        # 执行重命名
        os.rename(old_path, new_path)
        print(f"已重命名: {old_filename} -> {name}{extension}")


# 运行主函数
if __name__ == "__main__":
    # 确认操作
    confirm = input("将按Windows自然排序规则重命名图片文件，是否继续? (y/n): ").lower()
    if confirm == 'y':
        rename_images()
        print("重命名操作已完成!")
    else:
        print("操作已取消")