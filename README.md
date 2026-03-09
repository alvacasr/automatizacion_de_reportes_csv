# Automatización de reportes csv

Herramienta de automatización en Python que procesa múltiples archivos CSV y genera reportes consolidados de ventas automáticamente.

## Descripción

Este proyecto implementa un pequeño pipeline de datos que automatiza el procesamiento de archivos CSV de ventas. El sistema carga todos los archivos CSV de una carpeta, los combina en un solo dataset y genera un reporte resumen con estadísticas de ventas por producto.

El objetivo del proyecto es demostrar cómo automatizar tareas repetitivas de procesamiento de datos utilizando Python.

## Características

- Procesamiento automático de múltiples archivos CSV
- Consolidación de datos en un solo dataset
- Generación de reportes de ventas
- Pipeline reproducible de procesamiento de datos
- Código modular y fácil de extender

## Tecnologías utilizadas

- Python
- Pandas

## Estructura del proyecto

csv-report-automation  
│  
├── process_files.py        # Carga y combina archivos CSV  
├── generate_summary.py     # Genera el reporte de ventas  
├── run_pipeline.py         # Ejecuta todo el pipeline  
│  
├── input_data/             # Archivos CSV de entrada  
│   ├── sales_january.csv  
│   └── sales_february.csv  
│  
├── output/                 # Resultados generados  
│   ├── merged_data.csv  
│   └── summary_report.csv  
│  
└── README.md  

## Flujo del pipeline

El sistema sigue tres pasos principales:

1. **Procesamiento de archivos**
   - Se detectan automáticamente todos los archivos CSV en la carpeta `input_data`.
   - Los datos se cargan y se combinan en un solo dataset.

2. **Consolidación de datos**
   - Se genera un archivo con todos los registros combinados.

3. **Generación de reporte**
   - Se calculan métricas de ventas por producto.
   - Se genera un reporte resumen.

Flujo del sistema:

process_files.py → generate_summary.py → summary_report.csv

## Instalación

Clonar el repositorio:

git clone https://github.com/tu-usuario/csv-report-automation.git  
cd csv-report-automation

Instalar dependencias:

pip install -r requirements.txt

## Uso

Ejecutar todo el pipeline automáticamente:

python run_pipeline.py

O ejecutar los pasos manualmente:

Procesar archivos:

python process_files.py

Generar reporte:

python generate_summary.py

## Resultados

El proyecto genera automáticamente:

- **merged_data.csv**  
  Dataset consolidado con todos los registros de ventas.

- **summary_report.csv**  
  Reporte resumen con estadísticas de ventas por producto.

## Posibles mejoras

Algunas mejoras futuras podrían incluir:

- generación de gráficos automáticos
- exportación de reportes en Excel
- integración con bases de datos
- ejecución automática mediante tareas programadas
- dashboard interactivo de ventas

## Autor

Ramón Alvarado
