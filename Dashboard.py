import pandas as pd
import matplotlib.pyplot as mp

class Dashboard:
    def __init__(self):
        pass

    # Getter y setter para total_tipo_servicio
    def total_tipo_servicio(self, df):
        return df.groupby("tipo_servicio")["valor_total"].sum()

    # Getter y setter para total_genero_preferencia
    def total_genero_preferencia(self, df):
        return df.groupby("genero_preferencia")["valor_total"].sum()   

    def ganancia_genero(self, df):
        return df.groupby("genero_cliente")["valor_total"].sum() 
    
    def medios_de_pago(self, df):
        return df.groupby("medio_pago")["valor_total"].sum()
    
    #Funcion para crear las graficas correspondientes a la actividad 6
    def crear_dashboard(self, df):
        fig, axes = mp.subplots(2,3, figsize=(10,6))
        #Grafica de barras
        self.total_tipo_servicio(df).plot(kind="bar", ax=axes[0,0], title="Ganancia por tipo de servicio")
        axes[0,0].set_xlabel("Tipo de servicio")
        axes[0,0].set_ylabel("Total Ganancias")
        #Grafica circular
        self.total_genero_preferencia(df).plot(kind="pie", ax=axes[0,1], autopct='%1.1f%%', title="Género de preferencia")
        axes[0,1].set_xlabel("")
        axes[0,1].set_ylabel("")
        #Grafica de caja y bigotes
        mp.sca(axes[0,2])
        mp.boxplot(df["valor_total"], vert=False)
        mp.title("Grafica de Cuartiles")
        #Grafica de barras por genero cliente
        self.ganancia_genero(df).plot(kind="bar", ax=axes[1,0], title="Ganancia genero de preferencia")
        axes[1,0].set_xlabel("Genero del cliente")
        axes[1,0].set_ylabel("Total Ganancias")
        #Grafica de tiempo
        mp.sca(axes[1,1])
        mp.boxplot(df["tiempo_minutos"], vert=False)
        mp.title("Rankin de tiempo")
        #Grafica Medios de pago
        self.medios_de_pago(df).plot(kind="pie", ax=axes[1,2], autopct='%1.1f%%', title="Medios de pago")
        axes[1,2].set_xlabel("")
        axes[1,2].set_ylabel("")
        mp.tight_layout()
        mp.show()
        
    #Funcion para crear cuartiles
    def crear_cuartiles(self, df, columna):
        Q1=df["valor_total"].quantile(0.25)
        Q2=df["valor_total"].quantile(0.50)
        Q3=df["valor_total"].quantile(0.75)
        return Q1, Q2, Q3
    
    #Funcion para imprimir los resultados de los cuartiles en el menu 
    def imprimir_cuartiles(self, df):
        Q1, Q2, Q3 = self.crear_cuartiles(df, "valor_total")
        print("Cuartiles:")
        print("Cuartil N°1:", Q1)
        print("Cuartil N°2:", Q2)
        print("Cuartil N°3:", Q3)
        print()

   
        
        

