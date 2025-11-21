import os

def open_app(path):
    try:
        os.startfile(path)
        return "Application opened."
    except Exception as e:
        return f"Error: {e}"
