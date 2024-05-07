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

def get_os_logo():
    """
    Obtiene el logo ASCII del sistema operativo y lo colorea según la distribución de Linux.
    """
    os_name = platform.system()

    if os_name == "Linux":
        dist_info = platform.linux_distribution()
        dist_name = dist_info[0].lower()
        if "debian" in dist_name:
            return f"{Fore.RED}" + """
                _,met$$$$$gg.
                ,g$$$$$$$$$$$$$$$P.
            ,g$$P'            'Y$$.".
            ,$$P'              `$$$.
            ',$$P       ,ggs.     `$$b:
            `d$$'     ,$P\"   .    $$$
            $$P      d$'     ,    $$P
            $$:      $$.   -    ,d$$'
            $$;      Y$b._   _,d$P'
            Y$$.    `. `"Y$$$$P"'
            `$$b      "-.__
            `Y$$
                `Y$$.
                `$$b.
                    `Y$$b.
                        `"Y$b._
            """

       
        elif "ubuntu" in dist_name:
            return f"{Fore.YELLOW}" + """
                    ./oydmMMMMMMmdyo/.
                    :smMMMMMMMMMMMhs+:++yhs:
                `omMMMMMMMMMMMN+`        `odo`
                /NMMMMMMMMMMMMN-            `sN/
            `hMMMMmhhmMMMMMMh               sMh`
            .mMmo-     /yMMMMm`              `MMm.
            mN/       yMMMMMMMd-              MMMm
            oN-        oMMMMMMMMMms+//+o+:    :MMMMo
            m/          +NMMMMMMMMMMMMMMMMm. :NMMMMm
            M`           .NMMMMMMMMMMMMMMMNodMMMMMMM
            M-            sMMMMMMMMMMMMMMMMMMMMMMMMM
            mm`           mMMMMMMMMMNdhhdNMMMMMMMMMm
            oMm/        .dMMMMMMMMh:      :dMMMMMMMo
            mMMNyo/:/sdMMMMMMMMM+          sMMMMMm
            .mMMMMMMMMMMMMMMMMMs           `NMMMm.
            `hMMMMMMMMMMM.oo+.            `MMMh`
                /NMMMMMMMMMo                sMN/
                `omMMMMMMMMy.            :dmo`
                    :smMMMMMMMh+-`   `.:ohs:
                    ./oydmMMMMMMdhyo/.
            """

        elif "mint" in dist_name:
            return f"{Fore.GREEN}" + """
                        ...-:::::-...
                    .-MMMMMMMMMMMMMMM-.
                .-MMMM`..-:::::::-..`MMMM-.
                .:MMMM.:MMMMMMMMMMMMMMM:.MMMM:.
            -MMM-M---MMMMMMMMMMMMMMMMMMM.MMM-
            `:MMM:MM`  :MMMM:....::-...-MMMM:MMM:`
            :MMM:MMM`  :MM:`  ``    ``  `:MMM:MMM:
            .MMM.MMMM`  :MM.  -MM.  .MM-  `MMMM.MMM.
            :MMM:MMMM`  :MM.  -MM-  .MM:  `MMMM-MMM:
            :MMM:MMMM`  :MM.  -MM-  .MM:  `MMMM:MMM:
            :MMM:MMMM`  :MM.  -MM-  .MM:  `MMMM-MMM:
            .MMM.MMMM`  :MM:--:MM:--:MM:  `MMMM.MMM.
            :MMM:MMM-  `-MMMMMMMMMMMM-`  -MMM-MMM:
            :MMM:MMM:`                `:MMM:MMM:
            .MMM.MMMM:--------------:MMMM.MMM.
                '-MMMM.-MMMMMMMMMMMMMMM-.MMMM-'
                '.-MMMM``--:::::--``MMMM-.'
                        '-MMMMMMMMMMMMM-'
                        ``-:::::-``
            """

        elif "fedora" in dist_name:
            return f"{Fore.BLUE}" + """
                        .',;::::;,'.
                    .';:cccccccccccc:;,.
                .;cccccccccccccccccccccc;.
                .:cccccccccccccccccccccccccc:.
            .;ccccccccccccc;.dddl:.;ccccccc;.
            .:ccccccccccccc;OWMKOOXMWd;ccccccc:.
            .:ccccccccccccc;KMMc;cc;xMMc;ccccccc:.
            ,cccccccccccccc;MMM.;cc.;WW:;cccccccc,
            :cccccccccccccc;MMM.;cccccccccccccccc:
            :ccccccc;oxOOOo;MMM0OOk.;cccccccccccc:
            cccccc;0MMKxdd:;MMMkddc.;cccccccccccc;
            ccccc;XM0';cccc;MMM.;cccccccccccccccc'
            ccccc;MMo;ccccc;MMW.;ccccccccccccccc;
            ccccc;0MNc.;ccc.xMMd;ccccccccccccccc;
            cccccc;dNMWXXXWM0:;cccccccccccccc:;
            cccccccc.;odl:.;cccccccccccccc:,.
            :cccccccccccccccccccccccccccc:'.
            .:cccccccccccccccccccccc:;,..
            '::cccccccccccccc::;,.
            """

        else:
            return "Unsupported Linux Distribution"
    
    elif os_name == "Windows 11" or os_name == "Windows 10" or os_name == "Windows 8" or os_name == "Windows":
        return f"{Fore.CYAN}" + """
        ################  ################
        ################  ################
        ################  ################
        ################  ################
        ################  ################
        ################  ################
        ################  ################

        ################  ################
        ################  ################
        ################  ################
        ################  ################
        ################  ################
        ################  ################
        ################  ################
        """
  
    else:
        return "Unsupported OS"

