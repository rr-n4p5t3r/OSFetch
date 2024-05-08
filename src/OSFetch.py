"""
Proyecto: OSFetch
Autor: Ricardo Rosero
Email: rrosero2000@gmail.com
Nick: n4p5t3r
GitHub: https://github.com/rr-n4p5t3r

Descripción:
Este programa obtiene información del sistema operativo actual, como el nombre, la versión, la arquitectura del hardware, información de la CPU, memoria y disco, y muestra un logotipo ASCII del sistema operativo con colores según la distribución de Linux.

Requisitos:
- Se requiere la instalación de las bibliotecas externas 'psutil' y 'colorama'. Estas se pueden instalar utilizando pip:
  pip install psutil colorama
"""

import platform
import psutil
from colorama import Fore, Style
import os
from helpers.SystemInfo import SystemInfo
from helpers.SystemLogo import SystemLogo

if __name__ == "__main__":
    # Crear una instancia de la clase SystemInfo
    system_info_instance = SystemInfo()
    os_logo = SystemLogo.get_os_logo()
    
    system_info = {
        'System': platform.system(),
        'Node Name': platform.node(),
        'Release': platform.release(),
        'Version': platform.version(),
        'Machine': platform.machine(),
        'Processor': platform.processor()
    }

    # Obtener la información de la CPU, memoria y disco de la instancia de SystemInfo
    cpu_info = system_info_instance.get_cpu_info()
    memory_info = system_info_instance.get_memory_info()
    disk_info = system_info_instance.get_disk_info()

    # Imprimir el logo del sistema operativo y luego la información del sistema en dos columnas
    system_info_instance.print_centered(os_logo)
    for key, value in system_info.items():
        system_info_instance.print_side_by_side(f"{key}: {value}", "")

    # Imprimir la información adicional del CPU, memoria y disco en dos columnas
    for info in [cpu_info, memory_info, disk_info]:
        for key, value in info.items():
            system_info_instance.print_side_by_side(f"{key}: {value}", "")
