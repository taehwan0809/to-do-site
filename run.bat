@echo off
cd /d %~dp0
call C:\Users\hongk\OneDrive\Desktop\fast-test.venv\Scripts\activate
uvicorn main:app --reload
pause
