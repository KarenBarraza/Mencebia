#improta archivos necesarios
import pandas as pd
import matplotlib.pyplot as mp
from Archivo import Archivo
from Funciones import Funciones
#se instancia la clase archivo
archivo= Archivo('Buceo_de_la_Concha.csv')
#lee el archivo
archivo.leer()
df=archivo.datos
#se instancia la clase funciones
funcion=Funciones()
#se crea una nueva columna 
df["valor_minutos"]=funcion.valorMinutos(df)

#muestra el valor maximo y minimo por minuto
funcion.valorMinutoMax(df)#agregar al menu 
