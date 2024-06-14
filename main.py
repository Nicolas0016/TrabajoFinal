import pandas as pd

def cargar_datos(archivo:str, separador:str):
    return pd.read_csv(archivo, sep=separador)

def jugador_mas_joven(datos): 
    return datos[datos.Edad == datos.Edad.min()][["Nombre", "Edad"]]

def jugador_mas_viejo(datos):
    return datos[datos.Edad == datos.Edad.max()][["Nombre", "Edad"]]

def seleccion_mas_valiosa(datos):
    return datos.groupby("Seleccion").Valor_mill_euros.sum().idxmax()

def club_que_mas_aporta(datos): 
    new_dataFrame = datos[datos.Seleccion.isin(["Argentina", "Brasil", "Uruguay"])]
    return new_dataFrame.groupby("Club").Nombre.count().max()
    
def seleccion_con_mas_zurdos(datos):
    return datos.groupby("Seleccion").Destreza_pie.count().idxmax()

def generar_dataframe_edades(datos):
    promedio = datos.groupby("Seleccion").Edad.mean()
    desvio = datos.groupby("Seleccion").Edad.std()
    diccionario = {"promedio": promedio, "desvio":desvio}
    return pd.DataFrame(data=diccionario)


def generar_dataframe_edades_alturas(datos):
    DataFrame_edades = generar_dataframe_edades(datos)
    altura_maxima = datos.groupby("Seleccion").Edad.max()
    altura_minima= datos.groupby("Seleccion").Edad.min()
    pomedio_altura = datos.groupby("Seleccion").Edad.mean()
    
    diccionario = {"altura_maxima":altura_maxima, "altura_minima":altura_minima, "altura_promedio":pomedio_altura}
    DataFrame_Alturas = pd.DataFrame(data=diccionario)
    return pd.concat([DataFrame_edades,DataFrame_Alturas], axis=1)

# Videojuegos