@echo off
chcp 65001 >nul
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0nangman_interior_정리_발행예약폴더.ps1"
