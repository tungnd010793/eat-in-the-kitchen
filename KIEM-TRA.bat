@echo off
chcp 65001 >nul
title KIEM TRA bang chung
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0..\_cong-cu\kiem-tra.ps1" -DuAn "%~dp0."
echo.
pause
