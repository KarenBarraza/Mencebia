#Importacion de pandas y clases
import pandas as pd
import matplotlib.pyplot as plt
from MencebiaClass import MencebiaClass
from Archivo import Archivo
# Ruta del archivo CSV
instanciacion= Archivo("Buceo_de_la_Concha.csv")
instanciacion.leer()
#Intanciacion del datafream
df=instanciacion.datos
mencebia = MencebiaClass()
#Creacion del bucle del menu
while True:
    print("Seleccione una opción:")
    print("1. Mostrar ordenado el total")
    print("2. Mostrar total por producto")
    print("3. Mostrar total por alias")
    print("4. Salir")
    print("5. Mostrar las primeras filas")
    print("6. Mostrar tipo de datos")
    print("7. Mostrar valor minimo")
    print("8. Mostrar valor maximo")
#Campo donde se ingresa la opcion que desea el usuario
    opcion = input("Ingrese el número de la opción deseada: ")
    
    mencebia = MencebiaClass()
#La opcion uno que nos muestra el orden de mayor a menor
    if opcion == '1':
        print(mencebia.ordenado_total(df))
#La opcion dos que nos muestra el total por porducto
    elif opcion == '2':
        print(mencebia.total_por_producto(df))
#La opcion tres que nos muestra el total por alias
    elif opcion == '3':
        print(mencebia.total_por_alias(df))
#La opcion cuatro que rompre el bucle para cerrar el programa
    elif opcion == '4':
        print("Saliendo del programa.")
        break
#La opcion cinco que nos muestra las primeras cinco filas
    elif opcion =='5' :
        print(mencebia.visualizacion_filas(df))
#La opcion seis que nos muestra el tipo de datos
    elif opcion == '6':
        print(mencebia.tipo_datos(df))
#La opcion siete que nos muestra el valor minimo
    elif opcion == '7' :
        print("El valor minimo es: ",mencebia.valor_minimo(df))
#La opcion ocho que nos muestra el valor maximo
    elif opcion == '8':
        print("El valor maximo es: ",mencebia.valor_maximo(df))