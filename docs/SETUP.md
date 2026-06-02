# 🚀 设置指南

## 前置要求

- Python 3.10+
- Node.js 16+
- Docker & Docker Compose
- Git

## API Keys 获取

在开始前，您需要获取以下 API keys：

### 1. OpenAI API
- 访问 https://platform.openai.com/api-keys
- 创建新的 API key
- 复制并保存

### 2. Runway ML API
- 访问 https://app.runwayml.com
- 注册或登录账户
- 生成 API key

### 3. D-ID API
- 访问 https://www.d-id.com
- 创建账户
- 获取 API key

### 4. Stability AI (Stable Diffusion)
- 访问 https://beta.dreamstudio.ai
- 注册账户
- 获取 API key

## 本地开发设置

### 1. 克隆仓库
```bash
git clone https://github.com/yourusername/ai-animation-movie.git
cd ai-animation-movie
```

### 2. 设置后端

```bash
# 创建虚拟环境
cd backend
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 复制环境变量模板
cp .env.example .env

# 编辑 .env 文件，添加您的 API keys
nano .env
```

### 3. 设置前端

```bash
# 进入前端目录
cd ../frontend

# 安装依赖
npm install

# 复制环境变量
cp .env.example .env
```

### 4. 启动 Docker 服务

```bash
# 返回项目根目录
cd ..

# 启动 Docker Compose
docker-compose up -d

# 查看日志
docker-compose logs -f
```

### 5. 初始化数据库

```bash
# 进入后端目录
cd backend

# 运行迁移
python -m alembic upgrade head

# 创建超级用户（可选）
python scripts/create_admin.py
```

### 6. 启动开发服务

在不同的终端窗口中运行：

```bash
# 终端 1 - 启动后端
cd backend
source venv/bin/activate  # 如果还没激活
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

```bash
# 终端 2 - 启动前端
cd frontend
npm run dev
```

## 访问应用

- 🌐 前端: http://localhost:5173
- 🔗 后端 API: http://localhost:8000
- 📚 API 文档 (Swagger): http://localhost:8000/docs
- 📘 API 文档 (ReDoc): http://localhost:8000/redoc
- 🗄️ pgAdmin: http://localhost:5050

## 使用 Docker Compose

### 启动所有服务
```bash
docker-compose up -d
```

### 查看日志
```bash
docker-compose logs -f backend
```

### 停止服务
```bash
docker-compose down
```

### 清理数据（谨慎操作）
```bash
docker-compose down -v
```

## 环境变量配置详解

### 必需的 API Keys
- `OPENAI_API_KEY` - OpenAI 文本生成
- `RUNWAY_API_KEY` - Runway ML 视频生成
- `DID_API_KEY` - D-ID 数字人脸
- `STABILITY_API_KEY` - Stable Diffusion 图像生成

### 数据库配置
- `DATABASE_URL` - PostgreSQL 连接字符串
- `REDIS_URL` - Redis 连接字符串

### 服务器配置
- `SECRET_KEY` - JWT 密钥（改成安全的随机字符串）
- `DEBUG` - 调试模式

## 测试 API

### 使用 curl
```bash
# 获取健康状态
curl http://localhost:8000/health

# 生成剧本
curl -X POST http://localhost:8000/api/v1/scripts/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "一个关于机器人的故事"}'
```

### 使用 Python
```python
import requests

url = "http://localhost:8000/api/v1/scripts/generate"
data = {"prompt": "一个关于未来城市的冒险故事"}
response = requests.post(url, json=data)
print(response.json())
```

## 常见问题

### 数据库连接失败
- 确保 PostgreSQL 正在运行：`docker-compose ps`
- 检查 `DATABASE_URL` 配置
- 查看日志：`docker-compose logs postgres`

### API Key 无效
- 确认 API key 已正确复制到 `.env` 文件
- 检查 API key 是否过期或被禁用
- 访问相应服务的控制面板验证

### 模块导入错误
- 确保虚拟环境已激活
- 重新安装依赖：`pip install -r requirements.txt`

### 端口被占用
- 修改 `docker-compose.yml` 中的端口映射
- 或杀死占用端口的进程

## 下一步

- 查看 [API 文档](./API.md)
- 了解 [使用说明](./USAGE.md)
- 阅读 [开发指南](./DEVELOPMENT.md)

## 获取帮助

- 📖 官方文档: https://docs.example.com
- 💬 Discord: https://discord.gg/example
- 🐛 报告问题: https://github.com/yourusername/ai-animation-movie/issues
