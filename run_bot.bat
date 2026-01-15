@echo off
REM Script de inicio rápido para el bot


REM Asegurar que estamos en el directorio del script
cd /d "%~dp0"

echo Iniciando Linkedini Bot...

REM Ejecución del script principal de Python
python main.py

echo.
echo Presiona Enter para salir...
pause >nul
