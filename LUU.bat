@echo off
chcp 65001 >nul
title LUU phien lam viec
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0..\_cong-cu\luu.ps1" -DuAn "%~dp0."
echo.
pause
