import pandas as pd
from Archivo import Archivo

class Funciones:
    def __init__(self):
           pass
    #Funcion que permite seleccionar las columnas referidas
    def seleccionar_columnas(self, df):
            print("\n--- Selección de columnas ---")

            print("\nColumna 'alias':")
            print(df['alias'])

            print("\nColumnas 'genero_cliente' y 'tipo_servicio':")
            print()
            print(df[['genero_cliente', 'tipo_servicio']])

    #funcion que selecciona las filas dentro de un rango, en este caso de 5  
    def seleccionar_filas(self,df):
            print("\n--- Selección de filas ---")
            print(df.iloc[0:5])

    #funcion que permite filtrar los datos segun ls criterios que se le indiquen
    def aplicar_filtros(self, df):
            print("\n--- Aplicación de filtros ---")

            clientes_femeninos = df[df['genero_cliente'] == 'Femenino']
            print("\nClientes Femeninos:\n", clientes_femeninos)

            altos = df[df['valor_total'] > 300000]
            print("\nRegistros con valor_total > 300000:\n", altos)

            print("\nCantidad de clientes femeninos:", len(clientes_femeninos))
            print("Cantidad de registros con valor_total > 300000:", len(altos))
    #funcion que maneja los valores nulos.
    #Simula un valor nulo
    def valores_nulos(self, df):
           print("--- Manejo de valores nulos ---")
           print()
           df.loc[100, "tiempo_minutos"]=None
           print(df.isnull().sum())
           print()
            #Rellena los valores nulos
           print("Rellena los valores nulos")
           print()
           df["tiempo_minutos"]=df["tiempo_minutos"].fillna(1)
           #df["tiempo_minutos"].fillna(1, inplace=True)
           print(df.isnull().sum())
           print()
            #Recalcula la columna 'total' después de corregir los nulos
           print("Recalcula la columna 'total' después de corregir los nulos")
           print()
           df["Recalcular_total"] = df["valor_total"] / df["tiempo_minutos"]
           print(df["Recalcular_total"])
           print()
    
    #se crea una funcion para crear una nueva columna con el valor por minuto    
    def valorMinutos(self,df):
        print()
        df=df["valor_total"]/df["tiempo_minutos"]
        print("Creacion columna Valor_minutos: ")
        print(df)
        
    #se crea una funcion para mostrar el valor maximo y minimo por minuto
    def valorMinutoMax(self,df):
        valor=df["valor_minutos"]
        print("---- Calculo por minutos ----")
        print()
        print("El valor mas alto por minuto es:",valor.max())
        print("El valor mas bajo por minuto es:",valor.min())
    
    # Ordenar la columna TOTAL de mayor a menor
    def ordenado_total(self,df):
        print("Valor total ordenado de forma ascendente:")
        print()
        return df.sort_values('valor_total', ascending=False)

    # Agrupar por servicio y sumar valor_total
    def total_por_producto(self,df):
        print("Valor total por tipo de servicio:")
        print()
        return df.groupby('tipo_servicio')['valor_total'].sum()

    # Agrupar por alias y sumar valor_total
    def total_por_alias(self,df):
        print("Consumo total por Alias:")
        print()
        return df.groupby('alias')['valor_total'].sum()
    #Visualizacion de las primeras cinco filas
    def visualizacion_filas(self,df):
        return (df.head())
    #Visualizacion de el tipo de dato
    def tipo_datos(self,df):
        return (df.info())
    #Visualizacion de el valor minimo en valor_total
    def valor_minimo(self,df):
        return (df["valor_total"].min())
    #Visualizacion de el valor maximo en valor_total
    def valor_maximo(self,df):
        return (df["valor_total"].max())




    
