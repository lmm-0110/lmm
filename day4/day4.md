# 第四天实训报告

## 一、实训目标
基于泰坦尼克号数据集，完成：
1. 数据探索性分析（EDA）
2. 理解监督学习流程
3. 认识深度学习核心结构
4. 区分监督学习与无监督学习的应用场景

## 二、数据探索分析
### 直方图分析
- **年龄分布**：
  - 20-40岁乘客占比最高，呈现右偏分布
  - 儿童（<10岁）生还率显著高于其他年龄段，体现救援优先级策略
- **舱位等级**：
  - 三等舱乘客占比近50%
  - 生还率最低（仅约25%），印证社会等级对生存机会的影响

### 柱形图分析
- **性别与生还率**：
  - 女性生还率高达74.2%（男性仅18.9%）
  - 凸显"妇孺优先"救援原则
- **综合特征交叉分析**：
  - 头等舱女性生还率超95%
  - 三等舱男性生还率不足15%
  - 证明**特征交互**对预测的关键作用

## 三、监督学习实践
### 流程实现（参照训练流程图）
1. **模型训练**：
   - 前向传播 → 计算损失 → 反向传播 → 权重更新
   - 损失计算：交叉熵损失函数
2. **验证阶段**：
   - 批量样本验证 → 计算指标 → 输出评估结果
3. **模型选择**：
   - 本任务为二分类监督学习（标签：生还/未生还）
   - 与传统无监督学习形成对比（后者无需标签）

## 四、深度学习扩展
### 核心结构认知（参照网络结构图）
| 网络结构      | 核心特点                          | 应用场景                  |
|---------------|-----------------------------------|--------------------------|
| **CNN**       | 卷积层提取空间特征，池化层降维    | 图像识别/特征提取         |
| **LSTM**      | 门控机制解决长序列遗忘问题        | 时间序列预测              |
| **Transformer**| 自注意力机制捕捉全局依赖          | 自然语言处理              |
| **GAN**       | 生成器-判别器对抗训练             | 生成合成数据/小样本增强   |

## 五、实验总结
### 监督学习核心价值
- 通过端到端训练流程验证特征工程的决定性影响
- 证实性别与舱位的强关联性对预测结果的关键作用

### 深度学习延伸意义
- 不同网络结构对应不同数据形态处理方案：
  - CNN → 空间数据（图像）
  - LSTM → 时间序列数据
  - Transformer → 序列依赖数据
  - GAN → 数据生成任务

### 优化方向
1. 引入集成学习（如随机森林）对比深度学习模型
2. 应用GAN生成少数类别样本解决生还标签不平衡问题
3. 扩展处理非结构化数据（乘客评论/船票图像）