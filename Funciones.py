import pandas as pd


class Funciones():
    def __init__(self,datos):
        self.minutos=datos
        self.ValorTotal=datos
        

    @property
    def minutos(self)->int:
        return self._minutos
    
    @minutos.setter
    def minutos(self,datos):
        self._minutos=datos["tiempo_minutos"]

    @property
    def ValorTotal(self)->int:
        return self._ValorTotal
    
    @ValorTotal.setter
    def ValorTotal(self,datos):
        self._ValorTotal=datos["valor_total"]

    def valorMinutos(self):
        datos=self.ValorTotal/self.minutos
        return datos

    