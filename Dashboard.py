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

    def crear_dashboard(self, df):
        fig, axes = mp.subplots(2,1, figsize=(5,5))
        #grafico 1
        self.total_tipo_servicio(df).plot(kind="bar", ax=axes[0], title="Ganancia por tipo de servicio")
        axes[0].set_xlabel("Tipo de servicio")
        axes[0].set_ylabel("Total Ganancias")
        #grafica 2
        self.total_genero_preferencia(df).plot(kind="pie", ax=axes[1], autopct='%1.1f%%', title="Género de preferencia")
        axes[1].set_ylabel("")
        axes[1].set_xlabel("")
        mp.tight_layout()
        mp.show()
