# converter.py
from dll_loader import preload_gtk_dlls
preload_gtk_dlls()  # must be called before importing weasyprint

from weasyprint import HTML, CSS
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
font_file = os.path.join(base_dir, 'fonts', 'NotoSansSinhala.ttf')

def convert_html_to_pdf(html_path: str, output_path: str) -> bool:
    try:
        HTML(html_path).write_pdf(
            output_path,
            stylesheets=[CSS(string=f'''
                @font-face {{
                    font-family: 'NotoSansSinhala';
                    src: url('file:///{font_file.replace(os.sep, "/")}');
                }}
                body {{
                    font-family: 'NotoSansSinhala', sans-serif;
                }}
            ''')]
        )
        return True
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        return False
