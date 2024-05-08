import platform
import psutil
from colorama import Fore, Style
import os

class SystemInfo:
    def __init__(self):
        self.os_name = platform.system()
        self.system_info = {
            'System': platform.system(),
            'Node Name': platform.node(),
            'Release': platform.release(),
            'Version': platform.version(),
            'Machine': platform.machine(),
            'Processor': platform.processor()
        }

    def get_cpu_info(self):
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

    def get_memory_info(self):
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

    def get_disk_info(self):
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

    def display_system_info(self):
        """
        Muestra información general sobre el sistema.
        """
        print("System Information:")
        for key, value in self.system_info.items():
            print(f"{key}: {value}")

    def display_cpu_info(self):
        """
        Muestra información sobre la CPU del sistema.
        """
        print("\nCPU Information:")
        cpu_info = self.get_cpu_info()
        for key, value in cpu_info.items():
            print(f"{key}: {value}")

    def display_memory_info(self):
        """
        Muestra información sobre la memoria del sistema.
        """
        print("\nMemory Information:")
        memory_info = self.get_memory_info()
        for key, value in memory_info.items():
            print(f"{key}: {value:.2f} GB")

    def display_disk_info(self):
        """
        Muestra información sobre los discos del sistema.
        """
        print("\nDisk Information:")
        disk_info = self.get_disk_info()
        for mount_point, details in disk_info.items():
            print(f"Mount Point: {mount_point}")
            for key, value in details.items():
                print(f"\t{key}: {value}")

    def display_directory_info(self, directory):
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

    def print_centered(self, text):
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

    def print_side_by_side(self, left_text, right_text):
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
