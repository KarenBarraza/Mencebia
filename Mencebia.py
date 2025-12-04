#improta archivos necesarios
import pandas as pd
import matplotlib.pyplot as mp
from Archivo import Archivo
from Funciones import Funciones
#se instancia la clase archivo
archivo= Archivo('Buceo_de_la_Concha.csv')
#lee el archivo
archivo.leer()
datos=archivo.datos
#se instancia la clase funciones
funcion=Funciones(datos)
#se crea una nueva columna 
datos["valor_minutos"]=funcion.valorMinutos()

print(datos)
#muestra el valor maximo por minuto
print("El valor maximo por minuto es:",funcion.valorMinutoMax())
