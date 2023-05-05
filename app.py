import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Carga el archivo Excel donde la información de las ventas está en la hoja 'Salidas'
def procesar_archivo_excel(archivo):
    ventas = pd.read_excel(archivo, sheet_name='Salidas', skiprows=4, usecols=range(10))

    ventas.columns = [
        'id',
        'pago',
        'mp',
        'promo',
        'bebida',
        'precio',
        'cantidad',
        'importe',
        'total',
        'observaciones'
    ]

    ventas = ventas[ventas['bebida'].notna()]
    return ventas

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


# Ventas por Bebida
ventas_totales_por_bebida = ventas_totales.groupby('bebida').agg({'importe': 'sum'})
print(ventas_totales_por_bebida)


# Ventas tomadas por richard
ventas_richard = ventas_totales[ventas_totales['observaciones'].str.contains('richard', case=False, na=False)]
suma_importes_richard = ventas_richard['importe'].sum()

print("La suma total de los importes para las ventas con la palabra 'richard' en las observaciones es:", suma_importes_richard)


ventas_richard_congelada = ventas_totales[ventas_totales['observaciones'].str.contains('richard|congelada', case=False, na=False, regex=True)]
suma_importes_richard_congelada = ventas_richard_congelada['importe'].sum()

print("La suma total de los importes para las ventas con la palabra 'richard' o 'congelada' en las observaciones es:", suma_importes_richard_congelada)

ventas_richard = ventas_totales[ventas_totales['observaciones'].str.contains('richard', case=False, na=False)]

print("Ventas con la palabra 'richard' en las observaciones:")
print(ventas_richard)


# Ventas por Bebida
ventas_totales_por_bebida = ventas_totales.groupby('bebida').agg({'importe': 'sum'})
print("Ventas totales por bebida:", ventas_totales_por_bebida)

# Gráfico de barras
plt.bar(ventas_totales_por_bebida.index, ventas_totales_por_bebida['importe'])
plt.title('Ventas por Bebida')
plt.xlabel('Bebida')
plt.ylabel('Importe')
plt.xticks(rotation=45)
plt.show()


# Gráfico de pastel
plt.pie(ventas_totales_por_bebida['importe'], labels=ventas_totales_por_bebida.index, autopct='%1.1f%%')
plt.title('Ventas por Bebida')
plt.show()



ventas_richard = ventas_totales[ventas_totales['observaciones'].str.contains('richard', case=False, na=False)]
ventas_richard_por_bebida = ventas_richard.groupby('bebida').agg({'importe': 'sum'})

# Gráfico de barras
plt.bar(ventas_richard_por_bebida.index, ventas_richard_por_bebida['importe'])
plt.title("Ventas con la palabra 'richard' en las observaciones")
plt.xlabel('Bebida')
plt.ylabel('Importe')
plt.xticks(rotation=45)
plt.show()


"""# Si es necesario, puedes cargar también la información de precios y stock de las bebidas
# desde otra pestaña del archivo Excel
bebidas = pd.read_excel('ArchivosExcel/20230428.xlsx', sheet_name='Bebidas', usecols=range(1,10))
print(bebidas)


 A partir de aquí, puedes comenzar a realizar el análisis de datos utilizando pandas.
# Por ejemplo, podrías calcular el total de ventas por día, agrupar las ventas por tipo de bebida, etc.
# Aquí hay algunos ejemplos:

# Calcular el total de ventas por día
ventas_por_dia = ventas.groupby(ventas.index.date).agg({'total': 'sum'})

# Calcular la cantidad de bebidas vendidas por tipo
ventas_por_tipo = ventas.groupby('bebida').agg({'cantidad': 'sum'})

# Calcular el total de ventas por tipo de bebida
ventas_totales_por_tipo = ventas.groupby('bebida').agg({'total': 'sum'})

# Calcular la cantidad de ventas por promoción
ventas_por_promo = ventas.groupby('promo').agg({'cantidad': 'sum'})

# Puedes continuar con el análisis según tus necesidades. """
