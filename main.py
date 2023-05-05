import os
import pandas as pd
from datetime import datetime
from lectura_datos import procesar_archivo_excel
from consultas_datos import *

ruta_carpeta = 'ArchivosExcel/'
archivos_excel = [f for f in os.listdir(ruta_carpeta) if f.endswith('.xlsx') and not f.startswith('~$')]

ventas_totales = pd.DataFrame(columns=['fecha', 'id', 'pago', 'mp', 'promo', 'bebida', 'precio', 'cantidad', 'importe', 'total', 'observaciones'])

for archivo in archivos_excel:
    if archivo.endswith('.xlsx'):
        # Extrae la fecha del nombre del archivo
        fecha_str = archivo[:-5]
        fecha = datetime.strptime(fecha_str, '%Y%m%d')

        # Carga el archivo Excel y renombra las columnas
        archivo_path = os.path.join(ruta_carpeta, archivo)
        ventas = procesar_archivo_excel(archivo_path)

        # Agrega la columna 'fecha' al DataFrame de ventas
        ventas.insert(0, 'fecha', fecha)

        # Combina el DataFrame de ventas con el DataFrame de ventas_totales
        ventas_totales = pd.concat([ventas_totales, ventas], ignore_index=True)

# Imprimimos todo el DataFrame
print(ventas_totales)


ventas_por_bebida(ventas_totales)