import pandas
from Archivo import Archivo
from Funciones import Funciones
funcion=Funciones()
def menu():
    archivo = Archivo("Buceo_de_la_Concha.csv")
    archivo.leer()
    df=archivo.datos
    while True:
        print("""
===========================
            MENÚ
===========================
1. Seleccionar columnas
2. Seleccionar filas
3. Aplicar filtros
4. valores nulos
5. Salir
===========================
""")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            funcion.seleccionar_columnas(df)
        if opcion == "2":
            funcion.seleccionar_filas(df)
        elif opcion == "3":
            funcion.aplicar_filtros(df)
        elif opcion == "4":
            funcion.valores_nulos(df)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        
menu()