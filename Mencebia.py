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
    print("1. Mostrar ordenado el total")
    print("2. Mostrar total por servicio")
    print("3. Mostrar total por alias")
    print("4. Mostrar las primeras filas")
    print("5. Mostrar tipo de datos")
    print("6. Mostrar valor minimo")
    print("7. Mostrar valor maximo")#alison
    print("8. Seleccionar columnas")
    print("9. Seleccionar filas")
    print("10. Aplicar filtros")
    print("11. valores nulos")
    print("12. Rango valor minuto")#Michelle
    print("13. Mini Dashboard")
    print("14. Cuartiles")
    #print("15. Grafica cuartiles")
    print("16. Salir")

    opcion=input("Seleccione una opcion: ")
    #La opcion uno que nos muestra el orden de mayor a menor
    if opcion == '1':
        print(funcion.ordenado_total(df))
    #La opcion dos que nos muestra el total por porducto
    elif opcion == '2':
        print(funcion.total_por_producto(df))
    #La opcion tres que nos muestra el total por alias
    elif opcion == '3':
        print(funcion.total_por_alias(df))
    #La opcion que nos permite visualizar las filas
    elif opcion =='4' :
        print(funcion.visualizacion_filas(df))
    #La opcion que nos muestra el tipo de datos
    elif opcion == '5':
        print(funcion.tipo_datos(df))
    #La opcion que nos muestra el valor minimo
    elif opcion == '6' :
        print("El valor minimo es: ",funcion.valor_minimo(df))
    #La opcion que nos muestra el valor maximo
    elif opcion == '7':
        print("El valor maximo es: ",funcion.valor_maximo(df))
    elif opcion == "8":
            funcion.seleccionar_columnas(df)
    elif opcion == "9":
        funcion.seleccionar_filas(df)
    elif opcion == "10":
        funcion.aplicar_filtros(df)
    elif opcion == "11":
        funcion.valores_nulos(df)
    elif opcion == "12":
        #muestra el valor maximo y minimo por minuto
        funcion.valorMinutoMax(df)
    elif opcion == "13":
        print(f.crear_dashboard(df))
    elif opcion == "14":
        print(f.imprimir_cuartiles(df))
    #La opcion que rompre el bucle para cerrar el programa
    elif opcion == '16':
        print("Saliendo del programa.")
        break

