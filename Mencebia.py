import pandas as pd
import matplotlib.pyplot as mp
from Archivo import Archivo

archivo= Archivo('Buceo_de_la_Concha.csv')
archivo.leer()
print(archivo.datos)
