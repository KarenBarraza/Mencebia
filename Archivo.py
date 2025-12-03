import pandas as pd

class Archivo:
    def __init__(self, ruta):
        self.ruta = ruta
        self._datos = None

    def leer(self):
        try:
            self.datos = pd.read_csv(self.ruta)
            print("Archivo cargado correctamente.")

        except FileNotFoundError:
            print("No existe el archivo en la ruta indicada.")

    @property
    def datos(self):
        return self._datos

    @datos.setter
    def datos(self, datos):
        self._datos = datos