import pandas as pd
from Archivo import Archivo

def seleccionar_columnas(df):
    print("\n--- Selección de columnas ---")

    print("\nColumna 'alias':")
    print(df['alias'])

    print("\nColumnas 'genero_cliente' y 'tipo_servicio':")
    print(df[['genero_cliente', 'tipo_servicio']])


def seleccionar_filas(df):
    print("\n--- Selección de filas ---")
    print(df.iloc[0:5])


def aplicar_filtros(df):
    print("\n--- Aplicación de filtros ---")

    clientes_femeninos = df[df['genero_cliente'] == 'Femenino']
    print("\nClientes Femeninos:\n", clientes_femeninos)

    altos = df[df['valor_total'] > 300000]
    print("\nRegistros con valor_total > 300000:\n", altos)

    print("\nCantidad de clientes femeninos:", len(clientes_femeninos))
    print("Cantidad de registros con valor_total > 300000:", len(altos))