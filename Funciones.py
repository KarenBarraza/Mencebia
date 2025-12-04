import pandas as pd


class Funciones():
    def __init__(self):
       pass

    #se crea una funcion para crear una nueva columna con el valor por minuto    
    def valorMinutos(self,df):
        df=df["valor_total"]/df["tiempo_minutos"]
        return df

    #se crea una funcion para mostrar el valor maximo y minimo por minuto
    def valorMinutoMax(self,df):
        valor=df["valor_minutos"]
        print("el valor mas alto por minuto es",valor.max())
        print("el valor mas bajo por minuto es",valor.min())