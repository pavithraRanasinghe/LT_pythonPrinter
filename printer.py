# printer.py
import os
import time

def print_pdf_windows(file_path: str):
    if not os.path.exists(file_path):
        print(f"❌ File does not exist: {file_path}")
        return False

    try:
        print(f"🖨️ Printing: {file_path}")
        os.startfile(file_path, "print")  # Windows-only
        time.sleep(2)  # Give it time to send to printer
        return True
    except Exception as e:
        print(f"❌ Error printing {file_path}: {e}")
        return False
