import pandas as pd

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
