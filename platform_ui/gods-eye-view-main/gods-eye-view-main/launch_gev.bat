@echo off
TITLE God's Eye View 3D Workstation - Cesium & Vite Engine
COLOR 0B
echo ===============================================================================
echo     GOD'S EYE VIEW 3D WORKSTATION - CESIUM / VITE INTELLIGENCE ENGINE
echo                     Author: Bilawal Sidhu / EconAgent Platform
echo ===============================================================================
echo.

cd /d "%~dp0"

if not exist ".env" (
    echo [*] Creating local .env from .env.example...
    copy ".env.example" ".env" >nul
)

if not exist "node_modules" (
    echo [*] Installing Node.js packages (Cesium, Vue 3, Pinia)...
    call npm.cmd install --ignore-scripts
)

echo.
echo [*] Starting God's Eye View local server on http://localhost:4173 ...
echo [*] BMAP and EconAgent Platform will automatically embed this 3D stream!
echo.

start "" "http://localhost:4173"
call npm.cmd run dev

pause
