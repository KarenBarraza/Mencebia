import pandas as pd
import matplotlib.pyplot as plt
from MencebiaClass import MencebiaClass
from Archivo import Archivo
# Ruta del archivo CSV
instanciacion= Archivo("Buceo_de_la_Concha.csv")
instanciacion.leer()
df=instanciacion.datos
mencebia = MencebiaClass()

while True:
    print("Seleccione una opción:")
    print("1. Mostrar ordenado el total")
    print("2. Mostrar total por producto")
    print("3. Mostrar total por alias")
    print("4. Salir")
    
    opcion = input("Ingrese el número de la opción deseada: ")
    
    mencebia = MencebiaClass()
    
    if opcion == '1':
        print(mencebia.ordenado_total(df))

    elif opcion == '2':
        print(mencebia.total_por_producto(df))

    elif opcion == '3':
        print(mencebia.total_por_alias(df))

    elif opcion == '4':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")