from pathlib import Path
import pandas as pd

Estaciones = {
    1:"Primavera",
    2:"Verano",
    3:"Otoño",
    4:"invierno"
}

Climas = {
    1:"Despejado",
    2:"Nublado",
    3:"lluvia o nieble ligera",
    4:"clima severo"
}

Meses = {
    1:"Enero",
    2:"Febrero",
    3:"Marzo",
    4:"Abril",
    5:"Mayo",
    6:"Junio",
    7:"Julio",
    8:"Agosto",
    9:"Septiembre",
    10:"Octubre",
    11:"Noviembre",
    12:"Diciembre"
}

Dias= {
    0:"Lunes",
    1:"Martes",
    2:"Miercoles",
    3:"Jueves",
    4:"Viernes",
    5:"Sabado",
    6:"Domingo"
}


def cargar_datos ():
    ruta = Path(__file__).parent / "Data" / "bicicleta.csv"
    df = pd.read_csv(ruta)

    df["datetime"]=pd.to_datetime(df["datetime"])
    df["Ano"] = df["datetime"].dt.year
    df["Mes N"] = df["datetime"].dt.month
    df["Mes"] = df["Mes N"].map(Meses)
    df["Dia N"] = df["datetime"].dt.dayofweek
    df["Dia"] = df["Dia N"].map(Dias)
    df["Estacion N"] = df["season"].map(Estaciones)
    df["Clima N"] = df["weather"].map(Climas)

    return df


def filtrar_datos(df,Estacion, Clima, Ano, Mes):
    resultado = df.copy()

    if Estacion != "Todos":
        resultado = resultado[resultado["Estacion N"] == Estacion]

    if Clima != "Todos":
            resultado = resultado[resultado["Clima N"] == Clima]

    if Ano != "Todos":
         resultado = resultado[resultado["Ano"] == Ano]

    if Mes != "Todos":
         resultado = resultado[resultado["Mes N"] == Mes]


    return  resultado



def preparar_analisis(df, opcion):
    if opcion == "Rentas por mes":
        datos = df.groupby("Mes N")["count"].sum().reindex(range(1,13))
        datos.index = [Meses[i] for i in datos.index]
        return datos.to_frame("Rentas"), "barras"


    if opcion == "Rentas por horas":
        datos = df.groupby("Hora")["count"].sum()
        return datos.to_frame("Rentas"),"linea"


    if opcion == "Rentas por estacion":
        orden = ["Primavera","Verano","Lluvia o nieve ligera","Clima severo"]
        datos = df.groupby("Estacion N")["count"].sum().reindex(orden)
        return datos.to_frame("Rentas"),"barras"


    if opcion == "Rentas por clima":
        orden = ["Despejado","Nublado","Lluvia o nieve ligera","Clima severo"]
        datos = df.groupby("Clima N")["count"].sum().reindex(orden).dropna()
        return datos.to_frame("Rentas"),"barras"

    if opcion == "Rentas por dia":
        datos = df.groupby("Dia N")["count"].sum().reindex(range(7))
        return datos.to_frame("Rentas"),"barras"