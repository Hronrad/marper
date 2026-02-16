import gradio as gr
from cli import convert_markdown 
import tempfile
import traceback
import os

custom_css = """
.fixed-file-box {
    min-height: 160px !important;
    max-height: 240px !important;
    box-sizing: border-box !important;
    overflow: hidden !important;
}
"""

async def generate_ppt(input_mode, file_obj, text_content, theme, level, formats):
    try:
        input_path = ""
        
        if input_mode == "upload":
            if not file_obj:
                return None, "❌ 请先上传 Markdown 文件. Please upload a Markdown file first."
            input_path = file_obj.name
        else:
            if not text_content.strip():
                return None, "❌ 请输入 Markdown 文本内容. Please enter Markdown text."
            fd, temp_path = tempfile.mkstemp(suffix=".md", text=True)
            with os.fdopen(fd, 'w', encoding='utf-8') as f:
                f.write(text_content)
            input_path = temp_path

        output_files = await convert_markdown(
            input_file=input_path, 
            theme=theme, 
            style_class="", 
            heading_split_levels=int(level), 
            output_formats=formats
        )
        if output_files:
            return output_files, "🎉 生成成功！请点击下载。Success! Now you can download."
        else:
            return None, "❌ 生成失败，请检查控制台报错。Error occurred during generation. Please check console for details."
            
    except Exception as e:
        error_detail = traceback.format_exc()
        print(error_detail) 
        return None, f"❌ 发生异常:\n\n{error_detail}"


with gr.Blocks(title="Marper PPT generator", css=custom_css) as demo:
    gr.Markdown("# Marper 可视化控制台 Console")
    gr.Markdown("上传 Markdown 文档或直接粘贴内容，调整参数，一键生成排版完美的 PPTX。 Upload your Markdown file or paste text, tweak settings, and generate perfectly paginated PPTX with one click.")
    
    with gr.Row():
        with gr.Column():
            input_mode = gr.State(value="upload")
            
            with gr.Tabs():
                with gr.Tab("📁 1. 上传 Markdown 文件 (Upload)") as tab_upload:
                    file_in = gr.File(label="文件 (.md)", file_types=[".md"], height=240)
                with gr.Tab("✍️ 1. 直接输入内容 (Type Content)") as tab_text:
                    text_in = gr.Textbox(label="粘贴或输入 Markdown 代码", lines=10)
            
            tab_upload.select(lambda: "upload", inputs=None, outputs=input_mode)
            tab_text.select(lambda: "text", inputs=None, outputs=input_mode)

            theme_in = gr.Dropdown(
                choices=["default", "gaia", "uncover", "academic", "beam", "rose-pine-dawn", "rose-pine-moon", "rose-pine-dawn-modern"], 
                value="default", 
                label="2. 选择主题皮肤 Choose Theme")
            with gr.Accordion("💡 点击查看主题说明 (Theme Details)", open=False):
                gr.Markdown("""
- **default**: 小字体，最佳兼容。Small font, clean black-on-white, best compatibility.
- **gaia**: 中字体，暖色调低对比。Medium font, warm tone, low contrast. Good for humanities, art/design, eco/lifestyle topics.
- **uncover**: 大字体，居中排版高对比。Large font, minimalist, high contrast. Good for product launches, TED-style talks.
                            
## Community Themes
(社区主题，请确保同时解压 themes 文件夹和 Marper 程序到同一目录下. Make sure to extract both the themes folder and Marper program to the same directory.)
- **academic**:  中字体，右对齐。Medium font with red titles. Note: right-aligned; use only when needed. Author: kaisugi.
- **beam**: 小字体，Beamer 风格。Small font, Beamer-like. Good for academic content. Author: rnd195.
- **rose-pine-dawn**: 小字体，浅色背景。Small font, light background, gentle style. Author: RAINBOWFLESH.
- **rose-pine-moon**: 小字体，深色背景。Small font, dark background, elegant for dark themes. Author: RAINBOWFLESH.
- **rose-pine-dawn-modern**: 中字体，卡片风格标题。Medium font, adds a modern card-style title on top of rose-pine-dawn. Author: 史诗生物.
            """)
            level_in = gr.Slider(minimum=1, maximum=6, value=2, step=1, label="3. 触发分页的最高标题层级 Heading Level to Trigger Pagination")
            
        with gr.Column():

            format_in = gr.CheckboxGroup(choices=["pptx", "pdf", "html", "md"], value=["pptx", "pdf"], label="4. 输出格式 Output Formats")
            submit_btn = gr.Button("⚡ 开始生成 PPT ", variant="primary")
            output_msg = gr.Textbox(label="运行状态 Status", interactive=False, lines=5)
            file_out = gr.File(label="5. 下载生成的演示文稿 Download Generated Presentation", interactive=False, height=200, elem_classes="fixed-file-box")

    submit_btn.click(
        fn=generate_ppt,
        inputs=[input_mode, file_in, text_in, theme_in, level_in, format_in],
        outputs=[file_out, output_msg]
    )

if __name__ == "__main__":
    demo.launch(inbrowser=True, server_port=9080, prevent_thread_lock=False, theme=gr.themes.Soft())