import pandas as pd
import matplotlib.pyplot as mp

#Clase para leer el archivo
class Archivo:
    def __init__ (self,Buceo_de_la_Concha):
        self.Buceo_de_la_Concha=Buceo_de_la_Concha

    #Funcion para leer el archivo
    def leer(self):
        try:
            self.datos=pd.read_csv(self.Buceo_de_la_Concha)
        except FileNotFoundError:
            print("No existe")
    #Getter     
    @property
    def datos(self):
        return self._datos
    #Setter
    @datos.setter
    def datos(self,datos):
        self._datos=datos

    
    