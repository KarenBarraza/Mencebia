import pandas as pd
import matplotlib.pyplot as mp
from Archivo import Archivo
from Dashboard import Dashboard

#Instanciacion 
archivo= Archivo('Buceo_de_la_Concha.csv')
archivo.leer()
df=archivo.datos
f=Dashboard()

#Menu interactivo para el cliente
menuActivo=True
while menuActivo:
    print("6. Mini Dashboard")
    print("7. Cuartiles")
    #print("8. Grafica cuartiles")

    opcion=input("Seleccione una opcion: ")

    if opcion == "6":
        print(f.crear_dashboard(df))
    elif opcion == "7":
        print(f.imprimir_cuartiles(df))
    # elif opcion == "8":
    #     print(f.crear_graficas_cuartiles(df))

