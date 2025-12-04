#Importacion de la libreria pandas
import pandas as pd

#creacion de la clase archivo
class Archivo:
#se define la ruta
    def __init__(self, ruta):
        self.ruta = ruta
        self._datos = None
#funcion que lee el archivo CSV
    def leer(self):
        try:
            self.datos = pd.read_csv(self.ruta)
            print("Archivo cargado correctamente.")

        except FileNotFoundError:
            print("No existe el archivo en la ruta indicada.")
#Getter que returna datos
    @property
    def datos(self):
        return self._datos
#setter para datos
    @datos.setter
    def datos(self, datos):
        self._datos = datos