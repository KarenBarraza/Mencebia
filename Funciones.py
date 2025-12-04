import pandas as pd
from Archivo import Archivo
class Funciones:
    def __init__(self):
           pass
           

    def seleccionar_columnas(self, df):
            print("\n--- Selección de columnas ---")

            print("\nColumna 'alias':")
            print(df['alias'])

            print("\nColumnas 'genero_cliente' y 'tipo_servicio':")
            print(df[['genero_cliente', 'tipo_servicio']])


    def seleccionar_filas(self,df):
            print("\n--- Selección de filas ---")
            print(df.iloc[0:5])


    def aplicar_filtros(self, df):
            print("\n--- Aplicación de filtros ---")

            clientes_femeninos = df[df['genero_cliente'] == 'Femenino']
            print("\nClientes Femeninos:\n", clientes_femeninos)

            altos = df[df['valor_total'] > 300000]
            print("\nRegistros con valor_total > 300000:\n", altos)

            print("\nCantidad de clientes femeninos:", len(clientes_femeninos))
            print("Cantidad de registros con valor_total > 300000:", len(altos))

    def valores_nulos(self, df):
           print("--- Manejo de valores nulos ---")
           df.loc[100, "tiempo_minutos"]=None
           print(df.isnull().sum())
           df["tiempo_minutos"]=df["tiempo_minutos"].fillna(1)
           #df["tiempo_minutos"].fillna(1, inplace=True)
           print(df.isnull().sum())
           df["Recalcular_total"] = df["valor_total"] / df["tiempo_minutos"]
           print(df["Recalcular_total"])




    