#Importacion de pandas
import pandas as pd
#Creacion del la clase
class MencebiaClass:

    def _init_(self):
        pass

# Ordenar la columna TOTAL de mayor a menor
    def ordenado_total(self,df):
        return df.sort_values('valor_total', ascending=False)

# Agrupar por servicio y sumar valor_total
    def total_por_producto(self,df):
        return df.groupby('tipo_servicio')['valor_total'].sum()

# Agrupar por alias y sumar valor_total
    def total_por_alias(self,df):
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