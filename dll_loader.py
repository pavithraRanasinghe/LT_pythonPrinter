# dll_loader.py
import os
import ctypes

def preload_gtk_dlls():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    gtk_bin_path = os.path.join(base_dir, 'gtk', 'bin')

    # Required DLLs for WeasyPrint on Windows
    required_dlls = [
        "libgobject-2.0-0.dll",
        "libglib-2.0-0.dll",
        "libffi-7.dll",
        "libpango-1.0-0.dll",
        "libcairo-2.dll",
        "libfontconfig-1.dll",
        "libfreetype-6.dll",
    ]

    for dll in required_dlls:
        dll_path = os.path.join(gtk_bin_path, dll)
        if os.path.exists(dll_path):
            try:
                ctypes.CDLL(dll_path)
            except OSError as e:
                print(f"❌ Failed to load {dll}: {e}")
        else:
            print(f"⚠️ DLL not found: {dll_path}")

    # Add GTK bin to PATH
    os.environ["PATH"] = gtk_bin_path + os.pathsep + os.environ["PATH"]
