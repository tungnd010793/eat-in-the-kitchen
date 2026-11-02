@echo off
chcp 65001 >nul
title CHOT MOC
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0..\_cong-cu\chot-moc.ps1" -DuAn "%~dp0."
echo.
pause
