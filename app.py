import streamlit as st
from funciones import cargar_datos, filtrar_datos, preparar_analisis

st.set_page_config(page_title="Renta de bicileta", page_icon="🚲",layout="wide")

df = cargar_datos()

st.title("Analisis de renta y uso de bicileta")
st.write("Bienvenido a la aplicacion de analisis de rentas y usi de bicicletas.")

Inicio,Exploracion,Analisis = st.tabs(["Inicio","Exploracion","Analisis"])

with Inicio:
    st.header("Conociendo mi conjunto de datos")
    st.write("El data set contiene informacion sobre las reantas de bicicletas, fechas,estaciones de ano y otros detalle relevantes.")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Registros", f"{len(df):,}")
    c2.metric("Total de rentas", f"{df['count'].sum():,}")
    c3.metric("Promedio de rentas por mes", f"{df['count'].sum() / df['Mes N'].nunique():,.2f}")
    c4.metric("Promedio por día", f"{df['count'].sum() / df['Dia'].nunique():,.2f}")

st.subheader("Resumen del conjunto de datos")
columnas = ["datetime", "Estacion N","Clima N","temp","humidity","count"]
st.dataframe(df[columnas].head(10), use_container_width=True)

with Exploracion:
    st.header("Exploracion")
    st.write("Esta es la seccion de exloracion de datos.")


with Analisis:
    st.header("Analisis")
    st.write("Esta es la seccion de analisis de datos.")    