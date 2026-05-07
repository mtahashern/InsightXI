@echo off
title InsightXI Official Software Builder
echo Preparing to build InsightXI Elite Tactical Suite...
echo Installing required packaging tools...
pip install pyinstaller streamlit fpdf
echo.
echo Building Official InsightXI.exe...
echo (This may take a minute to bundle the AI engine)
pyinstaller --onefile --noconsole --name "InsightXI" --collect-all streamlit --hidden-import streamlit.web.cli --add-data "insightxi;insightxi" main.py
echo.
echo SUCCESS! Your official software is now in the 'dist' folder.
echo You can move 'InsightXI.exe' to your Desktop.
pause
