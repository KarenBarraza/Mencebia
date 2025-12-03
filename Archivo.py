import pandas as pd
import matplotlib.pyplot as mp

class Archivo:
    def __init__ (self,Buceo_de_la_Concha):
        self.Buceo_de_la_Concha=Buceo_de_la_Concha

    def leer(self):
        try:
            self.datos=pd.read_csv(self.Buceo_de_la_Concha)
        except FileNotFoundError:
            print("No existe")
            
    @property
    def datos(self):
        return self._datos
    
    @datos.setter
    def datos(self,datos):
        self._datos=datos

    
    