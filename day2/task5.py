import numpy as np
import rasterio
from PIL import Image

def sentinel2_to_rgb(input_path, output_path):

    with rasterio.open(input_path) as src:
        # 假设波段顺序: [蓝, 绿, 红, 近红外, 短红外]
        blue = src.read(1)
        green = src.read(2)
        red = src.read(3)
        nir = src.read(4)  # 未使用但保留读取
        swir = src.read(5)  # 未使用但保留读取

    # 创建RGB数组
    rgb_stack = np.dstack((red, green, blue))


    def scale_band(band):
        # 仅处理非零值
        valid_pixels = band[band > 0]
        if valid_pixels.size == 0:
            return np.zeros_like(band, dtype=np.uint8)

        low, high = np.percentile(valid_pixels, (2, 98))
        if high <= low:
            # 避免除以零，使用整个范围
            low, high = np.min(valid_pixels), np.max(valid_pixels)
            if high <= low:
                # 如果所有值相同
                scaled = np.zeros_like(band, dtype=np.uint8)
                scaled[band > 0] = 128
                return scaled

        scaled = (band - low) * 255.0 / (high - low)
        scaled = np.clip(scaled, 0, 255)
        return scaled.astype(np.uint8)

    rgb_normalized = np.dstack([
        scale_band(rgb_stack[..., 0]),  # 红
        scale_band(rgb_stack[..., 1]),  # 绿
        scale_band(rgb_stack[..., 2])  # 蓝
    ])

    # 创建并保存图像
    img = Image.fromarray(rgb_normalized)
    img.save(output_path)
    print(f"RGB图像已保存至: {output_path}")


# 使用示例
if __name__ == "__main__":
    # 使用原始字符串解决路径问题
    input_file = r"C:\Users\86158\Desktop\2020_0427_fire_B2348_B12_10m_roi.tif"
    # 输出路径需要包含文件名（建议使用完整路径）
    output_file = r"D:\pycharm.1\sx\day2\rgb_output.jpg"  # 确保有文件名

    # 确保安装了必要的库: pip install rasterio numpy pillow
    sentinel2_to_rgb(input_file, output_file)