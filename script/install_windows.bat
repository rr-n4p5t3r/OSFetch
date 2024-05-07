@echo off

rem Verificar si Python está instalado
python --version
if %errorlevel% neq 0 (
    echo Python no está instalado. Descargue e instale Python desde https://www.python.org/downloads/
    exit /b 1
)

rem Instalar las dependencias necesarias
pip install psutil colorama

rem Directorio de instalación
set INSTALL_DIR="C:\Program Files\OSFetch"

rem Crear directorio de instalación si no existe
if not exist %INSTALL_DIR% mkdir %INSTALL_DIR%

rem Copiar OSFetch.py al directorio de instalación
copy OSFetch.py %INSTALL_DIR%\OSFetch.py

rem Agregar directorio de instalación al PATH
setx /m PATH "%PATH%;%INSTALL_DIR%"

echo OSFetch instalado correctamente. ¡Ejecuta 'OSFetch' para obtener información del sistema!
