
# Marp-Autosplitter

**Marp-Autosplitter** 是一个快速、智能的命令行工具，能将任意 Markdown 文档完美转换为排版精美、高度精准的 PPTX 和 PDF 演示文稿。它通过自动切分内容并修复跨页结构，再利用 Marp 转为适合展示的 PPTX 和 PDF 演示文稿。程序确保每一页都美观且信息完整，无论是文本、表格还是 LaTeX 公式，都能得到完美呈现。

## 核心特性
* **零依赖即开即用**：无需安装 Python、Node.js 或任何繁琐环境，下载双击即可运行。
* **物理级精准防溢出**：告别字符估算，真实渲染高度测量，100% 杜绝内容越界。
* **语义感知分页**：支持根据指定的标题层级（如 H1、H2）自动智能断页。
* **细胞级结构保护**：跨页时自动修补 Markdown 表格（补全表头）与列表结构，确保 LaTeX 公式完美渲染。
* **高度可定制**：内置多款主题，并支持挂载本地 `themes` 文件夹拓展自定义 CSS 皮肤。
* **跨平台免配置**：自动探测系统内置的 Chrome/Edge 浏览器，支持 Windows, macOS, Linux。
* **可视化操作界面**：内置现代化 Web UI，支持文件拖拽、参数可视化调节，一键输出结果。

## 快速使用
前往本仓库的 **[Releases page](https://github.com/Hronrad/marp-autosplitter/releases/)** 页面。

根据你的操作系统下载对应的可执行文件（如 Marp-Web-Client-Windows.exe）。

双击运行该程序。一个现代化的 Web 控制台将自动在你的浏览器中打开，上传 Markdown 文件即可一键生成排版完美的 PPTX 和 PDF！

## 开发者模式

请确保你的电脑已安装 Python 3.10+ 和 Node.js。

1. **克隆并进入项目**
```bash
git clone <your-repo-url>
cd marp-autosplitter
```

2. **安装核心依赖**
```bash
npm install
pip install -r requirements.txt
```


*(注：程序会自动调用本机的 Chrome/Edge，无需额外执行 playwright install)*

## 快速开始

基础转换（默认输出 PPTX 和 PDF，使用 `default` 主题）：

```bash
python cli.py report.md
```

带参数的进阶转换（使用 `gaia` 主题，文档中前 3 级标题都触发分页，输出 PPTX 和 HTML）：

```bash
python cli.py report.md -t gaia -l 3 -f pptx html

```

### ⚙️ 命令参数参考

| 参数 | 简写 | 说明 | 默认值 |
| --- | --- | --- | --- |
| `input` | 无 | **[必填]** 要转换的 Markdown 文件路径 | - |
| `--theme` | `-t` | 主题名称（支持 `default`, `gaia`, `uncover` 及 `themes/` 下的自定义主题） | `default` |
| `--level` | `-l` | 触发自动分页的 “前 $n$ 个实际存在的最高标题层级”。例如设为 2 时，若文档仅含 H1 和 H3，则 H1 与 H3 均会触发分页起新页。 | `2` |
| `--class_style` | `-c` | 附加的全局 CSS 类（如 `lead` 居中, `invert` 反色暗黑模式） | 空 |
| `--format` | `-f` | 指定输出格式，多个格式用空格隔开（可选: `pptx`, `pdf`, `html`） | `pptx pdf` |

## 产物输出

生成的中间件 `.md` 和最终的 PPT 文件均会自动保存在项目根目录下的 `output_slides` 文件夹中。


## 反馈与支持
使用中如遇问题或有任何建议，欢迎提交 Issue 或 Pull Request！
如果觉得本项目对你有帮助，别忘了点个 Star 支持一下！✨

---

# Marp-Autosplitter (English)

**Marp-Autosplitter** is a blazing-fast, intelligent, and standalone tool designed to flawlessly convert any Markdown document into beautifully formatted, highly precise PPTX and PDF presentations. Powered by a physical-level measurement engine, it automatically paginates lengthy content and smartly repairs cross-page structures. Leveraging Marp under the hood, it ensures every slide is rendered perfectly.

## ✨ Core Features

* **Zero Dependencies**: No Python, no Node.js required. Just download and run.
* **Physical-Level Overflow Prevention**: Utilizes real headless browser DOM height measurements, guaranteeing zero content overflow or text truncation.
* **Semantic Pagination**: Intelligently breaks pages based on your document's heading structure, maintaining logical flow.
* **Cell-Level Structure Protection**: Automatically repairs Markdown tables (injecting missing headers) and nested lists across page breaks.
* **Modern Web UI**: Comes with a built-in, user-friendly web interface. Just drag and drop your files and click generate.

## 🚀 Quick Start (For End Users)

No coding experience required. Get your presentation in 3 simple steps:

1. Go to the **[Releases page](https://github.com/Hronrad/marp-autosplitter/releases/)** of this repository.
2. Download the standalone executable for your operating system (e.g., `Marp-Web-Client-Windows.exe`).
3. **Double-click to run**. A modern Web UI will automatically open in your default browser. Upload your `.md` file, tweak the settings, and instantly download your PPTX/PDF!

---

## 💻 Developer Mode (For Source Code & CLI usage)

If you want to modify the core engine or use the Command Line Interface (CLI) for batch processing, you can set up the development environment:

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd marp-autosplitter

# 2. Install dev dependencies (Requires Python 3.10+ and Node.js)
npm install @marp-team/marp-cli
pip install -r requirements.txt

# 3. Run via CLI
python cli.py report.md -t gaia -l 3 -f pptx html

```

### ⚙️ CLI Arguments Reference

| Argument | Short | Description | Default |
| --- | --- | --- | --- |
| `input` | None | **[Required]** Path to the target Markdown file. | - |
| `--theme` | `-t` | Theme name (supports `default`, `gaia`, `uncover`, and custom CSS). | `default` |
| `--level` | `-l` | The **top n actual heading levels** that trigger pagination. For example, if set to 2, and your doc only has H1 and H3 tags, both will trigger a new slide. | `2` |
| `--class_style` | `-c` | Additional global CSS classes (e.g., `lead` for centered, `invert` for dark mode). | empty |
| `--format` | `-f` | Desired output formats, separated by spaces (Options: `pptx`, `pdf`, `html`). | `pptx pdf` |

## 💬 Feedback & Support

If you encounter any issues or have feature suggestions, feel free to open an Issue or submit a Pull Request!
If this project helped improve your workflow, please consider leaving a ⭐️ Star!