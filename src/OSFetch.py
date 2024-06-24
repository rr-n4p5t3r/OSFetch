"""
Proyecto: OSFetch
Autor: Ricardo Rosero
Email: rrosero2000@gmail.com
Nick: n4p5t3r
GitHub: https://github.com/rr-n4p5t3r

Descripción:
Este programa obtiene información del sistema operativo actual, como el nombre, la versión, la arquitectura del hardware, información de la CPU, memoria y disco, y muestra un logotipo ASCII del sistema operativo con colores según la distribución de Linux.

Requisitos:
- Se requiere la instalación de las bibliotecas externas 'psutil', 'colorama' y 'distro'. Estas se pueden instalar utilizando pip:
  pip install psutil colorama distro
"""

import platform
import psutil
import os
import distro
import warnings
from colorama import init, Fore, Style

from helpers.SystemInfo import SystemInfo
from helpers.SystemLogo import SystemLogo

# Inicializar colorama para Windows
init()

def print_colored(text, color=Fore.WHITE):
    """
    Función para imprimir texto en color.
    """
    print(color + text + Style.RESET_ALL)

if __name__ == "__main__":
    # Suprimir las advertencias de deprecación de distro
    warnings.filterwarnings('ignore', category=DeprecationWarning)

    # Crear una instancia de la clase SystemInfo
    system_info_instance = SystemInfo()
    os_logo = SystemLogo.get_os_logo()

    # Utiliza distro para obtener información de la distribución Linux
    dist_name = distro.name()
    dist_version = distro.version()
    dist_id = distro.id()

    system_info = {
        'System': platform.system(),
        'Node Name': platform.node(),
        'Release': platform.release(),
        'Version': platform.version(),
        'Machine': platform.machine(),
        'Processor': platform.processor(),
        'Distribution': f"{dist_name} {dist_version} ({dist_id})"
    }

    # Obtener la información de la CPU, memoria y disco de la instancia de SystemInfo
    cpu_info = system_info_instance.get_cpu_info()
    memory_info = system_info_instance.get_memory_info()
    disk_info = system_info_instance.get_disk_info()

    # Imprimir el logo del sistema operativo y luego la información del sistema en colores
    print_colored(os_logo)
    for key, value in system_info.items():
        print_colored(f"{key}: {value}")

    # Imprimir la información adicional del CPU, memoria y disco en colores
    for info in [cpu_info, memory_info, disk_info]:
        for key, value in info.items():
            print_colored(f"{key}: {value}")

    # Restaurar el color por defecto al finalizar
    print(Style.RESET_ALL)
