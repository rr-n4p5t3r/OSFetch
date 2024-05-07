#!/bin/bash

# Instalar dependencias
sudo apt-get update
sudo apt-get install python3 python3-pip

# Instalar paquetes Python necesarios
pip3 install psutil colorama

# Directorio de instalación
INSTALL_DIR="/usr/local/bin"

# Copiar OSFetch.py al directorio de instalación
sudo cp OSFetch.py $INSTALL_DIR/OSFetch.py

# Crear enlace simbólico para facilitar la ejecución desde cualquier ubicación
sudo ln -s $INSTALL_DIR/OSFetch.py /usr/bin/OSFetch

echo "OSFetch instalado correctamente. ¡Ejecuta 'OSFetch' para obtener información del sistema!"
