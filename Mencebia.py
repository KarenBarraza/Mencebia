import pandas as pd
import matplotlib.pyplot as mp
from Archivo import Archivo
from Dashboard import Dashboard


archivo= Archivo('Buceo_de_la_Concha.csv')
archivo.leer()
df=archivo.datos
f=Dashboard()

menuActivo=True
while menuActivo:
    print("6. Mini Dashboard")

    opcion=input("Seleccione una opcion: ")

    if opcion == "6":
        print(f.crear_dashboard(df))

