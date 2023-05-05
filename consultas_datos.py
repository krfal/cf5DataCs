import matplotlib.pyplot as plt

def ventas_por_bebida(df):
    ventas_totales_por_bebida = df.groupby('bebida').agg({'importe': 'sum'})
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