def get_cpu_info():
    """
    Obtiene información sobre la CPU del sistema.
    """
    try:
        cpu_info = {}
        cpu_info['CPU Model'] = platform.processor()
        cpu_info['Number of Cores'] = psutil.cpu_count(logical=False)
        return cpu_info
    except Exception as e:
        print(f"Error getting CPU info: {e}")
        return {}

def get_memory_info():
    """
    Obtiene información sobre la memoria del sistema.
    """
    try:
        memory_info = {}
        mem = psutil.virtual_memory()
        total_memory_gb = round(mem.total / (1024 * 1024 * 1024))  # Convertir a GB y redondear
        available_memory_gb = round(mem.available / (1024 * 1024 * 1024))  # Convertir a GB y redondear
        memory_info['Total Memory'] = f"{total_memory_gb} GB"
        memory_info['Available Memory'] = f"{available_memory_gb} GB"
        return memory_info
    except Exception as e:
        print(f"Error obteniendo información de la memoria: {e}")
        return {}

def get_disk_info():
    """
    Obtiene información sobre los discos del sistema.
    """
    try:
        disk_info = {}
        partitions = psutil.disk_partitions()
        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_info[partition.mountpoint] = {'Size': f"{usage.total / (1024*1024*1024):.2f} GB",
                                                'Used': f"{usage.used / (1024*1024*1024):.2f} GB",
                                                'Available': f"{usage.free / (1024*1024*1024):.2f} GB",
                                                'Usage%': f"{usage.percent}%"}
        return disk_info
    except Exception as e:
        print(f"Error getting disk info: {e}")
        return {}

def display_system_info(system_info):
    """
    Muestra información general sobre el sistema.
    """
    print("System Information:")
    for key, value in system_info.items():
        print(f"{key}: {value}")

def display_cpu_info(cpu_info):
    """
    Muestra información sobre la CPU del sistema.
    """
    print("\nCPU Information:")
    for key, value in cpu_info.items():
        print(f"{key}: {value}")

def display_memory_info(memory_info):
    """
    Muestra información sobre la memoria del sistema.
    """
    print("\nMemory Information:")
    for key, value in memory_info.items():
        print(f"{key}: {value:.2f} GB")

def display_disk_info(disk_info):
    """
    Muestra información sobre los discos del sistema.
    """
    print("\nDisk Information:")
    for mount_point, details in disk_info.items():
        print(f"Mount Point: {mount_point}")
        for key, value in details.items():
            print(f"\t{key}: {value}")

def display_directory_info(directory):
    """
    Muestra información sobre un directorio específico.
    """
    try:
        if os.path.exists(directory):
            print(f"\nDirectory Information for {directory}:")
            directory_info = os.stat(directory)
            print(f"Mode: {directory_info.st_mode}")
            print(f"Size: {directory_info.st_size} bytes")
            print(f"Last Accessed Time: {directory_info.st_atime}")
            print(f"Last Modified Time: {directory_info.st_mtime}")
            print(f"Creation Time: {directory_info.st_ctime}")
        else:
            print(f"The directory '{directory}' does not exist.")
    except Exception as e:
        print(f"Error getting directory info: {e}")

def print_centered(text):
    """
    Imprime el texto centrado en la terminal.

    Args:
        text (str): El texto que se imprimirá centrado.

    Returns:
        None
    """
    try:
        columns = os.get_terminal_size().columns
    except OSError:
        columns = 80  # Valor predeterminado para Windows
    print(text.center(columns))

def print_side_by_side(left_text, right_text):
    """
    Imprime dos textos uno al lado del otro en la terminal.

    Args:
        left_text (str): El texto que se imprimirá en el lado izquierdo.
        right_text (str): El texto que se imprimirá en el lado derecho.

    Returns:
        None
    """
    try:
        columns = os.get_terminal_size().columns
    except OSError:
        columns = 80  # Valor predeterminado para Windows
    left_width = len(left_text)
    padding = max(0, columns - left_width - len(right_text))
    print(left_text + ' ' * padding + right_text)

if __name__ == "__main__":
    os_logo = get_os_logo()
    system_info = {
        'System': platform.system(),
        'Node Name': platform.node(),
        'Release': platform.release(),
        'Version': platform.version(),
        'Machine': platform.machine(),
        'Processor': platform.processor()
    }

    cpu_info = get_cpu_info()  # Esta función la debes definir
    memory_info = get_memory_info()  # Esta función la debes definir
    disk_info = get_disk_info()  # Esta función la debes definir

    # Imprimir el logo del sistema operativo y luego la información del sistema en dos columnas
    print_centered(os_logo)
    for key, value in system_info.items():
        print_side_by_side(f"{key}: {value}", "")

    # Imprimir la información adicional del CPU, memoria y disco en dos columnas
    for info in [cpu_info, memory_info, disk_info]:
        for key, value in info.items():
            print_side_by_side(f"{key}: {value}", "")


