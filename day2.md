# NumPy基础操作与遥感图像处理实践
**日期：** 2025年6月29日  
**核心要点：** NumPy高效数组操作、遥感影像处理、向量化计算优势  

---

## 一、NumPy核心操作精要
### 🧱 数组创建与变形
```python
# 基础数组操作
arr = np.array([1,2,3])  # 创建数组
zeros_mat = np.zeros((3,3))  # 3x3零矩阵
seq_arr = np.arange(0,10,0.5)  # 0-9.5的等差序列

# 数组变形操作
reshaped = arr.reshape(1,3)  # 维度变换
flattened = zeros_mat.ravel()  # 展平为1D数组
# 元素级运算与广播
a = np.array([[1, 2], [3, 4]])
b = np.array([10, 20])
result = a * b  # 广播机制自动扩展计算

# 统计与线性代数
mean_val = np.mean(range_arr)                    # 数据聚合
matrix_prod = np.dot(a, a.T)                     # 矩阵乘法
```
## 二、遥感图像处理实践
### 🧱 数据加载与转换
**数据加载与转换**：使用rasterio库读取.tif格式遥感图像，将其转换为Numpy
数组（三维数组[H,W,Bands]）；验证影像尺寸与波段数。  
**图像操作演示**：  
1.波段提取：分离近红外（NIR）与红光（Red）波段  
```python
nir_band = image_array[:, :, 3]  # 提取第4波段（NIR）  
red_band = image_array[:, :, 0]   # 提取第1波段（Red）  
```
2.NDVI计算：​​ 基于公式 (NIR−Red)/(NIR+Red) 生成植被指数图  
```python
ndvi = (nir_band - red_band) / (nir_band + red_band + 1e-10)  # 避免除零  
```
3.统计输出：​​ 分析NDVI值的分布
```python
（ndvi.min(), ndvi.max(), ndvi.mean()）
```
## 三、总结与思考
**总结**：今日实训将NumPy的抽象概念（如数组广播、向量化运算）落地到遥感场景中，显著体会到其在海量数据处理中的性能优势。操作高分辨率影像时，尤其认识到数组预分配内存与避免循环的重要性。后续需进一步探索NumPy与GDAL、xarray等库的协同使用，提升地学数据分析的效率与深度。
