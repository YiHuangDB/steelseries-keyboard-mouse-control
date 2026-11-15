@echo off
setlocal
cd /d "%~dp0\.."
title Restoring Keyboard and Mouse LEDs
echo Restoring default RGB illumination...
python main.py --on
timeout /t 2 >nul
