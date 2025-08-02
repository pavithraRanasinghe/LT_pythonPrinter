from dll_loader import preload_gtk_dlls
preload_gtk_dlls()

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from converter import convert_html_to_pdf
from printer import print_pdf_windows
import os

app = FastAPI()

output_dir = r"C:\POP\print-job\output_file"
os.makedirs(output_dir, exist_ok=True)

class HtmlPathsRequest(BaseModel):
    html_paths: List[str]

@app.post("/generate-pdf")
def generate_pdf(request: HtmlPathsRequest):
    results = []
    for html_path in request.html_paths:
        if not os.path.isfile(html_path):
            results.append({"html": html_path, "success": False, "error": "File not found"})
            continue

        filename = os.path.basename(html_path).replace(".html", ".pdf")
        output_pdf = os.path.join(output_dir, filename)

        success = convert_html_to_pdf(html_path, output_pdf)

        printed = False
        if success:
            printed = print_pdf_windows(output_pdf)


        results.append({
            "html": html_path,
            "output": output_pdf if success else None,
            "success": success,
            "printed": printed
        })

    return {"results": results}
