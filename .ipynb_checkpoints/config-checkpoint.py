import os
from dotenv import load_dotenv

# 1. 自动加载同目录下的 .env 文件
load_dotenv()

# 2. 集中读取环境变量（如果没读到，会报错提示你，而不是运行到一半才报错）
ZHIPUAI_API_KEY = os.getenv("ZHIPUAI_API_KEY")
if not ZHIPUAI_API_KEY:
    raise ValueError("❌ 未找到 ZHIPUAI_API_KEY，请检查 .env 文件是否存在且格式正确")

# 3. 其他配置也可以放在这里（比如模型路径、向量库地址等）
EMBEDDING_MODEL = "text2vec-base-chinese"
LLM_MODEL = "glm-4-flash"
