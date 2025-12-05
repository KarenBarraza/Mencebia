import pandas as pd
import matplotlib.pyplot as plt
from Archivo import Archivo
from Funciones import Funciones
from Dashboard import Dashboard

#se instancia la clase archivo
archivo= Archivo('Buceo_de_la_Concha.csv')
#lee el archivo
archivo.leer()
df=archivo.datos
f=Dashboard()
#se instancia la clase funciones
funcion=Funciones()

#se crea una nueva columna 
df["valor_minutos"]=funcion.valorMinutos(df)

#Menu interactivo para el cliente
menuActivo=True
while menuActivo:
    print("------- MENU MENCEBIA -------")
    print("1. Exploración inicial del conjunto de datos")
    print("2. Selección de columnas, filas y aplicación de filtros")
    print("3. Ordenar y agrupar información")
    print("4. Creación de una nueva columna 'total'")
    print("5. Manejo de valores nulos")
    print("6. Mostrar cuartiles")
    print("7. Mini dashboard")
    print("8. Salir")

    #Se le solicita al cliente que seleccione una opcion 
    opcion=input("Seleccione una opcion: ")
    
    if opcion == '1':
        #Se visualizan las 5 primeras filas
        print("-------- Primeras Filas --------")
        print(funcion.visualizacion_filas(df))
        #Se visualizan los tipos de datos de la base de datos
        print("-------- Tipo de Datos ---------")
        print(funcion.tipo_datos(df))
        #Muestra el valor minimo y maximo
        print("----------------------------------------------")
        print("El valor minimo es: ",funcion.valor_minimo(df))
        print("El valor maximo es: ",funcion.valor_maximo(df))
    elif opcion == '2':
        #Esta funcin muestra datos filtrados segun criterios especificos
        funcion.aplicar_filtros(df)
        print("----------------------------------------------")
        #Muestra las filas referidas
        funcion.seleccionar_filas(df)
    elif opcion == '3':
        #Ordena el valor total de forma ascendente
        print(funcion.ordenado_total(df))
        print("----------------------------------------------")
        #Muestra el valor total por tipo de servicio
        print(funcion.total_por_producto(df))
        print("----------------------------------------------")
        #Muestra el valor total por alias
        print(funcion.total_por_alias(df))
    elif opcion =='4' :
        #Crea una columna de valor por minutos
        funcion.valorMinutos(df)
        #Selecciona las columnas requeridas
        funcion.seleccionar_columnas(df)
        #Muestra el valor maximo por minuto
        funcion.valorMinutoMax(df) 
        print("----------------------------------------------")
    elif opcion == '5':
        #Realiza todo el manejo de valores nulos
        funcion.valores_nulos(df)
    elif opcion == '6':
        #Muestra los cuartiles de 25, 50 y  75%
        print(f.imprimir_cuartiles(df))
    elif opcion == '7':
        #Muestra las graficas realizadas
        print(f.crear_dashboard(df))
    elif opcion == '8':
        #Sale del programa
        print("Saliendo del programa.")
        break

