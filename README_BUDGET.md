# 📊 预算文档转换指南

## 🎯 快速开始

您的项目预算文档已生成，提供以下格式：

### 📄 已生成的文件

```
✅ docs/PROJECT_BUDGET.md          - 完整预算说明 (Markdown)
✅ docs/BUDGET_DETAILED.md         - 详细预算表 (Markdown)
✅ docs/AI_ANIMATION_BUDGET.docx  - Word 文档 (可直接下载)
```

---

## 📥 下载 Word 文档

### 方式 1: 直接下载

访问以下链接直接下载已生成的 Word 文档：

```
https://github.com/joywenqi/ai-animation-movie/raw/main/docs/AI_ANIMATION_BUDGET.docx
```

### 方式 2: GitHub 网页下载

1. 打开项目仓库: https://github.com/joywenqi/ai-animation-movie
2. 进入 `docs` 文件夹
3. 找到 `AI_ANIMATION_BUDGET.docx`
4. 点击 "Raw" 或直接下载

---

## 🔄 Markdown 转 Word 转换

### 方法 A: 使用 Python 脚本（推荐）

#### 安装依赖

```bash
# 安装 python-docx
pip install python-docx

# 或安装所有依赖
pip install -r scripts/requirements.txt
```

#### 运行转换脚本

```bash
# 使用 python-docx 生成专业 Word 文档
python scripts/generate_word_document.py

# 或使用 Pandoc 转换
python scripts/markdown_to_word.py
```

### 方法 B: 使用 Pandoc（需要单独安装）

#### 安装 Pandoc

**Windows:**
```bash
choco install pandoc
# 或下载: https://pandoc.org/installing.html
```

**macOS:**
```bash
brew install pandoc
```

**Linux:**
```bash
sudo apt-get install pandoc
```

#### 转换命令

```bash
# 基础转换
pandoc docs/BUDGET_DETAILED.md -o output/budget.docx

# 高级转换（带目录和格式）
pandoc docs/BUDGET_DETAILED.md \
  -o output/budget.docx \
  --from=markdown \
  --to=docx \
  -M toc:true \
  --toc-depth=2 \
  -M lang=zh-CN
```

### 方法 C: 在线转换工具

1. **Pandoc 在线版**: https://pandoc.org/try/
   - 上传 `BUDGET_DETAILED.md`
   - 选择输出格式为 `docx`
   - 下载转换后的文件

2. **CloudConvert**: https://cloudconvert.com/md-to-docx
   - 支持批量转换
   - 可直接保存到云盘

3. **Zamzar**: https://www.zamzar.com/convert/md-to-docx/
   - 完全免费
   - 支持邮件接收

---

## 📋 文件说明

### PROJECT_BUDGET.md
- **内容**: 项目预算概览和优化方案
- **用途**: 管理层参考、投资方展示
- **大小**: ~8KB

### BUDGET_DETAILED.md
- **内容**: 完整的执行预算表（人民币结算）
- **用途**: 财务部门、项目管理、采购
- **大小**: ~14KB
- **特点**: 
  - ✅ 详细的成本明细
  - ✅ 月度预算分配
  - ✅ 支付节点计划
  - ✅ 风险评估
  - ✅ 财务成果分析

### AI_ANIMATION_BUDGET.docx
- **格式**: Microsoft Word (.docx)
- **用途**: 直接用于办公、打印、分享
- **特点**:
  - ✅ 专业排版
  - ✅ 易于编辑
  - ✅ 支持图表
  - ✅ 可生成PDF

---

## 🎨 自定义 Word 文档

### 使用 python-docx 修改样式

编辑 `scripts/generate_word_document.py`：

```python
# 修改字体
style.font.name = 'SimSun'  # 改为其他中文字体
style.font.size = Pt(11)    # 修改字号

# 修改颜色
title_run.font.color.rgb = RGBColor(0, 0, 139)  # 修改为其他颜色

# 修改表格样式
table.style = 'Light Grid Accent 1'  # 改为其他样式
```

### 直接在 Word 中编辑

1. 下载 `.docx` 文件
2. 在 Microsoft Word/WPS/LibreOffice 中打开
3. 直接修改内容和样式
4. 保存为新文件

---

## 📊 批量生成多个预算版本

运行脚本生成三个不同版本：

```bash
# 创建脚本 batch_generate.py
python scripts/batch_generate_budgets.py
```

输出文件：
- `output/Budget_Basic_600K.docx` - 基础版 (¥600,000)
- `output/Budget_Standard_1M.docx` - 标准版 (¥1,000,000)
- `output/Budget_Premium_1.5M.docx` - 高端版 (¥1,500,000)

---

## 🔐 保护 Word 文档

### 设置密码保护

```python
from docx import Document
from docx.oxml import parse_xml

doc = Document('output/budget.docx')

# 添加密码保护
protection_xml = '<w:documentProtection w:edit="forms" w:enforcement="1" w:hash="ABCD1234" />'
doc.element.insert(0, parse_xml(protection_xml))

doc.save('output/budget_protected.docx')
```

### 设置只读模式

在 Word 中：
1. 文件 → 信息
2. 保护文档 → 标记为最终版本
3. 保存

---

## 📱 转换为其他格式

### 转换为 PDF

```bash
# 使用 Pandoc
pandoc docs/BUDGET_DETAILED.md -o output/budget.pdf

# 使用 LibreOffice
libreoffice --headless --convert-to pdf output/budget.docx
```

### 转换为 Excel

```bash
# 生成 CSV 然后导入 Excel
python scripts/generate_budget_xlsx.py
```

### 转换为 HTML

```bash
pandoc docs/BUDGET_DETAILED.md -o output/budget.html --self-contained-html
```

---

## ✅ 预算文档清单

- [ ] 下载 Word 文档
- [ ] 打开并检查内容
- [ ] 根据实际情况修改
- [ ] 获取相关部门审批
- [ ] 保存最终版本
- [ ] 归档备查
- [ ] 定期更新

---

## 📞 遇到问题？

### 常见问题

**Q: Word 文档打不开？**
A: 确保安装了 Microsoft Word 或兼容软件（WPS、LibreOffice）

**Q: Pandoc 转换失败？**
A: 检查 Pandoc 是否正确安装：`pandoc --version`

**Q: 表格格式混乱？**
A: 在 Word 中重新调整列宽，或使用脚本生成的版本

**Q: 如何合并多个预算文档？**
A: 使用 python-docx 的 `add_page_break()` 和文件追加功能

---

## 📚 相关资源

- [Pandoc 官方文档](https://pandoc.org/)
- [python-docx 文档](https://python-docx.readthedocs.io/)
- [Markdown 语法](https://www.markdownguide.org/)
- [Word 文档格式规范](https://docs.microsoft.com/en-us/office/open-xml/)

---

**最后更新**: 2026年6月2日  
**版本**: v1.0
