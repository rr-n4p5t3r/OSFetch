# OSFetch

OSFetch es una herramienta que obtiene información del sistema operativo actual, como el nombre, la versión, la arquitectura del hardware, información de la CPU, memoria y disco, y muestra un logotipo ASCII del sistema operativo con colores según la distribución de Linux.

## Descripción

Este proyecto está basado en el proyecto [Neofetch](https://github.com/alexiarstein/neofetch), y proporciona funcionalidades similares pero enfocadas en obtener información específica del sistema operativo actual.

## Funcionalidades

### OSFetch.py

**OSFetch.py** es el script principal que obtiene información del sistema operativo y muestra un logotipo ASCII del mismo. Utiliza bibliotecas como `platform`, `psutil` y `colorama` para recopilar y formatear la información del sistema.

## Estructura del Proyecto OSFetch

### Scripts de Instalación

- **script/**
  - `install_linux.sh`
  - `install_windows.sh`

### Código Fuente

- **src/**
  - **helpers/** 
    - **__pycache__/** 
    - `__init__.py`
    - `SystemInfo.py`
    - `SystemLogo.py`
  - `OSFetch.py`
  - `requirements.txt`

### Documentación

- **doc/**
  - `neofetch`

### Archivos de Licencia

- `LICENSE`

### Archivo README

- `README.md`

### Archivo Actualizaciones

- `Actualizaciones.md`
  
## Instalación

### Linux

Para instalar OSFetch en Linux, sigue estos pasos:

1. Clona el repositorio desde GitHub: git clone https://github.com/rr-n4p5t3r/OSFetch.git
2. Navega al directorio del proyecto: cd OSFetch
3. Instala las dependencias utilizando pip: pip install -r requirements.txt

### Windows

Para instalar OSFetch en Windows, sigue estos pasos:

1. Descarga el código fuente desde GitHub.
2. Navega al directorio del proyecto en tu terminal.
3. Instala las dependencias utilizando pip: pip install -r requirements.txt

## Contribución

Las contribuciones son bienvenidas. Si deseas contribuir al proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Clona tu fork en tu máquina local.
3. Crea una nueva rama para tu contribución (`git checkout -b feature/nueva-funcionalidad`).
4. Realiza tus cambios y haz commits (`git commit -am 'Agrega nueva funcionalidad'`).
5. Haz push a tu rama (`git push origin feature/nueva-funcionalidad`).
6. Abre un pull request en GitHub.

## Licencia

Este proyecto está licenciado bajo la [Licencia Pública General de GNU, versión 3 (GNU GPLv3)](LICENSE).

## Autor

**Ricardo Rosero**  
Email: rrosero2000@gmail.com  
GitHub: [rr-n4p5t3r](https://github.com/rr-n4p5t3r)

## Invítame un café:

<div id="badges">
  <a href="https://www.buymeacoffee.com/elblogden4p5t3r" target="_blank">
    <img src="https://img.shields.io/badge/buymeacoffee-yellow?style=for-the-badge&logo=buymeacoffee&logoColor=white" alt="LinkedIn Badge"/>
  </a>
</div>
