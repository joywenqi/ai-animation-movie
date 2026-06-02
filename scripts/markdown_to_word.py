#!/usr/bin/env python3
"""
Markdown 转 Word 文档脚本
自动将预算 Markdown 文件转换为 Word 格式
"""

import os
import subprocess
from pathlib import Path

def convert_markdown_to_word():
    """
    使用 Pandoc 将 Markdown 转换为 Word
    """
    
    # 源文件和目标文件
    source_file = "docs/BUDGET_DETAILED.md"
    output_file = "output/AI_ANIMATION_MOVIE_BUDGET.docx"
    
    # 创建输出目录
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Pandoc 命令
    cmd = [
        "pandoc",
        source_file,
        "-o", output_file,
        "--from=markdown",
        "--to=docx",
        "-M", "toc:true",  # 生成目录
        "--toc-depth=2",
        "-M", "lang=zh-CN",  # 中文
    ]
    
    try:
        print("🔄 正在转换 Markdown 为 Word 格式...")
        subprocess.run(cmd, check=True)
        print(f"✅ 转换完成！")
        print(f"📄 输出文件: {output_file}")
        print(f"📊 文件大小: {os.path.getsize(output_file) / 1024:.2f} KB")
    except FileNotFoundError:
        print("❌ 错误: 未找到 Pandoc")
        print("请先安装 Pandoc: https://pandoc.org/installing.html")
    except subprocess.CalledProcessError as e:
        print(f"❌ 转换失败: {e}")

if __name__ == "__main__":
    convert_markdown_to_word()
