@echo off
cd /d %~dp0
streamlit run insightxi/app.py --browser.gatherUsageStats false --server.headless true
