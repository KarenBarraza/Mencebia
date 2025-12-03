import pandas as pd

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