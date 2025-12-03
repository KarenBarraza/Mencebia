import pandas
from Archivo import Archivo
import Funciones

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
4. Salir
===========================
""")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            Funciones.seleccionar_columnas(df)
        if opcion == "2":
            Funciones.seleccionar_filas(df)
        
        
menu()