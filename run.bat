@echo off
echo Starting Python Calculator Application...
cd /d "%~dp0"

:: Wait for a second before opening the browser to ensure the server starts
start "" http://127.0.0.1:5001

:: Run the Flask server
python app.py
pause
