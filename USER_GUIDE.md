# Meeting Atmosphere MCP 用户指南

## 服务简介

Meeting Atmosphere MCP 是一个专为改善会议和团队活动氛围而设计的工具集合。该服务提供了多种功能，包括生成破冰游戏和提供休闲笑话，旨在帮助团队建立更好的沟通氛围，增强团队凝聚力。

## 适用场景

### 1. 团队会议开场
当团队成员聚集在一起开会时，使用破冰游戏可以帮助大家放松心情，打破沉默，快速进入状态。

### 2. 新团队建设
新组建的团队或新成员加入时，通过有趣的破冰游戏可以让成员们更快地相互了解和熟悉。

### 3. 培训和工作坊
在培训课程或工作坊开始时，适当的破冰活动可以帮助参与者集中注意力，提高参与度。

### 4. 团建活动
团建活动中穿插轻松的小游戏和笑话，可以增加活动的趣味性，让团队成员更好地享受活动时光。

## MCP 服务功能

### 1. 破冰游戏生成器 (ice_breaking_game)
根据参与人数生成适合的破冰游戏建议。

**参数:**
- `num_people` (int): 参与游戏的人数
- `number` (int, 可选): 需要生成的游戏数量，默认为1

**返回值:**
- `List[str]`: 破冰游戏描述列表

### 2. 笑话提供器 (jokes)
获取一组随机笑话，为会议增添轻松氛围。

**参数:**
- `count` (int): 需要的笑话数量

**返回值:**
- `List[str]`: 笑话列表

## 使用方法

### 前置条件
- Python 3.13 或更高版本
- 安装了 uv 包管理器
- 配置好必要的环境变量（如 API 密钥）

### 安装步骤
1. 克隆项目到本地
2. 运行以下命令安装依赖:
   ```bash
   uv sync
   ```
   
如果在 `uv sync` 过程中遇到网络问题，特别是下载 Python 解释器时，请尝试以下解决方案:

#### 方案 1: 使用系统已有的 Python
```bash
# 让 uv 使用系统 Python 而不是下载新的
uv python install
uv sync
```

#### 方案 2: 配置 Python 下载镜像
```bash
# 使用托管 Python 构建的镜像
export UV_PYTHON_INSTALL_MIRROR=https://npmmirror.com/mirrors/python-build-standalone
uv sync
```

### 运行服务
安装完成后，使用以下命令启动服务:
```bash
uv run python server.py
```

服务将在 `0.0.0.0:8080/mcp` 上运行。

### 环境变量配置
为了正常使用服务，您需要配置以下环境变量:

1. `DASHSCOPE_API_KEY`: 阿里云百炼平台的 API 密钥，用于生成破冰游戏
2. `JOKE_API_KEY`: 笑话 API 的密钥（可选，默认已提供测试密钥）

您可以通过创建 `.env` 文件来配置这些环境变量:
```env
DASHSCOPE_API_KEY=your_api_key_here
JOKE_API_KEY=your_joke_api_key_here
```

## 技术架构

本服务基于 FastMCP 框架构建，使用 Python 开发。通过集成大语言模型，能够智能生成符合要求的内容。

## 自定义配置

您可以根据需要进行以下自定义配置:
- 在 config.py 中修改模型配置
- 设置环境变量以使用自定义 API 密钥
- 修改提示词以适应特定的使用场景