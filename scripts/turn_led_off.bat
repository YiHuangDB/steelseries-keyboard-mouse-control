@echo off
setlocal
cd /d "%~dp0\.."
title Turning Off Keyboard and Mouse LEDs
echo Turning off RGB illumination...
python main.py --off
timeout /t 2 >nul
