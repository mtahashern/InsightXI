import os
import sys
import streamlit.web.cli as stcli
import streamlit

# Elite Fix: Force-inject version metadata to bypass PackageNotFoundError
if not hasattr(streamlit, "__version__"):
    streamlit.__version__ = "1.25.0"

def resolve_path(path):
    if getattr(sys, 'frozen', False):
        # Running as EXE
        base_path = sys._MEIPASS
    else:
        # Running as Script
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, path)

if __name__ == "__main__":
    app_path = resolve_path(os.path.join("insightxi", "app.py"))
    
    # Configure Streamlit for Standalone EXE operation
    sys.argv = [
        "streamlit",
        "run",
        app_path,
        "--global.developmentMode=false",
        "--browser.gatherUsageStats=false",
        "--server.headless=true",
        "--server.port=8501"
    ]
    sys.exit(stcli.main())
